#!/usr/bin/env python3
"""Search for SCOIR pricing errors in Word documents"""
import zipfile
import xml.etree.ElementTree as ET

files = [
    "/Users/seancurrie/Desktop/MaiaLearningResearch/05-FINAL-DELIVERABLES/COMPARATIVE-ANALYSIS-TOP4/target-segments-top4.docx",
    "/Users/seancurrie/Desktop/MaiaLearningResearch/05-FINAL-DELIVERABLES/COMPARATIVE-ANALYSIS-TOP4/pricing-analysis-top4.docx"
]

for docx_file in files:
    print(f"\n=== Checking: {docx_file.split('/')[-1]} ===")
    try:
        with zipfile.ZipFile(docx_file, 'r') as zip_ref:
            xml_content = zip_ref.read('word/document.xml').decode('utf-8')

            # Search for pricing patterns
            if '$4.80-6' in xml_content:
                print(f"  ❌ FOUND: $4.80-6 pricing error")
                count = xml_content.count('$4.80-6')
                print(f"  Count: {count} instance(s)")
            elif '$5-6' in xml_content and 'SCOIR' in xml_content:
                # Check if SCOIR and $5-6 appear together
                print(f"  ⚠️  Found $5-6 and SCOIR in document - needs manual verification")
            else:
                print(f"  ✓ No obvious SCOIR pricing errors found")

    except Exception as e:
        print(f"  Error reading file: {e}")

print("\n✓ Search complete")
