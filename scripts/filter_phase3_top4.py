#!/usr/bin/env python3
"""
Filter Phase 3 Comparative Analysis files to focus on Top 4 competitors.

Keeps: Maia Learning, Naviance, SCOIR, SchooLinks, Xello
Removes: Cialfo, MajorClarity, Common App

Works on:
- feature-comparison-matrix.md
- pricing-analysis.md
- market-positioning.md
- technology-stack.md
- target-segments.md
"""

import re
import sys
from pathlib import Path


def filter_table_columns(line, keep_columns):
    """
    Filter markdown table rows to keep only specified columns.
    Handles both header and data rows.
    """
    if not line.strip().startswith('|'):
        return line

    # Split by | and clean up
    cells = [cell.strip() for cell in line.split('|')]
    cells = [c for c in cells if c]  # Remove empty cells from edges

    # If this is a separator row (contains only -, :, spaces, and |)
    if all(c == '' or all(ch in '-: ' for ch in c) for c in cells):
        # Keep same number of columns as header
        return '| ' + ' | '.join(['---'] * len(keep_columns)) + ' |\n'

    # For header and data rows, filter based on column names
    filtered_cells = []
    for i, cell in enumerate(cells):
        # Keep if this column index matches our keep list
        # We need to match against the header row to know which columns to keep
        # For now, we'll use a simpler approach based on content
        filtered_cells.append(cell)

    return '| ' + ' | '.join(filtered_cells) + ' |\n'


def filter_markdown_table(content):
    """
    Filter markdown tables to remove Cialfo, MajorClarity, and Common App columns.
    """
    lines = content.split('\n')
    result = []
    in_table = False
    header_indices = None

    for i, line in enumerate(lines):
        # Detect table start
        if line.strip().startswith('|') and not in_table:
            in_table = True
            # Parse header to find which columns to keep
            cells = [cell.strip() for cell in line.split('|')]
            cells = [c for c in cells if c]

            # Find indices of columns to keep
            keep_columns = []
            header_indices = []
            for idx, cell in enumerate(cells):
                cell_lower = cell.lower().strip('*').strip()
                if cell_lower not in ['cialfo', 'majorclarity', 'common app']:
                    keep_columns.append(cell)
                    header_indices.append(idx)

            result.append('| ' + ' | '.join(keep_columns) + ' |')
            continue

        # Process table rows
        if in_table and line.strip().startswith('|'):
            cells = [cell.strip() for cell in line.split('|')]
            cells = [c for c in cells if c]

            # Check if separator row
            if all(c == '' or all(ch in '-: ' for ch in c) for c in cells):
                result.append('| ' + ' | '.join(['---'] * len(header_indices)) + ' |')
            else:
                # Filter data row
                filtered_cells = [cells[i] for i in header_indices if i < len(cells)]
                result.append('| ' + ' | '.join(filtered_cells) + ' |')
            continue

        # Exit table
        if in_table and not line.strip().startswith('|'):
            in_table = False
            header_indices = None

        result.append(line)

    return '\n'.join(result)


def filter_key_insights(content):
    """
    Clean up Key Insights sections to minimize mentions of excluded competitors.
    Keep mentions that provide context but remove dedicated bullet points.
    """
    lines = content.split('\n')
    result = []
    skip_line = False

    for i, line in enumerate(lines):
        # Skip bullet points that lead with excluded competitors
        if re.match(r'^\s*[-*]\s+\*\*(Cialfo|MajorClarity|Common App)\*\*', line):
            skip_line = True
            continue

        # Remove inline mentions in lists
        line = re.sub(r',?\s*(?:Cialfo|MajorClarity|Common App)[^,);\n]*', '', line)

        # Clean up artifacts
        line = re.sub(r',\s*,', ',', line)
        line = re.sub(r',\s*\)', ')', line)
        line = re.sub(r'\(\s*,', '(', line)
        line = re.sub(r',\s*&', ' &', line)
        line = re.sub(r'&\s*,', '&', line)
        line = re.sub(r'\s+,', ',', line)

        result.append(line)

    return '\n'.join(result)


def update_platform_overview_table(content):
    """
    Update the Platform Overview section to show only 5 platforms (Maia + Top 4).
    """
    # Update any "8 platforms" references to "5 platforms"
    content = re.sub(r'8 platforms', '5 platforms', content, flags=re.IGNORECASE)
    content = re.sub(r'all 8', 'all 5', content, flags=re.IGNORECASE)

    return content


def filter_file(input_path, output_path):
    """
    Filter a single markdown file to remove non-top-4 competitors.
    """
    print(f"\nProcessing: {input_path.name}")

    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Track changes
    original_size = len(content)

    # Apply filters
    content = filter_markdown_table(content)
    content = filter_key_insights(content)
    content = update_platform_overview_table(content)

    # Update document metadata
    content = re.sub(
        r'(\*\*Scope:\*\*\s+)Comprehensive.*?8 platforms',
        r'\1Top 4 Competitors Comparison (Maia, Naviance, SCOIR, SchooLinks, Xello)',
        content
    )

    # Add filtering note at the top
    metadata_section = content.split('---')[0] if '---' in content else ''
    if '**Filtered Version:**' not in metadata_section:
        content = content.replace(
            'platforms\n\n---',
            'platforms\n**Filtered Version:** Top 4 Competitors Focus (Cialfo, MajorClarity, Common App excluded)\n\n---',
            1
        )

    # Write output
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

    new_size = len(content)
    reduction = ((original_size - new_size) / original_size * 100)

    print(f"  ✓ Original: {original_size:,} bytes")
    print(f"  ✓ Filtered: {new_size:,} bytes")
    print(f"  ✓ Reduction: {reduction:.1f}%")
    print(f"  ✓ Saved to: {output_path.name}")


def main():
    # Define paths
    base_dir = Path('/Users/seancurrie/Desktop/MaiaLearningResearch')
    input_dir = base_dir / '03-COMPARATIVE-ANALYSIS'
    output_dir = base_dir / '05-FINAL-DELIVERABLES' / 'SOURCE-FILES'

    # Files to filter
    files_to_filter = [
        'feature-comparison-matrix.md',
        'pricing-analysis.md',
        'market-positioning.md',
        'technology-stack.md',
        'target-segments.md'
    ]

    print("=" * 70)
    print("Phase 3 Comparative Analysis - Top 4 Filtering")
    print("=" * 70)
    print(f"\nInput:  {input_dir}")
    print(f"Output: {output_dir}")
    print(f"\nKeeping: Maia Learning, Naviance, SCOIR, SchooLinks, Xello")
    print(f"Removing: Cialfo, MajorClarity, Common App")

    # Ensure output directory exists
    output_dir.mkdir(parents=True, exist_ok=True)

    # Filter each file
    for filename in files_to_filter:
        input_path = input_dir / filename
        output_filename = filename.replace('.md', '-top4.md')
        output_path = output_dir / output_filename

        if not input_path.exists():
            print(f"\n⚠️  WARNING: {filename} not found, skipping...")
            continue

        filter_file(input_path, output_path)

    print("\n" + "=" * 70)
    print("✅ FILTERING COMPLETE")
    print("=" * 70)
    print(f"\nNext steps:")
    print(f"1. Review filtered files in: {output_dir}")
    print(f"2. Convert to .docx using Pandoc")
    print(f"3. Move .docx files to COMPARATIVE-ANALYSIS-TOP4/ folder")


if __name__ == '__main__':
    main()
