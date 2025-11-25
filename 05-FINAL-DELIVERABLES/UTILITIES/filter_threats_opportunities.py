#!/usr/bin/env python3
"""
Filter threats-opportunities.md to include only Maia Learning and top 4 competitors.
Removes: Cialfo, MajorClarity, Common App
Keeps: Maia Learning, Naviance, SCOIR, SchooLinks, Xello
"""

import re

def filter_document(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Track which sections to skip entirely
    skip_sections = {
        '### 🟢 Threat 10: Cialfo Improving (Manifest Integration)',
        '### 🔴 Opportunity 1: Attack Cialfo\'s Asia-Pacific Base (Poor 2.4/5 Reviews)',
        '### 🟡 Opportunity 6: Deepen Common App & Direct Admissions Integration'
    }

    # Process the document
    filtered_lines = []
    skip_until_next_section = False
    in_threat_summary = False
    in_opportunity_summary = False
    in_executive_summary = False

    i = 0
    while i < len(lines):
        line = lines[i]

        # Check if we're entering a section to skip entirely
        if any(skip_section in line for skip_section in skip_sections):
            # Skip until we hit the next ### or ## section
            skip_until_next_section = True
            i += 1
            continue

        # Check if we've reached the next section (stop skipping)
        if skip_until_next_section and (line.startswith('### ') or line.startswith('## ')):
            skip_until_next_section = False

        if skip_until_next_section:
            i += 1
            continue

        # Track if we're in summary sections that need editing
        if '### Threat Summary' in line:
            in_threat_summary = True
        elif '### Opportunity Summary' in line:
            in_opportunity_summary = True
        elif '### Critical Assessment' in line:
            in_executive_summary = True
        elif line.startswith('###') or line.startswith('##'):
            in_threat_summary = False
            in_opportunity_summary = False
            in_executive_summary = False

        # Filter out specific threat/opportunity lines in summaries
        if in_threat_summary:
            if '10. Cialfo improving' in line or '10. Cialfo' in line:
                i += 1
                continue

        if in_opportunity_summary:
            if '1. Attack Cialfo' in line or '6. Deepen Common App' in line:
                i += 1
                continue

        # Filter out mentions of excluded competitors in text
        # But be careful not to remove important context
        if 'MajorClarity' in line:
            # Remove MajorClarity from lists but keep line if it has other content
            line = re.sub(r',?\s*MajorClarity\s*\$5[^,)]*', '', line)
            line = re.sub(r'MajorClarity[^,)]*,?\s*', '', line)

        # Filter Cialfo mentions but keep if it's essential context
        if 'Cialfo' in line and not skip_until_next_section:
            # If it's just a mention in a list of competitors, remove it
            if re.search(r'\(.*Cialfo.*\)', line) or 'vs. Cialfo' in line:
                # Keep line but remove Cialfo reference
                line = re.sub(r',?\s*Cialfo[^,)]*', '', line)
                line = re.sub(r'vs\.\s*Cialfo\s*\$\d+', '', line)
                # Clean up any double commas or trailing commas
                line = re.sub(r',\s*,', ',', line)
                line = re.sub(r',\s*\)', ')', line)

        # Only add non-empty lines or lines that are part of the structure
        if line.strip() or line == '\n':
            filtered_lines.append(line)

        i += 1

    # Write the filtered content
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(filtered_lines)

    print(f"Filtered document written to: {output_file}")
    print(f"Original lines: {len(lines)}")
    print(f"Filtered lines: {len(filtered_lines)}")
    print(f"Lines removed: {len(lines) - len(filtered_lines)}")

if __name__ == '__main__':
    input_file = '/Users/seancurrie/Desktop/MaiaLearningResearch/04-STRATEGIC-INSIGHTS/threats-opportunities.md'
    output_file = '/Users/seancurrie/Desktop/MaiaLearningResearch/05-FINAL-DELIVERABLES/threats-opportunities-top4.md'
    filter_document(input_file, output_file)
