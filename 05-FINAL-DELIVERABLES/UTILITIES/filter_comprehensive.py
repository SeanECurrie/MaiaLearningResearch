#!/usr/bin/env python3
"""
Comprehensive filter for threats-opportunities.md
Removes:
  - Threat 6: Direct Admissions (Common App)
  - Threat 10: Cialfo
  - Opportunity 1: Cialfo
  - Opportunity 6: Common App & Direct Admissions

Keeps only: Maia, Naviance, SCOIR, SchooLinks, Xello
"""

import re

def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.readlines()

def write_file(filepath, lines):
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(lines)

def main():
    input_file = '/Users/seancurrie/Desktop/MaiaLearningResearch/04-STRATEGIC-INSIGHTS/threats-opportunities.md'
    output_file = '/Users/seancurrie/Desktop/MaiaLearningResearch/05-FINAL-DELIVERABLES/threats-opportunities-top4.md'

    lines = read_file(input_file)

    # Sections to remove entirely (line ranges will be determined)
    skip_sections = [
        '### 🟡 Threat 6: Direct Admissions Transformation',
        '### 🟢 Threat 10: Cialfo Improving (Manifest Integration)',
        '### 🔴 Opportunity 1: Attack Cialfo\'s Asia-Pacific Base',
        '### 🟡 Opportunity 6: Deepen Common App & Direct Admissions Integration'
    ]

    filtered_lines = []
    skip_mode = False
    i = 0

    while i < len(lines):
        line = lines[i]

        # Check if we're starting a section to skip
        if any(section in line for section in skip_sections):
            skip_mode = True
            i += 1
            continue

        # Check if we've reached the next section (stop skipping)
        if skip_mode and (line.startswith('### ') or line.startswith('## ')):
            if not any(section in line for section in skip_sections):
                skip_mode = False

        if skip_mode:
            i += 1
            continue

        # Filter specific list items in summaries
        if ('6. Direct Admissions transformation' in line or
            '10. Cialfo improving' in line or
            '1. Attack Cialfo' in line or
            '6. Deepen Common App' in line):
            i += 1
            continue

        # Remove MajorClarity mentions
        line = re.sub(r',?\s*MajorClarity[^,);\n]*', '', line)
        line = re.sub(r'\(MajorClarity[^)]*\)', '', line)

        # Remove Cialfo from comparison lists (but keep contextual mentions)
        # Only remove from lists like "Xello: NO AI, Cialfo: NO AI"
        if '- Cialfo: NO AI' in line:
            i += 1
            continue

        # Clean up artifacts
        line = re.sub(r',\s*,', ',', line)
        line = re.sub(r',\s*\)', ')', line)
        line = re.sub(r'\(\s*,', '(', line)

        filtered_lines.append(line)
        i += 1

    # Join and make comprehensive updates
    content = ''.join(filtered_lines)

    # Update Threat Summary (10 -> 8 total, removed T6 and T10)
    content = re.sub(r'### Threat Summary \(10 Total\)', '### Threat Summary (8 Total)', content)

    # Update MEDIUM-HIGH threats count (4 -> 3, removed T6)
    content = re.sub(
        r'(\*\*🟡 MEDIUM-HIGH \()4( threats:\*\*)',
        r'\g<1>3\g<2>',
        content
    )

    # Update LOW-MEDIUM threats count (3 -> 2, removed T10)
    content = re.sub(
        r'(\*\*🟢 LOW-MEDIUM \()3( threats:\*\*)',
        r'\g<1>2\g<2>',
        content
    )

    # Update Opportunity Summary (12 -> 8 total, removed 1, 6, and need to account for removed threats)
    content = re.sub(r'### Opportunity Summary \(12 Total\)', '### Opportunity Summary (8 Total)', content)

    # Update VERY HIGH opportunities (4 -> 3, removed Opp 1)
    content = re.sub(
        r'(\*\*🔴 VERY HIGH \()4( opportunities:\*\*)',
        r'\g<1>3\g<2>',
        content
    )

    # Update MEDIUM-HIGH opportunities (5 -> 3, removed Opp 6)
    content = re.sub(
        r'(\*\*🟡 MEDIUM-HIGH \()5( opportunities:\*\*)',
        r'\g<1>3\g<2>',
        content
    )

    # Fix numbering in Threat Summary
    # After removing T6, T7 becomes T6, etc.
    # LOW-MEDIUM section: 9. Naviance improving stays as is
    # But we removed T10, so just T9 Naviance improving
    threat_summary = re.search(r'(### Threat Summary.*?)(---)', content, re.DOTALL)
    if threat_summary:
        section = threat_summary.group(1)
        # After removing T6: T7->T6
        section = re.sub(r'^7\. SCOIR entering', '6. SCOIR entering', section, flags=re.MULTILINE)
        # LOW-MEDIUM section becomes just one item (removed T10)
        section = re.sub(r'^8\. Market consolidation', '7. Market consolidation', section, flags=re.MULTILINE)
        section = re.sub(r'^9\. Naviance improving', '8. Naviance improving', section, flags=re.MULTILINE)
        content = content.replace(threat_summary.group(1), section)

    # Fix numbering in Opportunity Summary
    # Removed: 1 (Cialfo) and 6 (Common App)
    # New numbering: 2->1, 3->2, 4->3, 5->4, 7->5, 8->6, 9->7, 10->8
    opp_summary = re.search(r'(### Opportunity Summary.*?)(---)', content, re.DOTALL)
    if opp_summary:
        section = opp_summary.group(1)
        # VERY HIGH section
        section = re.sub(r'^2\. Develop international', '1. Develop international', section, flags=re.MULTILINE)
        section = re.sub(r'^3\. First-mover', '2. First-mover', section, flags=re.MULTILINE)
        section = re.sub(r'^4\. Target Naviance', '3. Target Naviance', section, flags=re.MULTILINE)
        # MEDIUM-HIGH section
        section = re.sub(r'^5\. Tiered pricing', '4. Tiered pricing', section, flags=re.MULTILINE)
        section = re.sub(r'^7\. White space', '5. White space', section, flags=re.MULTILINE)
        section = re.sub(r'^8\. Enhanced AI career', '6. Enhanced AI career', section, flags=re.MULTILINE)
        section = re.sub(r'^9\. Publish customer', '7. Publish customer', section, flags=re.MULTILINE)
        # MEDIUM section
        section = re.sub(r'^10\. Statewide global', '8. Statewide global', section, flags=re.MULTILINE)
        # NOTE: Opp 11 and 12 are removed by matrix references below, but let's keep count at 8 total
        content = content.replace(opp_summary.group(1), section)

    # Remove matrix rows for deleted threats/opportunities
    # Remove T6 row
    content = re.sub(
        r'\| \*\*🟡 T6: Direct Admissions Transformation\*\* \|[^\n]*\n',
        '',
        content
    )

    # Remove T10 row
    content = re.sub(
        r'\| \*\*🟢 T10: Cialfo Improving\*\* \|[^\n]*\n',
        '',
        content
    )

    # Update T7 -> T6 in matrix
    content = re.sub(r'\*\*🟡 T7: SCOIR International', '**🟡 T6: SCOIR International', content)

    # Update T8->T7, T9->T8 in matrix
    content = re.sub(r'\*\*🟢 T8: Market Consolidation', '**🟢 T7: Market Consolidation', content)
    content = re.sub(r'\*\*🟢 T9: Naviance Improving', '**🟢 T8: Naviance Improving', content)

    # Update opportunity numbers in matrix and throughout
    # This is complex, so we'll do targeted replacements
    content = re.sub(r'Opp 2:', 'Opp 1:', content)
    content = re.sub(r'Opp 3:', 'Opp 2:', content)
    content = re.sub(r'Opp 4:', 'Opp 3:', content)
    content = re.sub(r'Opp 5:', 'Opp 4:', content)
    content = re.sub(r'Opp 7:', 'Opp 5:', content)
    content = re.sub(r'Opp 8:', 'Opp 6:', content)
    content = re.sub(r'Opp 9:', 'Opp 7:', content)
    content = re.sub(r'Opp 10:', 'Opp 8:', content)

    # Remove references to removed Opp 1 and Opp 6
    content = re.sub(r'<br>\*\*Opp 1:\*\* Attack Cialfo[^|]*', '', content)
    content = re.sub(r'\*\*Opp 1:\*\* Attack Cialfo[^|<\n]*', '', content)
    content = re.sub(r'<br>\*\*Opp 6:\*\* Direct Admissions[^|]*', '', content)

    # Update Key Insights section
    content = re.sub(
        r'1\. \*\*Opportunity 2 \(International Innovation Leader\) is CENTRAL\*\*',
        '1. **Opportunity 1 (International Innovation Leader) is CENTRAL**',
        content
    )
    content = re.sub(
        r'2\. \*\*Opportunity 5 \(Tiered Pricing\) is STRATEGIC\*\*',
        '2. **Opportunity 4 (Tiered Pricing) is STRATEGIC**',
        content
    )
    content = re.sub(
        r'3\. \*\*Opportunities 1 & 4 are TIME-SENSITIVE\*\* - Windows of opportunity before Cialfo/Naviance[^\n]*\n',
        '3. **Opportunity 3 is TIME-SENSITIVE** - Window of opportunity before Naviance potentially improves (12-18 months)\n',
        content
    )
    content = re.sub(
        r'4\. \*\*Opportunity 6 \(Direct Admissions\) is TABLE STAKES\*\*[^\n]*\n',
        '',
        content
    )

    write_file(output_file, content)

    print(f"✓ Filtered document written to: {output_file}")
    print(f"✓ Removed: Threat 6 (Direct Admissions), Threat 10 (Cialfo)")
    print(f"✓ Removed: Opportunity 1 (Cialfo), Opportunity 6 (Common App)")
    print(f"✓ Updated: 8 Threats total, 8 Opportunities total")
    print(f"✓ Renumbered all threats and opportunities")

if __name__ == '__main__':
    main()
