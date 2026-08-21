---
title: "Perplexity Crawlers"
site: "Perplexity"
source: "https://docs.perplexity.ai/docs/resources/perplexity-crawlers"
domain: "docs.perplexity.ai"
language: "en"
description: "We strive to improve our service every day by delivering the best search experience possible. To achieve this, we collect data using web crawlers (\"robots\") and user agents that gather and index information from the internet, operating either automatically or in response to user requests. Webmasters can use the following robots.txt tags to manage how their sites and content interact with Perplexity. Each setting works independently, and it may take up to 24 hours for our systems to reflect changes."
word_count: 346
---

| User Agent | Description |
| --- | --- |
| PerplexityBot | `PerplexityBot` is designed to surface and link websites in search results on Perplexity. It is not used to crawl content for AI foundation models. To ensure your site appears in search results, we recommend allowing `PerplexityBot` in your site’s `robots.txt` file and permitting requests from our published IP ranges listed below.      Full user-agent string: `Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; PerplexityBot/1.0; +https://perplexity.ai/perplexitybot)`      Published IP addresses: [https://www.perplexity.com/perplexitybot.json](https://www.perplexity.com/perplexitybot.json) |
| Perplexity‑User | `Perplexity-User` supports user actions within Perplexity. When users ask Perplexity a question, it might visit a web page to help provide an accurate answer and include a link to the page in its response. `Perplexity-User` controls which sites these user requests can access. It is not used for web crawling or to collect content for training AI foundation models.      Full user-agent string: `Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Perplexity-User/1.0; +https://perplexity.ai/perplexity-user)`      Published IP addresses: [https://www.perplexity.com/perplexity-user.json](https://www.perplexity.com/perplexity-user.json)      Since a user requested the fetch, this fetcher generally ignores robots.txt rules. |

## WAF Configuration

If you’re using a Web Application Firewall (WAF) to protect your site, you may need to explicitly whitelist Perplexity’s bots to ensure they can access your content. Below are configuration guidelines for popular WAF providers.

### Cloudflare WAF

To configure Cloudflare WAF to allow Perplexity bots:

### AWS WAF

For AWS WAF configuration, create IP sets and string match conditions:

### IP Address Sources

Always use the most current IP ranges from the official JSON endpoints. These addresses are updated regularly and should be the source of truth for your WAF configurations.

- **PerplexityBot IP addresses**: [https://www.perplexity.com/perplexitybot.json](https://www.perplexity.com/perplexitybot.json)
- **Perplexity-User IP addresses**: [https://www.perplexity.com/perplexity-user.json](https://www.perplexity.com/perplexity-user.json)

Set up automated processes to periodically fetch and update your WAF rules with the latest IP ranges from these endpoints to ensure continuous access for Perplexity bots.

### Best Practices

When configuring WAF rules for Perplexity bots, combine both User-Agent string matching and IP address verification for enhanced security while ensuring legitimate bot traffic can access your content.

Changes to WAF configurations may take some time to propagate. Monitor your logs to ensure the rules are working as expected and that legitimate Perplexity bot traffic is being allowed through.