#!/usr/bin/env node

const fs = require('fs');
const { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
        AlignmentType, HeadingLevel, BorderStyle, WidthType, ShadingType,
        VerticalAlign, LevelFormat } = require('docx');

// Read markdown file
const mdPath = process.argv[2] || '05-FINAL-DELIVERABLES/SOURCE-FILES/feature-comparison-matrix-top4.md';
const outputPath = process.argv[3] || '/tmp/feature-comparison-matrix-docxjs.docx';

const mdContent = fs.readFileSync(mdPath, 'utf-8');
const lines = mdContent.split('\n');

// Table border styling
const tableBorder = { style: BorderStyle.SINGLE, size: 1, color: "CCCCCC" };
const cellBorders = { top: tableBorder, bottom: tableBorder, left: tableBorder, right: tableBorder };

// Column widths for 6-column tables (Feature + 5 platforms)
// Letter page with 1" margins = 9360 DXA total width
const COL_WIDTHS = [2400, 1392, 1392, 1392, 1392, 1392]; // Feature column wider

// Helper: Create table cell
function createCell(text, isHeader = false, isBold = false) {
  return new TableCell({
    borders: cellBorders,
    width: { size: COL_WIDTHS[0], type: WidthType.DXA },
    shading: isHeader ? { fill: "D5E8F0", type: ShadingType.CLEAR } : undefined,
    verticalAlign: VerticalAlign.CENTER,
    children: [new Paragraph({
      alignment: isHeader ? AlignmentType.CENTER : AlignmentType.LEFT,
      children: [new TextRun({
        text: text.trim(),
        bold: isHeader || isBold,
        size: isHeader ? 20 : 18
      })]
    })]
  });
}

// Helper: Parse markdown table
function parseTable(startIdx) {
  const rows = [];
  let i = startIdx;

  while (i < lines.length && lines[i].trim().startsWith('|')) {
    const cells = lines[i].split('|')
      .map(c => c.trim())
      .filter(c => c.length > 0 && !c.match(/^-+$/)); // Skip separator rows

    if (cells.length > 0 && !lines[i].includes('---')) {
      rows.push(cells);
    }
    i++;
  }

  return { rows, nextIdx: i };
}

// Helper: Create table from parsed rows
function createTableFromRows(rows) {
  if (rows.length === 0) return null;

  return new Table({
    columnWidths: COL_WIDTHS,
    margins: { top: 80, bottom: 80, left: 100, right: 100 },
    rows: rows.map((cells, rowIdx) => {
      const isHeader = rowIdx === 0;
      return new TableRow({
        tableHeader: isHeader,
        children: cells.map((cellText, colIdx) => {
          const isBold = cellText.startsWith('**') && cellText.endsWith('**');
          const cleanText = cellText.replace(/\*\*/g, '');

          return new TableCell({
            borders: cellBorders,
            width: { size: COL_WIDTHS[colIdx] || COL_WIDTHS[0], type: WidthType.DXA },
            shading: isHeader ? { fill: "D5E8F0", type: ShadingType.CLEAR } : undefined,
            verticalAlign: VerticalAlign.CENTER,
            children: [new Paragraph({
              alignment: isHeader ? AlignmentType.CENTER : AlignmentType.LEFT,
              children: [new TextRun({
                text: cleanText,
                bold: isHeader || isBold,
                size: isHeader ? 20 : 18
              })]
            })]
          });
        })
      });
    })
  });
}

// Helper: Parse bullet list
function parseBulletList(startIdx) {
  const bullets = [];
  let i = startIdx;

  while (i < lines.length && lines[i].trim().startsWith('-')) {
    const text = lines[i].trim().substring(1).trim();
    bullets.push(text);
    i++;
  }

  return { bullets, nextIdx: i };
}

// Parse markdown and build document elements
const children = [];
let i = 0;

while (i < lines.length) {
  const line = lines[i].trim();

  // Headings (H1-H5)
  if (line.startsWith('##### ')) {
    children.push(new Paragraph({
      heading: HeadingLevel.HEADING_5,
      children: [new TextRun(line.substring(6))]
    }));
  }
  else if (line.startsWith('#### ')) {
    children.push(new Paragraph({
      heading: HeadingLevel.HEADING_4,
      children: [new TextRun(line.substring(5))]
    }));
  }
  else if (line.startsWith('### ')) {
    children.push(new Paragraph({
      heading: HeadingLevel.HEADING_3,
      children: [new TextRun(line.substring(4))]
    }));
  }
  else if (line.startsWith('## ')) {
    children.push(new Paragraph({
      heading: HeadingLevel.HEADING_2,
      children: [new TextRun(line.substring(3))]
    }));
  }
  else if (line.startsWith('# ')) {
    children.push(new Paragraph({
      heading: HeadingLevel.TITLE,
      children: [new TextRun(line.substring(2))]
    }));
  }
  // Horizontal rule (skip)
  else if (line.startsWith('---')) {
    // Add spacing instead of visual rule
    children.push(new Paragraph({ text: '' }));
  }
  // Table
  else if (line.startsWith('|')) {
    const { rows, nextIdx } = parseTable(i);
    const table = createTableFromRows(rows);
    if (table) children.push(table);
    i = nextIdx - 1; // -1 because we increment at end of loop
  }
  // Bullet list
  else if (line.startsWith('-') && !line.startsWith('---')) {
    const { bullets, nextIdx } = parseBulletList(i);
    bullets.forEach(bullet => {
      // Parse bold text within bullets
      const parts = [];
      let remaining = bullet;

      while (remaining.includes('**')) {
        const startIdx = remaining.indexOf('**');
        const endIdx = remaining.indexOf('**', startIdx + 2);

        if (endIdx === -1) break;

        // Add text before bold
        if (startIdx > 0) {
          parts.push(new TextRun(remaining.substring(0, startIdx)));
        }

        // Add bold text
        parts.push(new TextRun({
          text: remaining.substring(startIdx + 2, endIdx),
          bold: true
        }));

        remaining = remaining.substring(endIdx + 2);
      }

      // Add remaining text
      if (remaining.length > 0) {
        parts.push(new TextRun(remaining));
      }

      children.push(new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        children: parts.length > 0 ? parts : [new TextRun(bullet)]
      }));
    });
    i = nextIdx - 1;
  }
  // Bold key-value pairs (metadata)
  else if (line.startsWith('**') && line.includes(':')) {
    const parts = [];
    let remaining = line;

    while (remaining.includes('**')) {
      const startIdx = remaining.indexOf('**');
      const endIdx = remaining.indexOf('**', startIdx + 2);

      if (endIdx === -1) break;

      if (startIdx > 0) {
        parts.push(new TextRun(remaining.substring(0, startIdx)));
      }

      parts.push(new TextRun({
        text: remaining.substring(startIdx + 2, endIdx),
        bold: true
      }));

      remaining = remaining.substring(endIdx + 2);
    }

    if (remaining.length > 0) {
      parts.push(new TextRun(remaining));
    }

    children.push(new Paragraph({ children: parts }));
  }
  // Regular paragraph
  else if (line.length > 0) {
    children.push(new Paragraph({ children: [new TextRun(line)] }));
  }

  i++;
}

// Create document
const doc = new Document({
  numbering: {
    config: [{
      reference: "bullet-list",
      levels: [{
        level: 0,
        format: LevelFormat.BULLET,
        text: "•",
        alignment: AlignmentType.LEFT,
        style: { paragraph: { indent: { left: 720, hanging: 360 } } }
      }]
    }]
  },
  styles: {
    default: {
      document: { run: { font: "Arial", size: 22 } } // 11pt default
    },
    paragraphStyles: [
      {
        id: "Title",
        name: "Title",
        basedOn: "Normal",
        run: { size: 48, bold: true, color: "000000", font: "Arial" },
        paragraph: { spacing: { before: 240, after: 240 }, alignment: AlignmentType.LEFT }
      },
      {
        id: "Heading2",
        name: "Heading 2",
        basedOn: "Normal",
        next: "Normal",
        quickFormat: true,
        run: { size: 28, bold: true, color: "000000", font: "Arial" },
        paragraph: { spacing: { before: 240, after: 120 }, outlineLevel: 1 }
      },
      {
        id: "Heading3",
        name: "Heading 3",
        basedOn: "Normal",
        next: "Normal",
        quickFormat: true,
        run: { size: 24, bold: true, color: "000000", font: "Arial" },
        paragraph: { spacing: { before: 180, after: 100 }, outlineLevel: 2 }
      },
      {
        id: "Heading4",
        name: "Heading 4",
        basedOn: "Normal",
        next: "Normal",
        quickFormat: true,
        run: { size: 22, bold: true, color: "000000", font: "Arial" },
        paragraph: { spacing: { before: 140, after: 80 }, outlineLevel: 3 }
      },
      {
        id: "Heading5",
        name: "Heading 5",
        basedOn: "Normal",
        next: "Normal",
        quickFormat: true,
        run: { size: 20, bold: true, color: "000000", font: "Arial" },
        paragraph: { spacing: { before: 120, after: 60 }, outlineLevel: 4 }
      }
    ]
  },
  sections: [{
    properties: {
      page: { margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 } }
    },
    children: children
  }]
});

// Generate DOCX
Packer.toBuffer(doc).then(buffer => {
  fs.writeFileSync(outputPath, buffer);
  console.log(`✅ Successfully generated: ${outputPath}`);
  console.log(`📄 File size: ${(buffer.length / 1024).toFixed(1)} KB`);
}).catch(err => {
  console.error('❌ Error generating document:', err);
  process.exit(1);
});
