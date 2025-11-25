#!/usr/bin/env python3
"""
Batch refactor visualization HTML files to enterprise grayscale standards.
Removes emojis, colorful backgrounds, gradients, and applies conservative styling.
"""

import re
import os

# Emoji replacements
EMOJI_REPLACEMENTS = {
    '🔴 CRITICAL': 'CRITICAL',
    '🔴 Very High': 'VERY HIGH',
    '🟡 MEDIUM-HIGH': 'MEDIUM-HIGH',
    '🟡 Medium-High': 'MEDIUM-HIGH',
    '🟡 MEDIUM': 'MEDIUM',
    '🟡 Medium': 'MEDIUM',
    '🟡 HIGH': 'HIGH',
    '🟡 MED-HIGH': 'MED-HIGH',
    '🟢 MEDIUM': 'MEDIUM',
    '🟢 LOW-MED': 'LOW-MED',
    '⭐⭐⭐⭐⭐ High': 'HIGH (5/5)',
    '⭐⭐⭐⭐': 'VERY HIGH (4/5)',
    '⭐⭐⭐ Moderate': 'MODERATE (3/5)',
    '⭐⭐ Low': 'LOW (2/5)',
    '⭐ Very Low': 'VERY LOW (1/5)',
    '⭐ Maia Learning': 'Maia Learning',
    '⭐': '',
    '🔴 Tier 1:': 'TIER 1 (CRITICAL):',
    '🟡 Tier 2:': 'TIER 2 (HIGH PRIORITY):',
    '🟢 Tier 3:': 'TIER 3 (EMERGING):',
    '🔴 URGENT': 'URGENT',
    '🟡 HIGH PRIORITY': 'HIGH PRIORITY',
    '🟢 MEDIUM PRIORITY': 'MEDIUM PRIORITY',
    '🔴': '',
    '🟡': '',
    '🟢': '',
}

# Color pattern replacements
COLOR_PATTERNS = [
    (r'background:\s*linear-gradient\([^)]+\)', 'background: #333333'),
    (r'background:\s*#[0-9a-f]{6}(?![^<]*white)', 'background: #f5f5f5'),
    (r'border-bottom:\s*3px\s+solid\s+#3498db', 'border-bottom: 2px solid #000000'),
    (r'border-bottom:\s*2px\s+solid\s+#3498db', 'border-bottom: 2px solid #000000'),
    (r'border-left:\s*[45]px\s+solid\s+#[0-9a-f]{6}', 'border-left: 3px solid #000000'),
    (r'color:\s*#3498db', 'color: #000000'),
    (r'color:\s*#2c3e50', 'color: #333333'),
    (r'color:\s*#34495e', 'color: #333333'),
    (r'color:\s*#7f8c8d', 'color: #666666'),
]

def refactor_html_file(filepath):
    """Refactor a single HTML file to enterprise standards."""
    print(f"Refactoring: {filepath}")

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Replace emojis
    for emoji, replacement in EMOJI_REPLACEMENTS.items():
        content = content.replace(emoji, replacement)

    # Replace color patterns
    for pattern, replacement in COLOR_PATTERNS:
        content = re.sub(pattern, replacement, content)

    # Replace <style> section with enterprise-styles.css link
    if '<link rel="stylesheet" href="enterprise-styles.css">' not in content:
        # Find the style section
        style_match = re.search(r'(<style>.*?</style>)', content, re.DOTALL)
        if style_match:
            old_style = style_match.group(1)
            # Keep only file-specific styles that don't conflict with enterprise-styles.css
            new_style = '<link rel="stylesheet" href="enterprise-styles.css">'
            content = content.replace(old_style, new_style, 1)

    # Remove colored row backgrounds
    content = re.sub(r'class="priority-critical"', 'class=""', content)
    content = re.sub(r'class="priority-high"', 'class=""', content)
    content = re.sub(r'class="priority-medium"', 'class=""', content)

    # Write refactored content
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✓ Refactored {filepath}")
        return True
    else:
        print(f"  - No changes needed for {filepath}")
        return False

def main():
    """Main execution function."""
    viz_dir = '/Users/seancurrie/Desktop/MaiaLearningResearch/05-FINAL-DELIVERABLES/VISUALIZATIONS'
    os.chdir(viz_dir)

    files_to_refactor = [
        'market-trends-viz.html',
        'competitive-positioning-viz.html',
        'strategic-recommendations-viz.html',
        'threats-opportunities-viz.html',
        'pricing-analysis-top4-viz.html',
        'target-segments-top4-viz.html',
        'market-positioning-top4-viz.html',
        'technology-stack-top4-viz.html',
        'feature-comparison-matrix-top4-viz.html',
    ]

    refactored_count = 0
    for filename in files_to_refactor:
        if os.path.exists(filename):
            if refactor_html_file(filename):
                refactored_count += 1
        else:
            print(f"  ✗ File not found: {filename}")

    print(f"\n✓ Refactored {refactored_count} files to enterprise standards")
    print("✓ All emojis removed")
    print("✓ Colorful backgrounds converted to grayscale")
    print("✓ Gradients replaced with solid colors")

if __name__ == '__main__':
    main()
