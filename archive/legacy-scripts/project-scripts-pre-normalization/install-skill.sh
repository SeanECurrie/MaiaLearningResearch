#!/bin/bash

# Competitive Research Skill Installation Script
# This script installs the competitive-research-brightdata skill to your personal Claude CLI skills directory

set -e

echo "========================================="
echo "Competitive Research Skill Installer"
echo "========================================="
echo ""

# Check if .skill file exists
SKILL_FILE="competitive-research-brightdata.skill"
if [ ! -f "$SKILL_FILE" ]; then
    echo "❌ Error: $SKILL_FILE not found in current directory"
    echo "   Please run this script from the project root: bash scripts/install-skill.sh"
    exit 1
fi

# Create skills directory if it doesn't exist
SKILLS_DIR="$HOME/.claude/skills"
echo "📁 Creating skills directory: $SKILLS_DIR"
mkdir -p "$SKILLS_DIR"

# Check if skill is already installed
SKILL_DIR="$SKILLS_DIR/competitive-research-brightdata"
if [ -d "$SKILL_DIR" ]; then
    echo "⚠️  Skill already installed at: $SKILL_DIR"
    read -p "   Overwrite existing installation? (y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "❌ Installation cancelled"
        exit 0
    fi
    echo "🗑️  Removing existing installation..."
    rm -rf "$SKILL_DIR"
fi

# Extract skill
echo "📦 Extracting skill to: $SKILL_DIR"
unzip -q "$SKILL_FILE" -d "$SKILLS_DIR"

# Verify installation
if [ -f "$SKILL_DIR/SKILL.md" ]; then
    echo ""
    echo "✅ Skill installed successfully!"
    echo ""
    echo "📂 Installed to: $SKILL_DIR"
    echo "📄 Files:"
    find "$SKILL_DIR" -type f | sed 's|^|   - |'
    echo ""
    echo "⚠️  IMPORTANT: Restart Claude CLI to activate the skill"
    echo ""
    echo "🎯 The skill will automatically activate when you ask Claude to:"
    echo "   • Research companies"
    echo "   • Conduct competitive analysis"
    echo "   • Create market reports"
    echo "   • Compare products/services"
    echo "   • Analyze industries"
    echo ""
    echo "========================================="
else
    echo "❌ Error: Installation failed - SKILL.md not found"
    exit 1
fi
