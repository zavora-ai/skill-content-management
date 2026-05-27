#!/usr/bin/env python3
"""Check content SEO readiness before publishing."""
import json, sys

def check(data):
    issues = []
    title = data.get("title", "")
    body = data.get("body", "")
    seo_desc = data.get("seo_description", "")
    if len(title) < 10: issues.append("Title too short (< 10 chars)")
    if len(title) > 60: issues.append("Title too long (> 60 chars for SEO)")
    if not seo_desc: issues.append("Missing SEO description")
    if len(seo_desc) > 160: issues.append("SEO description > 160 chars")
    if len(body) < 300: issues.append("Body too short (< 300 chars)")
    return {"ready": len(issues) == 0, "issues": issues}

if __name__ == "__main__":
    print(json.dumps(check(json.loads(sys.argv[1])), indent=2))
