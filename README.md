# Content Management Skill

> Unified content platform for AI agents — articles, social media, YouTube, media library, SEO, and publishing workflows via mcp-cms (26 tools).

[![Skill Standard](https://img.shields.io/badge/standard-agentskills.io-blue)](https://agentskills.io)
[![MCP Server](https://img.shields.io/badge/mcp--server-mcp--cms-green)](https://github.com/zavora-ai/mcp-cms)
[![ADK-Rust Enterprise](https://img.shields.io/badge/ADK--Rust-Enterprise-purple.svg)](https://enterprise.adk-rust.com)
[![License](https://img.shields.io/badge/license-Apache--2.0-orange)](LICENSE)

## What This Skill Does

| Workflow | Calls | Revenue Impact |
|----------|-------|---------------|
| Create & Publish | 2-3 | Content marketing → leads |
| Social Distribution | 1-2 | Multi-platform reach |
| SEO Optimization | 1 | Organic traffic |
| Content Calendar | 1 | Planning visibility |

### Without this skill:
- Content published without SEO
- Same post copy-pasted to all platforms
- No engagement tracking after publishing

### With this skill:
- SEO checked before every publish
- Platform-adapted content distribution
- Engagement tracked and optimized

## Installation

```bash
git clone https://github.com/zavora-ai/skill-content-management.git ~/.skills/skills/content-management
```

## Requirements

**Required:** `mcp-cms` (26 tools)
**Cross-MCP:** `mcp-marketing` (campaigns), `mcp-analytics` (content performance)

## Scripts

### `seo_check.py`
```bash
python scripts/seo_check.py '{"title": "AI Agents", "body": "...", "seo_description": "..."}'
```

## Contributors

| [<img src="https://github.com/jkmaina.png" width="80px;"/><br /><sub><b>James Karanja Maina</b></sub>](https://github.com/jkmaina) |
|:---:|

## License

Apache-2.0 — Part of [ADK-Rust Enterprise](https://enterprise.adk-rust.com). Built with ❤️ by [Zavora AI](https://zavora.ai)
