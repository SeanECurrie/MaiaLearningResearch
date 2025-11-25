#!/bin/bash
# generate-pdfs.sh
# Convert HTML visualizations to PDF using Chrome headless
#
# Usage:
#   ./generate-pdfs.sh                    # Regenerate all PDFs in default directory
#   ./generate-pdfs.sh path/to/file.html  # Regenerate a specific PDF
#   ./generate-pdfs.sh --help             # Show this help
#
# Requirements:
#   - Google Chrome installed at standard location
#   - Write access to output directory

set -e

# Configuration
CHROME_PATH="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
DEFAULT_DIR="05-FINAL-DELIVERABLES/VISUALIZATIONS"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Help function
show_help() {
    echo "generate-pdfs.sh - Convert HTML visualizations to PDF"
    echo ""
    echo "Usage:"
    echo "  ./generate-pdfs.sh                    # Regenerate all PDFs"
    echo "  ./generate-pdfs.sh path/to/file.html  # Regenerate specific file"
    echo "  ./generate-pdfs.sh --help             # Show this help"
    echo ""
    echo "The script uses Chrome headless to render HTML files as PDFs."
    echo "PDFs are saved with the same name in the same directory as the HTML file."
}

# Check Chrome exists
check_chrome() {
    if [ ! -f "$CHROME_PATH" ]; then
        echo -e "${RED}Error: Chrome not found at $CHROME_PATH${NC}"
        echo "Please install Google Chrome or update CHROME_PATH in this script."
        exit 1
    fi
}

# Convert single HTML to PDF
convert_file() {
    local html_file="$1"
    local pdf_file="${html_file%.html}.pdf"

    if [ ! -f "$html_file" ]; then
        echo -e "${RED}Error: File not found: $html_file${NC}"
        return 1
    fi

    echo -n "Converting $(basename "$html_file")... "

    "$CHROME_PATH" \
        --headless \
        --disable-gpu \
        --print-to-pdf="$pdf_file" \
        "file://$html_file" \
        2>/dev/null

    if [ -f "$pdf_file" ]; then
        echo -e "${GREEN}OK${NC}"
        return 0
    else
        echo -e "${RED}FAILED${NC}"
        return 1
    fi
}

# Convert all HTML files in directory
convert_all() {
    local target_dir="${1:-$PROJECT_ROOT/$DEFAULT_DIR}"
    local success_count=0
    local fail_count=0

    if [ ! -d "$target_dir" ]; then
        echo -e "${RED}Error: Directory not found: $target_dir${NC}"
        exit 1
    fi

    echo "Converting HTML files in: $target_dir"
    echo "---"

    # Find all HTML files
    while IFS= read -r -d '' html_file; do
        if convert_file "$html_file"; then
            ((success_count++))
        else
            ((fail_count++))
        fi
    done < <(find "$target_dir" -name "*.html" -type f -print0)

    echo "---"
    echo -e "Complete: ${GREEN}$success_count succeeded${NC}, ${RED}$fail_count failed${NC}"

    if [ $fail_count -gt 0 ]; then
        exit 1
    fi
}

# Main
main() {
    case "${1:-}" in
        --help|-h)
            show_help
            exit 0
            ;;
        "")
            check_chrome
            convert_all
            ;;
        *)
            check_chrome
            # If argument is a file, convert it
            if [ -f "$1" ]; then
                convert_file "$(realpath "$1")"
            # If argument is a directory, convert all in it
            elif [ -d "$1" ]; then
                convert_all "$(realpath "$1")"
            else
                echo -e "${RED}Error: Not a file or directory: $1${NC}"
                exit 1
            fi
            ;;
    esac
}

main "$@"
