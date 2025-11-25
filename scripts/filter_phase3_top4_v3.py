#!/usr/bin/env python3
"""
Filter Phase 3 Comparative Analysis files to focus on Top 4 competitors (VERSION 3 - COMPLETE FIX).

Keeps: Maia Learning, Naviance, SCOIR, SchooLinks, Xello
Removes: Cialfo, MajorClarity, Common App

KEY FIX: Properly handles two types of tables:
1. Platform Overview table (remove ROWS for excluded competitors)
2. Feature comparison tables (remove COLUMNS for excluded competitors)
"""

import re
from pathlib import Path


REMOVED_COMPETITORS = ['cialfo', 'majorclarity', 'common app']


def is_platform_overview_table(header_line):
    """Check if this is the Platform Overview table (special case)."""
    return '| Platform | Founded | Focus |' in header_line or '| Platform | Price/Student |' in header_line


def should_remove_row(row_text):
    """Check if a table row should be completely removed (contains excluded competitor)."""
    row_lower = row_text.lower()
    for comp in REMOVED_COMPETITORS:
        # Check if row starts with the competitor name (after |)
        if f'| **{comp}' in row_lower or f'|**{comp}' in row_lower:
            return True
        # Check for fragments like "| **, " which are broken rows
        if row_text.strip().startswith('| **,') or row_text.strip().startswith('| **)'):
            return True
    return False


def filter_platform_overview_table(lines, start_idx):
    """
    Special handling for Platform Overview table - removes entire rows for excluded competitors.
    Returns (filtered_lines, next_index)
    """
    result = []
    i = start_idx

    # Add header
    result.append(lines[i])
    i += 1

    # Add separator
    if i < len(lines) and lines[i].strip().startswith('|'):
        result.append(lines[i])
        i += 1

    # Process data rows
    while i < len(lines) and lines[i].strip().startswith('|'):
        row = lines[i]
        if not should_remove_row(row):
            result.append(row)
        i += 1

    return result, i


def filter_feature_table(lines, start_idx):
    """
    Standard table filtering - removes columns for excluded competitors.
    Returns (filtered_lines, next_index)
    """
    result = []
    i = start_idx

    # Parse header to find columns to keep
    header = lines[i]
    cells = [cell.strip() for cell in header.split('|')]
    cells = [c for c in cells if c]  # Remove empty

    keep_indices = []
    keep_columns = []
    for idx, cell in enumerate(cells):
        cell_lower = cell.lower().strip('*').strip()
        is_removed = any(comp in cell_lower for comp in REMOVED_COMPETITORS)
        if not is_removed:
            keep_indices.append(idx)
            keep_columns.append(cell)

    result.append('| ' + ' | '.join(keep_columns) + ' |')
    i += 1

    # Process remaining table rows
    while i < len(lines) and lines[i].strip().startswith('|'):
        row = lines[i]
        cells = [cell.strip() for cell in row.split('|')]
        cells = [c for c in cells if c]

        # Check if separator row
        if all(c == '' or all(ch in '-: ' for ch in c) for c in cells):
            result.append('| ' + ' | '.join(['---'] * len(keep_indices)) + ' |')
        else:
            # Filter columns
            if len(cells) >= max(keep_indices) + 1:
                filtered_cells = [cells[idx] for idx in keep_indices]
                result.append('| ' + ' | '.join(filtered_cells) + ' |')
        i += 1

    return result, i


def filter_markdown_tables(content):
    """
    Filter all markdown tables, using appropriate method for each.
    """
    lines = content.split('\n')
    result = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # Detect table start
        if line.strip().startswith('|') and not all(c in '|- :' for c in line.strip()):
            # Determine table type and filter accordingly
            if is_platform_overview_table(line):
                filtered_table, next_i = filter_platform_overview_table(lines, i)
                result.extend(filtered_table)
                i = next_i
            else:
                filtered_table, next_i = filter_feature_table(lines, i)
                result.extend(filtered_table)
                i = next_i
        else:
            result.append(line)
            i += 1

    return '\n'.join(result)


def clean_prose_references(content):
    """
    Clean up prose text that mentions removed competitors.
    """
    # Remove incomplete bullet points (just "- **)" or similar)
    content = re.sub(r'^\s*[-*]\s+\*\*\)\s*$', '', content, flags=re.MULTILINE)
    content = re.sub(r'^\s*[-*]\s+\*\*,\s*$', '', content, flags=re.MULTILINE)

    # Remove from comma-separated lists
    content = re.sub(r',?\s*Cialfo[^,);\n\.]*', '', content)
    content = re.sub(r',?\s*MajorClarity[^,);\n\.]*', '', content)
    content = re.sub(r',?\s*Common App[^,);\n\.]*', '', content)

    # Remove bullet points that start with removed competitors
    content = re.sub(r'^\s*[-*]\s+\*\*(Cialfo|MajorClarity|Common App)\*\*[^\n]*\n', '', content, flags=re.MULTILINE)

    # Clean up artifacts
    content = re.sub(r',\s*,', ',', content)
    content = re.sub(r',\s*\)', ')', content)
    content = re.sub(r'\(\s*,', '(', content)
    content = re.sub(r',\s*&', ' &', content)
    content = re.sub(r'&\s*,', '&', content)
    content = re.sub(r'\s+,', ',', content)

    # Fix incomplete Key Insights lines
    content = re.sub(r'(\*\*Maia),\s+\*\*Xello\s*$', r'\1 and **Xello**', content, flags=re.MULTILINE)
    content = re.sub(r'(\*\*Maia)\s+\*\*Xello\s*$', r'\1 and **Xello**', content, flags=re.MULTILINE)
    content = re.sub(r'(\*\*Maia)\s*&\s*$', r'\1 and Xello', content, flags=re.MULTILINE)
    content = re.sub(r'(\*\*Maia)\s*&\s+\*\*Xello\s*$', r'\1 and **Xello**', content, flags=re.MULTILINE)

    # Remove orphaned price ranking numbers
    content = re.sub(r'^\d+\.\s*$', '', content, flags=re.MULTILINE)

    # Remove incomplete numbered items in summaries
    content = re.sub(r'^\d+\.\s+\*\*[^:]*:\*\*\s+Only\)[^\n]*\n', '', content, flags=re.MULTILINE)

    # Fix numbering gaps in Key Findings (e.g., 1, 2, 3, 5, 6 -> 1, 2, 3, 4, 5)
    lines = content.split('\n')
    in_numbered_list = False
    counter = 1
    result = []

    for line in lines:
        # Detect start of numbered list in Key Findings
        if line.strip() == '**Key Findings:**':
            in_numbered_list = True
            counter = 1
            result.append(line)
            continue

        if in_numbered_list:
            # Check if this is a numbered item
            match = re.match(r'^(\d+)\.\s+(.*)$', line)
            if match:
                # Renumber sequentially
                result.append(f'{counter}. {match.group(2)}')
                counter += 1
            elif line.strip() == '' or line.startswith('#') or line.startswith('---'):
                # End of numbered list
                in_numbered_list = False
                result.append(line)
            else:
                result.append(line)
        else:
            result.append(line)

    content = '\n'.join(result)

    return content


def update_counts(content):
    """Update platform counts from 8/7 to 5."""
    content = re.sub(r'8 platforms', '5 platforms', content, flags=re.IGNORECASE)
    content = re.sub(r'all 8', 'top 5', content, flags=re.IGNORECASE)
    content = re.sub(r'across 8', 'across 5', content, flags=re.IGNORECASE)
    content = re.sub(r'7 platforms', '5 platforms', content, flags=re.IGNORECASE)
    return content


def add_filtering_note(content):
    """Add filtering note if not present."""
    if '**Filtered Version:**' in content:
        return content

    parts = content.split('\n---\n', 1)
    if len(parts) == 2:
        header, rest = parts
        header += '\n**Filtered Version:** Top 4 Competitors Focus (Cialfo, MajorClarity, Common App excluded)\n'
        content = header + '\n---\n' + rest

    return content


def filter_file(input_path, output_path):
    """Filter a single markdown file."""
    print(f"\nProcessing: {input_path.name}")

    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_size = len(content)

    # Apply filters
    content = filter_markdown_tables(content)
    content = clean_prose_references(content)
    content = update_counts(content)
    content = add_filtering_note(content)

    # Final cleanup
    content = re.sub(r'\n{4,}', '\n\n\n', content)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

    new_size = len(content)
    reduction = ((original_size - new_size) / original_size * 100)

    print(f"  ✓ Original: {original_size:,} bytes")
    print(f"  ✓ Filtered: {new_size:,} bytes")
    print(f"  ✓ Reduction: {reduction:.1f}%")


def main():
    base_dir = Path('/Users/seancurrie/Desktop/MaiaLearningResearch')
    input_dir = base_dir / '03-COMPARATIVE-ANALYSIS'
    output_dir = base_dir / '05-FINAL-DELIVERABLES' / 'SOURCE-FILES'

    files_to_filter = [
        'feature-comparison-matrix.md',
        'pricing-analysis.md',
        'market-positioning.md',
        'technology-stack.md',
        'target-segments.md'
    ]

    print("=" * 70)
    print("Phase 3 Top-4 Filtering (V3 - COMPLETE FIX)")
    print("=" * 70)
    print("\nKeeping: Maia, Naviance, SCOIR, SchooLinks, Xello")
    print("Removing: Cialfo, MajorClarity, Common App\n")

    output_dir.mkdir(parents=True, exist_ok=True)

    for filename in files_to_filter:
        input_path = input_dir / filename
        output_filename = filename.replace('.md', '-top4.md')
        output_path = output_dir / output_filename

        if input_path.exists():
            filter_file(input_path, output_path)

    print("\n" + "=" * 70)
    print("✅ COMPLETE - All files filtered successfully")
    print("=" * 70)


if __name__ == '__main__':
    main()
