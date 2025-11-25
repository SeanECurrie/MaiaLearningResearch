#!/usr/bin/env python3
"""
Properly replace <style> sections with enterprise-styles.css link.
"""

import re

FILES = [
    'competitive-positioning-viz.html',
    'strategic-recommendations-viz.html',
    'threats-opportunities-viz.html',
    'pricing-analysis-top4-viz.html',
    'target-segments-top4-viz.html',
    'market-positioning-top4-viz.html',
    'technology-stack-top4-viz.html',
    'feature-comparison-matrix-top4-viz.html',
]

MINIMAL_ENTERPRISE_STYLES = '''    <link rel="stylesheet" href="enterprise-styles.css">
    <style>
        /* Minimal file-specific overrides only */
    </style>'''

for filepath in FILES:
    print(f"Processing: {filepath}")

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace the entire <style>...</style> section
    content = re.sub(
        r'<style>.*?</style>',
        MINIMAL_ENTERPRISE_STYLES,
        content,
        flags=re.DOTALL
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"  ✓ Replaced style section in {filepath}")

print("\n✓ All style sections replaced with enterprise-styles.css")
