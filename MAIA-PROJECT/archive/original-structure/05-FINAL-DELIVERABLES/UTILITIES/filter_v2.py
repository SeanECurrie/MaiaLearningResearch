#!/usr/bin/env python3
"""
Filter threats-opportunities.md to include only Maia Learning and top 4 competitors.
Removes: Cialfo, MajorClarity, Common App (as main topics)
Keeps: Maia Learning, Naviance, SCOIR, SchooLinks, Xello
"""

import re

def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def filter_document(input_file, output_file):
    content = read_file(input_file)

    # Split into sections
    lines = content.split('\n')

    filtered_lines = []
    skip_mode = False
    skip_until_marker = None

    i = 0
    while i < len(lines):
        line = lines[i]

        # Detect sections to skip entirely
        if '### 🟢 Threat 10: Cialfo Improving (Manifest Integration)' in line:
            # Skip until next ### or ##
            skip_mode = True
            skip_until_marker = r'^###? '
        elif '### 🔴 Opportunity 1: Attack Cialfo\'s Asia-Pacific Base' in line:
            skip_mode = True
            skip_until_marker = r'^###? '
        elif '### 🟡 Opportunity 6: Deepen Common App & Direct Admissions Integration' in line:
            skip_mode = True
            skip_until_marker = r'^###? '

        # Check if we should stop skipping
        if skip_mode and skip_until_marker and i > 0:
            if re.match(skip_until_marker, line) and not any(x in line for x in ['Cialfo', 'Common App & Direct Admissions']):
                skip_mode = False
                skip_until_marker = None

        # Skip if in skip mode
        if skip_mode:
            i += 1
            continue

        # Process the line for inline filtering
        original_line = line

        # Remove MajorClarity mentions
        line = re.sub(r',?\s*MajorClarity[^,);\n]*', '', line)

        # Handle specific list items to remove
        if '10. Cialfo improving (Manifest integration)' in line:
            i += 1
            continue
        if '1. Attack Cialfo' in line:
            i += 1
            continue
        if '6. Deepen Common App & Direct Admissions integration' in line:
            i += 1
            continue

        # Clean up artifacts
        line = re.sub(r',\s*,', ',', line)
        line = re.sub(r',\s*\)', ')', line)
        line = re.sub(r'\(\s*,', '(', line)
        line = re.sub(r',\s*$', '', line)

        filtered_lines.append(line)
        i += 1

    # Join back and fix numbering in summaries
    result = '\n'.join(filtered_lines)

    # Fix Threat Summary - should be 9 total now (removed Threat 10)
    result = re.sub(
        r'### Threat Summary \(10 Total\)',
        '### Threat Summary (9 Total)',
        result
    )

    # Fix Opportunity Summary - should be 9 total now (removed 3)
    result = re.sub(
        r'### Opportunity Summary \(12 Total\)',
        '### Opportunity Summary (9 Total)',
        result
    )

    # Fix the opportunity numbering in summary
    # After removing #1 and #6, renumber:
    # OLD: 2,3,4 -> NEW: 1,2,3
    # OLD: 5,7,8,9 -> NEW: 4,5,6,7
    # OLD: 10,11,12 -> NEW: 8,9,10 (but we only have 9 total, so 7,8,9)

    opportunity_summary_section = re.search(
        r'(### Opportunity Summary.*?)(---)',
        result,
        re.DOTALL
    )

    if opportunity_summary_section:
        old_section = opportunity_summary_section.group(1)
        new_section = old_section

        # Update the HIGH opportunities count from 4 to 3
        new_section = re.sub(
            r'\*\*🔴 VERY HIGH \(4 opportunities\):\*\*',
            '**🔴 VERY HIGH (3 opportunities):**',
            new_section
        )

        # Update MEDIUM-HIGH from 5 to 4
        new_section = re.sub(
            r'\*\*🟡 MEDIUM-HIGH \(5 opportunities\):\*\*',
            '**🟡 MEDIUM-HIGH (4 opportunities):**',
            new_section
        )

        # Now renumber the items
        # Change 2. -> 1., 3. -> 2., 4. -> 3.
        new_section = re.sub(r'^2\. Develop international', '1. Develop international', new_section, flags=re.MULTILINE)
        new_section = re.sub(r'^3\. First-mover', '2. First-mover', new_section, flags=re.MULTILINE)
        new_section = re.sub(r'^4\. Target Naviance', '3. Target Naviance', new_section, flags=re.MULTILINE)

        # Change 5. -> 4., 7. -> 5., 8. -> 6., 9. -> 7.
        new_section = re.sub(r'^5\. Tiered pricing', '4. Tiered pricing', new_section, flags=re.MULTILINE)
        new_section = re.sub(r'^7\. White space', '5. White space', new_section, flags=re.MULTILINE)
        new_section = re.sub(r'^8\. Enhanced AI career', '6. Enhanced AI career', new_section, flags=re.MULTILINE)
        new_section = re.sub(r'^9\. Publish customer', '7. Publish customer', new_section, flags=re.MULTILINE)

        # Change 10. -> 8., 11. -> 9., 12. -> 10. (but we said 9 total)
        # Actually we have: HIGH(3) + MEDIUM-HIGH(4) + MEDIUM(3) = 10 total
        # So let's recalculate: removed 3 ops, so 12-3 = 9 total
        # HIGH: 4-1=3, MEDIUM-HIGH: 5-2=3, MEDIUM: 3
        # Wait, I need to check which category #6 was in

        # Let me recount: Removed #1 (HIGH), #6 (MEDIUM-HIGH), so:
        # HIGH: 4-1 = 3 (correct)
        # MEDIUM-HIGH: 5-1 = 4 (correct as updated above)
        # MEDIUM: 3 (unchanged)
        # Total: 3+4+3 = 10 total! Not 9

        result = result.replace(opportunity_summary_section.group(1), new_section)

    # Fix total count to 10
    result = re.sub(
        r'### Opportunity Summary \(9 Total\)',
        '### Opportunity Summary (10 Total)',
        result
    )

    write_file(output_file, result)

    print(f"Filtered document written to: {output_file}")
    print(f"Removed sections: Threat 10 (Cialfo), Opportunity 1 (Cialfo), Opportunity 6 (Common App)")

if __name__ == '__main__':
    input_file = '/Users/seancurrie/Desktop/MaiaLearningResearch/04-STRATEGIC-INSIGHTS/threats-opportunities.md'
    output_file = '/Users/seancurrie/Desktop/MaiaLearningResearch/05-FINAL-DELIVERABLES/threats-opportunities-top4.md'
    filter_document(input_file, output_file)
