#!/usr/bin/env python3
"""
bulk-replace.py
Find and replace text across multiple files safely.

Usage:
    python bulk-replace.py --old "OLD_TEXT" --new "NEW_TEXT" --path DIR --dry-run
    python bulk-replace.py --old "OLD_TEXT" --new "NEW_TEXT" --path DIR

Options:
    --old       Text to find (required)
    --new       Replacement text (required)
    --path      Directory to search (required)
    --dry-run   Preview changes without modifying files (recommended first)
    --include   File patterns to include, comma-separated (e.g., "*.md,*.html")
    --exclude   File patterns to exclude, comma-separated (e.g., "*.pdf,*.docx")
    --backup    Create .bak backup of modified files
    --help      Show this help message

Safety:
    - Always run with --dry-run first to preview changes
    - Binary files (PDF, DOCX, images) are never modified
    - Use --backup to create backups before modifying
"""

import argparse
import fnmatch
import os
import shutil
import sys
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

def find_occurrences(filepath, old_text):
    """Find all occurrences of old_text in file. Returns list of (line_num, line_content)."""
    occurrences = []
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            for line_num, line in enumerate(f, 1):
                if old_text in line:
                    occurrences.append((line_num, line.rstrip()))
    except Exception as e:
        print(f"Warning: Could not read {filepath}: {e}", file=sys.stderr)
    return occurrences

def replace_in_file(filepath, old_text, new_text, backup=False):
    """Replace old_text with new_text in file. Returns number of replacements made."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        count = content.count(old_text)
        if count == 0:
            return 0

        new_content = content.replace(old_text, new_text)

        if backup:
            shutil.copy2(filepath, filepath + '.bak')

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

        return count
    except Exception as e:
        print(f"Error: Could not process {filepath}: {e}", file=sys.stderr)
        return 0

def dry_run(files, old_text, new_text):
    """Preview changes without modifying files."""
    total_files = 0
    total_occurrences = 0

    print("=" * 60)
    print("DRY RUN - No files will be modified")
    print("=" * 60)
    print(f"Finding: '{old_text}'")
    print(f"Replace: '{new_text}'")
    print("-" * 60)

    for filepath in files:
        occurrences = find_occurrences(filepath, old_text)
        if occurrences:
            total_files += 1
            total_occurrences += len(occurrences)
            print(f"\n{filepath}:")
            for line_num, line in occurrences:
                # Highlight the match
                highlighted = line.replace(old_text, f">>>{old_text}<<<")
                print(f"  Line {line_num}: {highlighted[:100]}...")

    print("\n" + "=" * 60)
    print(f"Summary: {total_occurrences} occurrences in {total_files} files")
    print("=" * 60)

    if total_occurrences > 0:
        print("\nTo apply these changes, run again without --dry-run")
    else:
        print("\nNo occurrences found. Nothing to replace.")

    return total_files, total_occurrences

def apply_changes(files, old_text, new_text, backup=False):
    """Apply replacements to files."""
    total_files = 0
    total_occurrences = 0

    print("=" * 60)
    print("APPLYING CHANGES")
    print("=" * 60)
    print(f"Finding: '{old_text}'")
    print(f"Replace: '{new_text}'")
    if backup:
        print("Backup: Enabled (.bak files will be created)")
    print("-" * 60)

    for filepath in files:
        count = replace_in_file(filepath, old_text, new_text, backup)
        if count > 0:
            total_files += 1
            total_occurrences += count
            print(f"  {filepath}: {count} replacement(s)")

    print("\n" + "=" * 60)
    print(f"Complete: {total_occurrences} replacements in {total_files} files")
    print("=" * 60)

    return total_files, total_occurrences

def main():
    parser = argparse.ArgumentParser(
        description='Find and replace text across multiple files safely.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument('--old', required=True, help='Text to find')
    parser.add_argument('--new', required=True, help='Replacement text')
    parser.add_argument('--path', required=True, help='Directory to search')
    parser.add_argument('--dry-run', action='store_true', help='Preview changes only')
    parser.add_argument('--include', help='File patterns to include (comma-separated)')
    parser.add_argument('--exclude', help='File patterns to exclude (comma-separated)')
    parser.add_argument('--backup', action='store_true', help='Create .bak backup files')

    args = parser.parse_args()

    # Validate path
    if not os.path.isdir(args.path):
        print(f"Error: Directory not found: {args.path}", file=sys.stderr)
        sys.exit(1)

    # Validate old != new
    if args.old == args.new:
        print("Error: --old and --new cannot be the same", file=sys.stderr)
        sys.exit(1)

    # Find files
    files = find_files(args.path, args.include, args.exclude)

    if not files:
        print("No files found matching criteria.")
        sys.exit(0)

    # Run
    if args.dry_run:
        total_files, total_occurrences = dry_run(files, args.old, args.new)
    else:
        # Confirm before applying
        print(f"About to search {len(files)} files in {args.path}")
        print(f"Replace: '{args.old}' -> '{args.new}'")
        response = input("Continue? [y/N]: ")
        if response.lower() != 'y':
            print("Aborted.")
            sys.exit(0)

        total_files, total_occurrences = apply_changes(files, args.old, args.new, args.backup)

    # Exit code: 0 if changes made/found, 1 if nothing found
    sys.exit(0 if total_occurrences > 0 else 1)

if __name__ == '__main__':
    main()
