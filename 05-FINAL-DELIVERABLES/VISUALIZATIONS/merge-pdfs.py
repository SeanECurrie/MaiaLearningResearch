#!/usr/bin/env python3
"""
Merge all ENTERPRISE PDFs into a single optimized combined PDF
"""

import os
from PyPDF2 import PdfMerger

def merge_enterprise_pdfs():
    """Merge all ENTERPRISE PDFs in the correct order"""

    # Define the order of PDFs for the combined document
    pdf_files = [
        "swot-analysis-viz-ENTERPRISE.pdf",
        "competitive-positioning-viz-ENTERPRISE.pdf",
        "market-positioning-top4-viz-ENTERPRISE.pdf",
        "feature-comparison-matrix-top4-viz-ENTERPRISE.pdf",
        "technology-stack-top4-viz-ENTERPRISE.pdf",
        "pricing-analysis-top4-viz-ENTERPRISE.pdf",
        "target-segments-top4-viz-ENTERPRISE.pdf",
        "market-trends-viz-ENTERPRISE.pdf",
        "strategic-recommendations-viz-ENTERPRISE.pdf",
        "threats-opportunities-viz-ENTERPRISE.pdf"
    ]

    merger = PdfMerger()

    print("=" * 60)
    print("Merging ENTERPRISE PDFs")
    print("=" * 60)
    print()

    for pdf_file in pdf_files:
        if os.path.exists(pdf_file):
            file_size = os.path.getsize(pdf_file) / 1024  # KB
            print(f"Adding: {pdf_file} ({file_size:.1f} KB)")
            merger.append(pdf_file)
        else:
            print(f"WARNING: {pdf_file} not found, skipping")

    output_file = "Combined-Competitive-Analysis-Visualizations-ENTERPRISE.pdf"

    print()
    print("Writing combined PDF...")
    merger.write(output_file)
    merger.close()

    output_size = os.path.getsize(output_file) / (1024 * 1024)  # MB
    print()
    print("=" * 60)
    print(f"✓ SUCCESS: {output_file}")
    print(f"  Size: {output_size:.2f} MB")
    print("=" * 60)

if __name__ == "__main__":
    merge_enterprise_pdfs()
