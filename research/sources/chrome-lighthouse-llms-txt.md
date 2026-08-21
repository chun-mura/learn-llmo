---
title: "llms.txt  |  Lighthouse"
site: "Chrome for Developers"
source: "https://developer.chrome.com/docs/lighthouse/agentic-browsing/llms-txt"
domain: "developer.chrome.com"
language: "en"
description: "Learn about the llms.txt audit and how to provide a machine-readable summary of your website."
word_count: 135
---

The `llms.txt` file is an [emerging convention](https://llmstxt.org/) used to provide a machine-readable summary of a website's content, specifically designed for LLMs and AI agents.

Without this file, agents may spend more time crawling the site to understand its high-level structure and primary content.

## How the llms.txt audit works

Lighthouse flags the pages if a server error occurs when attempting to retrieve the `llms.txt` file. If the file is not provided by the server (resulting in a 404), the audit is marked as Not Applicable (N/A), as providing the file is optional at the moment.

## How to fix

Create an `llms.txt` file and place it in the root directory of your website (for example, `https://example.com/llms.txt`). The file should follow the [llms.txt specification](https://llmstxt.org/) and provide a concise Markdown summary of your site's purpose and key links.