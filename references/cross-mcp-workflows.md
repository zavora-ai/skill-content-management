# CMS Cross-MCP Workflows

## CMS + Marketing: Content → Campaign
```
CMS: create_content(title: "Why AI Agents Matter", type: "blog") → article
CMS: publish_content(id) → live
MARKETING: create_campaign(name: "AI Agents Blog Push", content_id)
MARKETING: schedule_post(platforms: ["linkedin", "twitter"], content: article_summary)
```

## CMS + Analytics: Publish → Track → Optimize
```
CMS: publish_content(id)
ANALYTICS: query_metric(name: "blog_views", filter: article_id)
CMS: get_social_metrics(post_id) → engagement
→ If low engagement: CMS: update_content(id, new_headline)
```
