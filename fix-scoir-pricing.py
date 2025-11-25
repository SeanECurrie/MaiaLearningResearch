#!/usr/bin/env python3
"""Fix SCOIR pricing errors in Word documents"""
import zipfile
import os
import shutil
from pathlib import Path

files = [
    "/Users/seancurrie/Desktop/MaiaLearningResearch/05-FINAL-DELIVERABLES/COMPARATIVE-ANALYSIS-TOP4/target-segments-top4.docx",
    "/Users/seancurrie/Desktop/MaiaLearningResearch/05-FINAL-DELIVERABLES/COMPARATIVE-ANALYSIS-TOP4/pricing-analysis-top4.docx"
]

for docx_path in files:
    filename = Path(docx_path).name
    print(f"\n{'='*60}")
    print(f"Processing: {filename}")
    print(f"{'='*60}")

    temp_dir = f"/Users/seancurrie/Desktop/MaiaLearningResearch/temp-{filename}-unpacked"

    try:
        # Extract docx
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
        os.makedirs(temp_dir)

        with zipfile.ZipFile(docx_path, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)

        # Read document.xml
        doc_xml_path = os.path.join(temp_dir, 'word', 'document.xml')
        with open(doc_xml_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Search for errors
        error_count = content.count('$4.80-6')
        print(f"\nFound {error_count} instances of '$4.80-6' pricing error")

        if error_count > 0:
            # Fix errors
            fixed_content = content.replace('$4.80-6', '$4.80')

            # Write back
            with open(doc_xml_path, 'w', encoding='utf-8') as f:
                f.write(fixed_content)

            # Repack docx
            backup_path = docx_path.replace('.docx', '-BACKUP.docx')
            shutil.copy2(docx_path, backup_path)
            print(f"✓ Created backup: {Path(backup_path).name}")

            with zipfile.ZipFile(docx_path, 'w', zipfile.ZIP_DEFLATED) as zip_ref:
                for root, dirs, files in os.walk(temp_dir):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, temp_dir)
                        zip_ref.write(file_path, arcname)

            print(f"✓ Fixed {error_count} instances of '$4.80-6' → '$4.80'")

            # Verify
            with zipfile.ZipFile(docx_path, 'r') as zip_ref:
                verify_content = zip_ref.read('word/document.xml').decode('utf-8')
                remaining = verify_content.count('$4.80-6')
                print(f"✓ Verification: {remaining} instances remaining (should be 0)")
        else:
            print("✓ No pricing errors found - document is clean")

        # Cleanup
        shutil.rmtree(temp_dir)

    except Exception as e:
        print(f"✗ Error: {e}")
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)

print(f"\n{'='*60}")
print("✓ QA Complete")
print(f"{'='*60}\n")
