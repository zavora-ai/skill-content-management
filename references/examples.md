# CMS Examples

## Example 1: "Write and publish a blog post about AI agents"
```
create_content(title: "Why AI Agents Are the Future", body: "...", tags: ["ai", "agents"], seo: "...")
publish_content(id)
schedule_social_post(platforms: ["linkedin"], content: "New post: Why AI Agents Are the Future [link]")
```

## Example 2: "What's scheduled for this week?"
```
list_scheduled_posts(range: "this_week") → [{platform: "twitter", time: "Mon 9am"}, ...]
```
