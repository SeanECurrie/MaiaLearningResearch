const fs = require('fs');
const { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
        AlignmentType, HeadingLevel, BorderStyle, WidthType, ShadingType,
        VerticalAlign, LevelFormat } = require('docx');

const mdContent = fs.readFileSync('05-FINAL-DELIVERABLES/SOURCE-FILES/feature-comparison-matrix-top4.md', 'utf-8');
const lines = mdContent.split('\n');

const border = { style: BorderStyle.SINGLE, size: 1, color: "CCCCCC" };
const cellBorders = { top: border, bottom: border, left: border, right: border };
const COL_WIDTHS = [2400, 1392, 1392, 1392, 1392, 1392];

function createCell(text, isHeader, isBold, colIdx) {
  return new TableCell({
    borders: cellBorders,
    width: { size: COL_WIDTHS[colIdx] || COL_WIDTHS[0], type: WidthType.DXA },
    shading: isHeader ? { fill: "D5E8F0", type: ShadingType.CLEAR } : undefined,
    verticalAlign: VerticalAlign.CENTER,
    children: [new Paragraph({
      alignment: isHeader ? AlignmentType.CENTER : AlignmentType.LEFT,
      children: [new TextRun({
        text: text.replace(/\*\*/g, '').trim(),
        bold: isHeader || isBold,
        size: isHeader ? 20 : 18
      })]
    })]
  });
}

function parseTable(idx) {
  const rows = [];
  let i = idx;
  while (i < lines.length && lines[i].trim().startsWith('|')) {
    const cells = lines[i].split('|').map(c => c.trim()).filter(c => c && !c.match(/^-+$/));
    if (cells.length > 0) rows.push(cells);
    i++;
  }
  return { rows, nextIdx: i };
}

function parseBullets(idx) {
  const bullets = [];
  let i = idx;
  while (i < lines.length && lines[i].trim().startsWith('-') && !lines[i].startsWith('---')) {
    bullets.push(lines[i].trim().substring(1).trim());
    i++;
  }
  return { bullets, nextIdx: i };
}

function parseBoldText(text) {
  const parts = [];
  let remaining = text;
  while (remaining.includes('**')) {
    const start = remaining.indexOf('**');
    const end = remaining.indexOf('**', start + 2);
    if (end === -1) {
      // Incomplete ** - just remove it and continue
      remaining = remaining.substring(0, start) + remaining.substring(start + 2);
      break;
    }
    if (start > 0) parts.push(new TextRun(remaining.substring(0, start)));
    parts.push(new TextRun({ text: remaining.substring(start + 2, end), bold: true }));
    remaining = remaining.substring(end + 2);
  }
  if (remaining) parts.push(new TextRun(remaining));
  return parts.length > 0 ? parts : [new TextRun(text)];
}

function parseNumberedList(idx) {
  const items = [];
  let i = idx;
  while (i < lines.length && lines[i].trim().match(/^\d+\.\s/)) {
    const text = lines[i].trim().replace(/^\d+\.\s+/, '');
    if (text && text !== '**') items.push(text);
    i++;
  }
  return { items, nextIdx: i };
}

const children = [];
let i = 0;

while (i < lines.length) {
  const line = lines[i].trim();

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
  else if (line.startsWith('---')) {
    children.push(new Paragraph({ text: '' }));
  }
  else if (line.startsWith('|')) {
    const { rows, nextIdx } = parseTable(i);
    if (rows.length > 0) {
      children.push(new Table({
        columnWidths: COL_WIDTHS,
        margins: { top: 80, bottom: 80, left: 100, right: 100 },
        rows: rows.map((cells, rowIdx) => new TableRow({
          tableHeader: rowIdx === 0,
          children: cells.map((cellText, colIdx) =>
            createCell(cellText, rowIdx === 0, cellText.startsWith('**'), colIdx))
        }))
      }));
    }
    i = nextIdx - 1;
  }
  else if (line.startsWith('-') && !line.startsWith('---')) {
    const { bullets, nextIdx } = parseBullets(i);
    bullets.forEach(bullet => {
      children.push(new Paragraph({
        numbering: { reference: "bullet-list", level: 0 },
        children: parseBoldText(bullet)
      }));
    });
    i = nextIdx - 1;
  }
  else if (line.match(/^\d+\.\s/)) {
    const { items, nextIdx } = parseNumberedList(i);
    items.forEach(item => {
      children.push(new Paragraph({
        numbering: { reference: "numbered-list", level: 0 },
        children: parseBoldText(item)
      }));
    });
    i = nextIdx - 1;
  }
  else if (line.startsWith('**') && line.includes(':')) {
    children.push(new Paragraph({ children: parseBoldText(line) }));
  }
  else if (line.length > 0) {
    children.push(new Paragraph({ children: parseBoldText(line) }));
  }

  i++;
}

const doc = new Document({
  numbering: {
    config: [
      {
        reference: "bullet-list",
        levels: [{
          level: 0,
          format: LevelFormat.BULLET,
          text: "•",
          alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 720, hanging: 360 } } }
        }]
      },
      {
        reference: "numbered-list",
        levels: [{
          level: 0,
          format: LevelFormat.DECIMAL,
          text: "%1.",
          alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 720, hanging: 360 } } }
        }]
      }
    ]
  },
  styles: {
    default: { document: { run: { font: "Arial", size: 22 } } },
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

Packer.toBuffer(doc).then(buffer => {
  fs.writeFileSync('05-FINAL-DELIVERABLES/COMPARATIVE-ANALYSIS-TOP4/feature-comparison-matrix-top4.docx', buffer);
  console.log('✅ DOCX created successfully!');
  console.log('📄 File: 05-FINAL-DELIVERABLES/COMPARATIVE-ANALYSIS-TOP4/feature-comparison-matrix-top4.docx');
  console.log('📊 Size: ' + (buffer.length / 1024).toFixed(1) + ' KB');
});
