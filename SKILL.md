---
name: content-management
description: Orchestrate content operations — manage articles, schedule social media, publish to YouTube, organize media library, optimize SEO, and run publishing workflows. Use when creating blog posts, scheduling social media, managing content calendars, publishing articles, uploading media, or optimizing SEO.
license: Apache-2.0
compatibility: Requires mcp-cms server connected (WordPress, Contentful, YouTube, Twitter, LinkedIn, Meta, or Custom API).
allowed-tools: [list_content, get_content, create_content, update_content, publish_content, unpublish_content, list_social_accounts, schedule_social_post, get_social_metrics, list_scheduled_posts, delete_scheduled_post]
metadata:
  category: communication
  author: Zavora AI
  mcp-server: mcp-cms
  revenue-impact: direct
  success-criteria:
    trigger-rate: "90% on content/publishing queries"
    publishing-speed: "Draft to published in 3 calls"
---

# Content Management

You manage the content lifecycle — create, edit, publish, and distribute across web and social. Always check SEO before publishing. Never publish without review.

## Decision Tree

```
├── "write", "article", "blog post", "create content"? → create_content (draft)
├── "publish", "go live", "make public"? → publish_content
├── "social", "post", "schedule", "twitter", "linkedin"? → schedule_social_post
├── "metrics", "engagement", "views"? → get_social_metrics
├── "calendar", "scheduled", "upcoming"? → list_scheduled_posts
├── "unpublish", "take down"? → unpublish_content
```

## Key Workflows

### Create & Publish Article (3 calls)
1. `create_content(title, body, tags, seo_description)` → draft
2. Review content quality
3. `publish_content(id)` → live on website

### Social Media Distribution (2 calls)
1. `schedule_social_post(platforms: ["twitter", "linkedin"], content, time)` → scheduled
2. `get_social_metrics(post_id)` → engagement tracking

### Content Calendar (1 call)
1. `list_scheduled_posts` → all upcoming content across platforms

## MUST DO
- Include SEO description on every article
- Schedule social posts for optimal times (not midnight)
- Track engagement after publishing

## MUST NOT DO
- Don't publish without SEO metadata
- Don't post same content to all platforms without adapting format
