# GitHub Copilot Instructions for CHILI GraFx Documentation

This document provides guidelines for GitHub Copilot when working with the CHILI GraFx documentation repository.

## Project Overview

This is a technical documentation site for CHILI GraFx products, built with MkDocs Material. The documentation covers multiple GraFx applications including Studio, Publisher, Media, Fonts, Brand Kits, and Developer resources.

## Language & Style Guidelines

### Language
- **Primary Language**: English (US)
- **Tone**: Professional, clear, and user-friendly
- **Audience**: Technical users, developers, designers, and administrators

### Spelling & Grammar
- Use American English spelling (e.g., "color" not "colour", "center" not "centre")
- Check for common typos and grammatical errors
- Ensure consistent terminology throughout

## Content Quality Standards

### Terminology Consistency
- **CHILI GraFx** (with capital "F" in "GraFx")
- **GraFx Studio** (not "GraFX Studio" or "Grafx Studio")
- **GraFx Publisher** (not "GraFX Publisher" or "Grafx Publisher")
- **GraFx Media** (not "GraFX Media" or "Grafx Media")
- **GraFx Fonts** (not "GraFX Fonts" or "Grafx Fonts")
- **GraFx Brand Kits** (not "GraFX Brand Kits" or "Grafx Brand Kits")
- **Smart Templates** (capitalized)
- **Template Designer** (capitalized)
- **End-users** (with hyphen)

### Technical Terms
- Use "multichannel" (not "multi-channel")
- Use "self-service" (with hyphen)
- Use "real-time" (with hyphen)
- Use "end-to-end" (with hyphens)
- Use "plug-and-play" (with hyphens)

### Product Names
- Always use the exact product names as specified
- Include version numbers when relevant (e.g., "v1.27")
- Use proper trademark symbols when appropriate

## File Structure & Organization

### Directory Naming
- Use kebab-case for directory names (e.g., `grafx-studio`, `brand-kits`)
- Follow the established hierarchy: `docs/[Product-Name]/[section]/[subsection]/index.md`

### File Naming
- All documentation files should be named `index.md`
- Use descriptive directory names to indicate content
- Maintain consistent folder structure across products

## Markdown Standards

### Headers
- Use `#` for main page titles
- Use `##` for major sections
- Use `###` for subsections
- Maintain proper header hierarchy (no skipping levels)

### Links
- Use relative paths for internal links
- Include `.md` extension for markdown files in links
- Use descriptive link text
- Ensure all links are functional

### Images
- Use descriptive alt text for all images
- Place images in appropriate `assets/` directories
- Use consistent image naming conventions
- Include proper image sizing attributes when needed

### Code Blocks
- Use appropriate language identifiers for syntax highlighting
- Include comments explaining complex code
- Ensure code examples are complete and functional

## Content Patterns

### Release Notes
- Follow the established format with frontmatter
- Include proper categorization (`Releases`, `Operational updates`)
- Use consistent emoji patterns (✨ for new features, 🛠️ for improvements, 🐛 for fixes)
- Include relevant screenshots and links to documentation

### Guide Structure
- Start with clear objectives
- Provide step-by-step instructions
- Include screenshots where helpful
- End with next steps or related resources

### Concept Pages
- Define terms clearly
- Provide context and use cases
- Include examples where appropriate
- Link to related concepts and guides

## Quality Checks

### Before Committing
1. **Spelling**: Run spell check on all content
2. **Links**: Verify all internal and external links work
3. **Images**: Ensure all images load and have proper alt text
4. **Consistency**: Check terminology consistency across the document
5. **Structure**: Verify proper markdown formatting and hierarchy

### Content Review
- Ensure all product names are spelled correctly
- Check for consistent use of technical terms
- Verify all code examples are syntactically correct
- Confirm all screenshots are current and relevant

## Common Issues to Watch For

### Spelling Mistakes
- "GraFX" → "GraFx"
- "Grafx" → "GraFx"
- "colour" → "color"
- "centre" → "center"
- "realise" → "realize"
- "organise" → "organize"

### Formatting Issues
- Inconsistent header levels
- Missing image alt text
- Broken internal links
- Inconsistent bullet point formatting
- Missing frontmatter in release notes

### Content Issues
- Outdated screenshots
- Broken code examples
- Inconsistent terminology
- Missing context or explanations
- Unclear instructions

## MkDocs Specific Guidelines

### Navigation
- Ensure all pages are properly included in `mkdocs.yml`
- Use consistent indentation in navigation structure
- Verify page titles match navigation labels

### Plugins
- Be aware of the blog plugin for release notes
- Understand the redirects plugin for moved content
- Consider RSS feed implications for new content

### Material Theme
- Use appropriate Material Design icons
- Follow the established color scheme
- Maintain consistent card layouts for overview pages

## Best Practices

1. **Always test locally** before committing changes
2. **Use descriptive commit messages** that explain what was changed
3. **Keep screenshots current** and relevant to the content
4. **Provide context** for technical concepts
5. **Include examples** where they add value
6. **Link to related content** to help users navigate
7. **Use consistent formatting** across all documentation

## Resources

- [MkDocs Material Documentation](https://squidfunk.github.io/mkdocs-material/)
- [CHILI GraFx Documentation Site](https://docs.chiligrafx.com/)
- [CHILI publish Website](https://www.chili-publish.com/)

---

*This file should be updated as the documentation standards evolve and new patterns emerge.*
