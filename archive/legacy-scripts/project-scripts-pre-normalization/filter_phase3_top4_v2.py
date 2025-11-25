#!/usr/bin/env python3
"""
Filter Phase 3 Comparative Analysis files to focus on Top 4 competitors (VERSION 2 - FIXED).

Keeps: Maia Learning, Naviance, SCOIR, SchooLinks, Xello
Removes: Cialfo, MajorClarity, Common App

Improvements over v1:
- Better table column filtering
- Prose text cleanup for removed competitors
- Handles incomplete sentences and lists
"""

import re
from pathlib import Path


def filter_markdown_tables(content):
    """
    Filter markdown tables to remove columns for excluded competitors.
    """
    lines = content.split('\n')
    result = []
    in_table = False
    header_indices = None
    removed_competitors = ['cialfo', 'majorclarity', 'common app']

    for i, line in enumerate(lines):
        # Detect table start (line with | that's not just separator)
        if line.strip().startswith('|') and not in_table:
            # Check if it's a header (not all dashes)
            if not all(c in '|- :' for c in line.strip()):
                in_table = True
                # Parse header to find columns to keep
                cells = [cell.strip() for cell in line.split('|')]
                cells = [c for c in cells if c]  # Remove empty from edges

                # Find which columns to keep
                keep_columns = []
                header_indices = []
                for idx, cell in enumerate(cells):
                    cell_lower = cell.lower().strip('*').strip()
                    # Check if this is a removed competitor
                    is_removed = any(comp in cell_lower for comp in removed_competitors)
                    if not is_removed:
                        keep_columns.append(cell)
                        header_indices.append(idx)

                # Rebuild header row
                result.append('| ' + ' | '.join(keep_columns) + ' |')
                continue

        # Process table rows
        if in_table and line.strip().startswith('|'):
            cells = [cell.strip() for cell in line.split('|')]
            cells = [c for c in cells if c]  # Remove empty from edges

            # Check if separator row
            if all(c == '' or all(ch in '-: ' for ch in c) for c in cells):
                result.append('| ' + ' | '.join(['---'] * len(header_indices)) + ' |')
            else:
                # Filter data row based on header indices
                if header_indices and len(cells) >= max(header_indices) + 1:
                    filtered_cells = [cells[i] for i in header_indices]
                    result.append('| ' + ' | '.join(filtered_cells) + ' |')
                else:
                    # Skip malformed rows
                    continue
            continue

        # Exit table when we hit a non-table line
        if in_table and not line.strip().startswith('|'):
            in_table = False
            header_indices = None

        result.append(line)

    return '\n'.join(result)


def clean_prose_references(content):
    """
    Clean up prose text that mentions removed competitors.
    Remove them from lists and fix sentence grammar.
    """
    # Remove from comma-separated lists
    content = re.sub(r',?\s*Cialfo[^,);\n\.]*', '', content)
    content = re.sub(r',?\s*MajorClarity[^,);\n\.]*', '', content)
    content = re.sub(r',?\s*Common App[^,);\n\.]*', '', content)

    # Fix "Only)" -> "Only Cialfo" was removed, need to handle these cases
    # Better to remove the entire sentence/bullet if it's only about removed competitors
    content = re.sub(r'\d+\.\s+\*\*Premium Pricing:\*\*\s+Only\)[^\n]*\n', '', content)

    # Remove bullet points that start with removed competitors
    content = re.sub(r'^\s*[-*]\s+\*\*(Cialfo|MajorClarity|Common App)\*\*[^\n]*\n', '', content, flags=re.MULTILINE)

    # Clean up double commas, leading/trailing commas
    content = re.sub(r',\s*,', ',', content)
    content = re.sub(r',\s*\)', ')', content)
    content = re.sub(r'\(\s*,', '(', content)
    content = re.sub(r',\s*&', ' &', content)
    content = re.sub(r'&\s*,', '&', content)
    content = re.sub(r'\s+,', ',', content)

    # Fix lines ending with "Maia," or "Xello," or other incomplete lists
    content = re.sub(r'(\*\*Maia),?\s*$', r'\1', content, flags=re.MULTILINE)
    content = re.sub(r'(\*\*Xello),?\s*$', r'\1', content, flags=re.MULTILINE)
    content = re.sub(r'(\*\*Maia\s*&)\s*$', r'\1 Xello', content, flags=re.MULTILINE)

    # Remove ranking lines that reference removed competitors (e.g., "4. Cialfo")
    content = re.sub(r'^\d+\.\s*$', '', content, flags=re.MULTILINE)

    # Fix "**Common App Integration**" row that's incomplete
    content = re.sub(r'\|\s+\*\*\s*\|\s*$', '', content, flags=re.MULTILINE)

    return content


def update_counts(content):
    """
    Update document metadata to reflect filtering (8 platforms -> 5 platforms).
    """
    # Update platform counts
    content = re.sub(r'8 platforms', '5 platforms', content, flags=re.IGNORECASE)
    content = re.sub(r'all 8', 'top 5', content, flags=re.IGNORECASE)
    content = re.sub(r'across 8', 'across 5', content, flags=re.IGNORECASE)

    # Update pricing tables "7 platforms" -> "5 platforms" (excluding Common App which is N/A)
    content = re.sub(r'7 platforms', '5 platforms', content, flags=re.IGNORECASE)

    return content


def add_filtering_note(content):
    """
    Add a note at the top indicating this is a filtered version.
    """
    # Check if filtering note already exists
    if '**Filtered Version:**' in content:
        return content

    # Find first --- separator and add note before it
    parts = content.split('\n---\n', 1)
    if len(parts) == 2:
        header, rest = parts
        # Add filtering note to header
        header += '\n**Filtered Version:** Top 4 Competitors Focus (Cialfo, MajorClarity, Common App excluded)\n'
        content = header + '\n---\n' + rest

    return content


def filter_file(input_path, output_path):
    """
    Filter a single markdown file to remove non-top-4 competitors.
    """
    print(f"\nProcessing: {input_path.name}")

    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_size = len(content)

    # Apply filters in sequence
    content = filter_markdown_tables(content)
    content = clean_prose_references(content)
    content = update_counts(content)
    content = add_filtering_note(content)

    # Final cleanup: remove excessive blank lines
    content = re.sub(r'\n{4,}', '\n\n\n', content)

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
    print("Phase 3 Comparative Analysis - Top 4 Filtering (VERSION 2 - FIXED)")
    print("=" * 70)
    print(f"\nInput:  {input_dir}")
    print(f"Output: {output_dir}")
    print(f"\nKeeping: Maia Learning, Naviance, SCOIR, SchooLinks, Xello")
    print(f"Removing: Cialfo, MajorClarity, Common App")
    print(f"\nFixes: Better table filtering, prose cleanup, grammar fixes")

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
    print("✅ FILTERING COMPLETE (V2)")
    print("=" * 70)
    print(f"\nNext steps:")
    print(f"1. Review filtered files for quality")
    print(f"2. Convert to .docx using Pandoc")
    print(f"3. Move .docx files to COMPARATIVE-ANALYSIS-TOP4/ folder")


if __name__ == '__main__':
    main()
