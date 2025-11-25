#!/usr/bin/env python3
"""
verify-consistency.py
Check that a value appears consistently across documents.
Report only - never modifies files.

Usage:
    python verify-consistency.py --search "TERM" --path DIR
    python verify-consistency.py --search "TERM" --expected 15 --path DIR
    python verify-consistency.py --search "TERM" --path DIR --list

Options:
    --search    Text or pattern to search for (required)
    --path      Directory to search (required)
    --expected  Expected occurrence count (optional - exits with error if mismatch)
    --list      List all occurrences with file and line number
    --include   File patterns to include, comma-separated (e.g., "*.md,*.html")
    --exclude   File patterns to exclude, comma-separated (e.g., "*.pdf,*.docx")
    --help      Show this help message

Exit codes:
    0 - Success (count matches expected, or no expected specified)
    1 - Failure (count does not match expected)
    2 - Error (invalid arguments, directory not found, etc.)

Note: This script only reports findings. It never modifies files.
"""

import argparse
import fnmatch
import os
import re
import sys
from collections import defaultdict
from pathlib import Path

# Binary file extensions to skip
BINARY_EXTENSIONS = {
    '.pdf', '.docx', '.xlsx', '.pptx', '.doc', '.xls', '.ppt',
    '.png', '.jpg', '.jpeg', '.gif', '.bmp', '.ico', '.svg',
    '.zip', '.tar', '.gz', '.rar', '.7z',
    '.exe', '.dll', '.so', '.dylib',
    '.mp3', '.mp4', '.wav', '.avi', '.mov',
    '.ttf', '.otf', '.woff', '.woff2',
    '.pyc', '.pyo', '.class',
}

def is_binary_file(filepath):
    """Check if file is binary based on extension."""
    return Path(filepath).suffix.lower() in BINARY_EXTENSIONS

def matches_patterns(filename, patterns):
    """Check if filename matches any of the glob patterns."""
    if not patterns:
        return True
    return any(fnmatch.fnmatch(filename, p.strip()) for p in patterns.split(','))

def find_files(directory, include=None, exclude=None):
    """Find all text files in directory, respecting include/exclude patterns."""
    files = []
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(root, filename)

            # Skip binary files
            if is_binary_file(filepath):
                continue

            # Check include patterns
            if include and not matches_patterns(filename, include):
                continue

            # Check exclude patterns
            if exclude and matches_patterns(filename, exclude):
                continue

            files.append(filepath)

    return sorted(files)

def search_file(filepath, search_term):
    """Search for term in file. Returns list of (line_num, line_content, count_in_line)."""
    results = []
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            for line_num, line in enumerate(f, 1):
                count = line.count(search_term)
                if count > 0:
                    results.append((line_num, line.rstrip(), count))
    except Exception as e:
        print(f"Warning: Could not read {filepath}: {e}", file=sys.stderr)
    return results

def run_search(files, search_term, show_list=False):
    """Search all files and return results."""
    results_by_file = defaultdict(list)
    total_count = 0

    for filepath in files:
        file_results = search_file(filepath, search_term)
        if file_results:
            results_by_file[filepath] = file_results
            for _, _, count in file_results:
                total_count += count

    return results_by_file, total_count

def print_report(results_by_file, total_count, search_term, expected=None, show_list=False):
    """Print the verification report."""
    print("=" * 60)
    print("CONSISTENCY CHECK REPORT")
    print("=" * 60)
    print(f"Search term: '{search_term}'")
    print(f"Files searched: {len(results_by_file)} contain matches")
    print(f"Total occurrences: {total_count}")

    if expected is not None:
        if total_count == expected:
            print(f"Expected: {expected} ✓ MATCH")
        else:
            print(f"Expected: {expected} ✗ MISMATCH (found {total_count})")

    print("-" * 60)

    # Summary by file
    print("\nFiles containing matches:")
    for filepath, results in sorted(results_by_file.items()):
        file_count = sum(count for _, _, count in results)
        relative_path = filepath
        print(f"  {relative_path}: {file_count} occurrence(s)")

    # Detailed list if requested
    if show_list and results_by_file:
        print("\n" + "-" * 60)
        print("Detailed occurrences:")
        for filepath, results in sorted(results_by_file.items()):
            print(f"\n{filepath}:")
            for line_num, line, count in results:
                # Truncate long lines
                display_line = line[:80] + "..." if len(line) > 80 else line
                print(f"  Line {line_num}: {display_line}")

    print("\n" + "=" * 60)

    # Final status
    if expected is not None:
        if total_count == expected:
            print("Status: PASS - Count matches expected value")
            return True
        else:
            print(f"Status: FAIL - Expected {expected}, found {total_count}")
            return False
    else:
        print(f"Status: Found {total_count} occurrences")
        return True

def main():
    parser = argparse.ArgumentParser(
        description='Check that a value appears consistently across documents.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument('--search', required=True, help='Text to search for')
    parser.add_argument('--path', required=True, help='Directory to search')
    parser.add_argument('--expected', type=int, help='Expected occurrence count')
    parser.add_argument('--list', action='store_true', dest='show_list', help='List all occurrences')
    parser.add_argument('--include', help='File patterns to include (comma-separated)')
    parser.add_argument('--exclude', help='File patterns to exclude (comma-separated)')

    args = parser.parse_args()

    # Validate path
    if not os.path.isdir(args.path):
        print(f"Error: Directory not found: {args.path}", file=sys.stderr)
        sys.exit(2)

    # Find files
    files = find_files(args.path, args.include, args.exclude)

    if not files:
        print("No files found matching criteria.")
        if args.expected is not None and args.expected != 0:
            print(f"Expected {args.expected} occurrences, found 0")
            sys.exit(1)
        sys.exit(0)

    # Run search
    results_by_file, total_count = run_search(files, args.search, args.show_list)

    # Print report
    passed = print_report(results_by_file, total_count, args.search, args.expected, args.show_list)

    # Exit code
    if args.expected is not None and not passed:
        sys.exit(1)
    sys.exit(0)

if __name__ == '__main__':
    main()
