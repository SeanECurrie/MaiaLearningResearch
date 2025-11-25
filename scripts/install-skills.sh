#!/bin/bash
# install-skills.sh - Sync skill definitions from repo to ~/.claude/skills/
#
# Usage: ./install-skills.sh [--dry-run] [--backup]
#
# Options:
#   --dry-run   Show what would be done without making changes
#   --backup    Create timestamped backups before overwriting
#
# This script copies skill definitions from skills/local/ to ~/.claude/skills/
# The repo is the source of truth; this script pushes changes to the active location.

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"
SKILLS_SOURCE="$REPO_ROOT/skills/local"
SKILLS_TARGET="$HOME/.claude/skills"

DRY_RUN=false
BACKUP=false

# Parse arguments
for arg in "$@"; do
    case $arg in
        --dry-run)
            DRY_RUN=true
            ;;
        --backup)
            BACKUP=true
            ;;
        *)
            echo "Unknown option: $arg"
            echo "Usage: ./install-skills.sh [--dry-run] [--backup]"
            exit 1
            ;;
    esac
done

echo "=== Skill Installation Script ==="
echo "Source: $SKILLS_SOURCE"
echo "Target: $SKILLS_TARGET"
echo "Dry run: $DRY_RUN"
echo "Backup: $BACKUP"
echo ""

# Check source exists
if [ ! -d "$SKILLS_SOURCE" ]; then
    echo "ERROR: Source directory not found: $SKILLS_SOURCE"
    exit 1
fi

# Create target if needed
if [ ! -d "$SKILLS_TARGET" ]; then
    if [ "$DRY_RUN" = true ]; then
        echo "[DRY RUN] Would create: $SKILLS_TARGET"
    else
        mkdir -p "$SKILLS_TARGET"
        echo "Created: $SKILLS_TARGET"
    fi
fi

# Process each skill
for skill_dir in "$SKILLS_SOURCE"/*/; do
    skill_name=$(basename "$skill_dir")
    source_file="$skill_dir/SKILL.md"
    target_dir="$SKILLS_TARGET/$skill_name"
    target_file="$target_dir/SKILL.md"

    if [ ! -f "$source_file" ]; then
        echo "SKIP: No SKILL.md found in $skill_dir"
        continue
    fi

    echo "Processing: $skill_name"

    # Backup if requested and target exists
    if [ "$BACKUP" = true ] && [ -f "$target_file" ]; then
        backup_file="${target_file}.backup.$(date +%Y%m%d-%H%M%S)"
        if [ "$DRY_RUN" = true ]; then
            echo "  [DRY RUN] Would backup: $target_file -> $backup_file"
        else
            cp "$target_file" "$backup_file"
            echo "  Backed up: $backup_file"
        fi
    fi

    # Create target directory if needed
    if [ ! -d "$target_dir" ]; then
        if [ "$DRY_RUN" = true ]; then
            echo "  [DRY RUN] Would create directory: $target_dir"
        else
            mkdir -p "$target_dir"
            echo "  Created directory: $target_dir"
        fi
    fi

    # Copy skill file
    if [ "$DRY_RUN" = true ]; then
        echo "  [DRY RUN] Would copy: $source_file -> $target_file"
    else
        cp "$source_file" "$target_file"
        echo "  Installed: $target_file"
    fi
done

echo ""
echo "=== Installation Complete ==="

# Verification
echo ""
echo "Verification:"
for skill_dir in "$SKILLS_SOURCE"/*/; do
    skill_name=$(basename "$skill_dir")
    target_file="$SKILLS_TARGET/$skill_name/SKILL.md"
    if [ -f "$target_file" ]; then
        echo "  OK $skill_name installed"
    else
        echo "  MISSING $skill_name NOT installed"
    fi
done
