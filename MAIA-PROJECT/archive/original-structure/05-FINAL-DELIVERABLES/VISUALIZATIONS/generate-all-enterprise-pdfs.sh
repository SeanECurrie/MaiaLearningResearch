#!/bin/bash
# Batch generate all enterprise PDFs from refactored HTML files

CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
VIZ_DIR="/Users/seancurrie/Desktop/MaiaLearningResearch/05-FINAL-DELIVERABLES/VISUALIZATIONS"

cd "$VIZ_DIR"

FILES=(
    "swot-analysis-viz"
    "competitive-positioning-viz"
    "market-trends-viz"
    "strategic-recommendations-viz"
    "threats-opportunities-viz"
    "pricing-analysis-top4-viz"
    "target-segments-top4-viz"
    "market-positioning-top4-viz"
    "technology-stack-top4-viz"
    "feature-comparison-matrix-top4-viz"
)

echo "=========================================="
echo "Generating Enterprise PDFs"
echo "=========================================="
echo ""

for file in "${FILES[@]}"; do
    echo "Processing: ${file}.html"
    "$CHROME" \
        --headless \
        --disable-gpu \
        --print-to-pdf="${VIZ_DIR}/${file}-ENTERPRISE.pdf" \
        "file://${VIZ_DIR}/${file}.html" 2>/dev/null

    if [ -f "${file}-ENTERPRISE.pdf" ]; then
        echo "  ✓ Generated: ${file}-ENTERPRISE.pdf"
    else
        echo "  ✗ FAILED: ${file}-ENTERPRISE.pdf"
    fi
done

echo ""
echo "=========================================="
echo "PDF Generation Complete"
echo "=========================================="
echo ""
ls -lh *-ENTERPRISE.pdf 2>/dev/null | wc -l | xargs echo "Total PDFs generated:"
