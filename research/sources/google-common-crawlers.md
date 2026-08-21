---
title: "Google's common crawlers | Google Crawling Infrastructure  |  Crawling infrastructure"
site: "Google for Developers"
source: "https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers"
domain: "developers.google.com"
language: "en"
description: "Google crawlers discover and scan websites. This overview will help you understand the common Google crawlers including the Googlebot user agent."
word_count: 1056
---

Google's common crawlers are used to find information for building Google's search indexes, perform other product specific crawls, and for analysis. They always obey [robots.txt rules](https://developers.google.com/crawling/docs/robots-txt/robots-txt-spec) when crawling automatically. The general [technical properties](https://developers.google.com/crawling/docs/crawlers-fetchers/overview-google-crawlers#crawl-technical-props) of Google's crawlers also apply to the common crawlers.

The common crawlers generally crawl from the IP ranges published in the [common-crawlers.json](https://developers.google.com/static/crawling/ipranges/common-crawlers.json) object, and the reverse DNS mask of their hostname matches `crawl-***-***-***-***.googlebot.com` or `geo-crawl-***-***-***-***.geo.googlebot.com`.

The following list shows the common crawlers, their user agent strings as they appear in the HTTP requests, their user agent tokens for the `User-agent:` line in robots.txt, and the products that are affected by crawl preferences for the crawler. Some crawlers have more than one user agent token; you need to match only one crawler token for a rule to apply. The list is not exhaustive, it only covers the requestors that are more likely to show up in log files and that we've received questions about.

## Googlebot

**`User-Agent` in HTTP requests**

| Googlebot Smartphone | ``` Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/W.X.Y.Z Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html) ``` |
| --- | --- |
| Googlebot Desktop | ``` Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Chrome/W.X.Y.Z Safari/537.36 ```  Rarely:  - `Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)` - `Googlebot/2.1 (+http://www.google.com/bot.html)` |

**robots.txt**

| User-agent token in robots.txt | `Googlebot` |
| --- | --- |
| Example robots.txt group | ``` user-agent: Googlebot allow: /archive/1Q84 disallow: /archive ``` |

**Affected products**Crawling preferences addressed to the `Googlebot` user agent affect Google Search (including Discover and all Google Search features), as well as other products such as Google Images, Google Video, Google News, and Discover.

## Googlebot Image

**User-Agent in HTTP requests**

```
Googlebot-Image/1.0
```

**robots.txt**

| User-agent token in robots.txt | `Googlebot-Image`  ---  `Googlebot` |
| --- | --- |
| Example robots.txt group | ``` user-agent: Googlebot-Image allow: /archive/1Q84 disallow: /archive/moons.jpg ``` |

**Affected products**Crawling preferences addressed to the `Googlebot-Image` user agent affect Google Images, Discover, Google Video, and all features in Google Search where images, logos, and favicons are presented.

## Googlebot Video

**User-Agent in HTTP requests**

```
Googlebot-Video/1.0
```

**robots.txt**

| User-agent token in robots.txt | `Googlebot-Video`  ---  `Googlebot` |
| --- | --- |
| Example robots.txt group | ``` user-agent: Googlebot-Video allow: /archive/1Q84 disallow: /archive/ ``` |

**Affected products**Crawling preferences addressed to the `Googlebot-Video` user agent affect video-related Google Search features and other products dependent on videos.

## Googlebot News

**User-Agent in HTTP requests**Googlebot-news doesn't have a separate HTTP request user agent string. Crawling is done with [various Googlebot user agent strings](#googlebot).**robots.txt**

| User-agent token in robots.txt | `Googlebot-News`  ---  `Googlebot` |
| --- | --- |
| Example robots.txt group | ``` user-agent: Googlebot-News allow: /archive/1Q84 disallow: /archive/ ``` |

**Affected products**Crawling preferences addressed to the `Googlebot-News` user agent affect the Google News product, including [news.google.com](https://news.google.com/) and the Google News app.

## Google StoreBot

**User-Agent in HTTP requests**

| Desktop agent | ``` Mozilla/5.0 (X11; Linux x86_64; Storebot-Google/1.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/W.X.Y.Z Safari/537.36 ``` |
| --- | --- |
| Mobile agent | ``` Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012; Storebot-Google/1.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/W.X.Y.Z Mobile Safari/537.36 ``` |

**robots.txt**

| User-agent token in robots.txt | `Storebot-Google` |
| --- | --- |
| Example robots.txt group | ``` user-agent: Storebot-Google allow: /archive/1Q84 disallow: /archive/konbini ``` |

**Affected products**Crawling preferences addressed to the `Storebot-Google` user agent affect all surfaces of Google Shopping (for example, the Shopping tab in Google Search and [Google Shopping](https://shopping.google.com/)).

## Google-InspectionTool

**User-Agent in HTTP requests**

| Desktop agent | ``` Mozilla/5.0 (compatible; Google-InspectionTool/1.0) ``` |
| --- | --- |
| Mobile agent | ``` Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/W.X.Y.Z Mobile Safari/537.36 (compatible; Google-InspectionTool/1.0) ``` |

**robots.txt**

| User-agent token in robots.txt | `Google-InspectionTool`  ---  `Googlebot` |
| --- | --- |
| Example robots.txt group | ``` user-agent: Google-InspectionTool allow: /archive/1Q84 disallow: /archive/ ``` |

**Affected products**Crawling preferences addressed to the `Google-InspectionTool` user agent affect Search testing tools such as the [Rich Result Test](https://search.google.com/test/rich-results) and [URL inspection](https://support.google.com/webmasters/answer/9012289) in Search Console. It has no effect on Google Search or other products.

## GoogleOther

**User-Agent in HTTP requests**

```
Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/W.X.Y.Z Mobile Safari/537.36 (compatible; GoogleOther)
```

---

```
Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; GoogleOther) Chrome/W.X.Y.Z Safari/537.36
```

**robots.txt**

| User-agent token in robots.txt | `GoogleOther` |
| --- | --- |
| Example robots.txt group | ``` user-agent: GoogleOther allow: /archive/1Q84 disallow: /archive/ ``` |

**Affected products**Crawling preferences addressed to the `GoogleOther` user agent don't affect any specific product. GoogleOther is the generic crawler that may be used by various product teams for fetching publicly accessible content from sites. For example, it may be used for one-off crawls for internal research and development.

## GoogleOther-Image

**User-Agent in HTTP requests**

```
GoogleOther-Image/1.0
```

**robots.txt**

| User-agent token in robots.txt | `GoogleOther-Image`  ---  `GoogleOther` |
| --- | --- |
| Example robots.txt group | ``` user-agent: GoogleOther-Image allow: /archive/1Q84 disallow: /archive/moon.jpg ``` |

**Affected products**Crawling preferences addressed to the `GoogleOther-Image` user agent don't affect any specific product, similar to GoogleOther. GoogleOther-Image is the version of GoogleOther optimized for fetching publicly accessible image URLs.

## GoogleOther-Video

**User-Agent in HTTP requests**

```
GoogleOther-Video/1.0
```

**robots.txt**

| User-agent token in robots.txt | `GoogleOther-Video`  ---  `GoogleOther` |
| --- | --- |
| Example robots.txt group | ``` user-agent: GoogleOther-Video allow: /archive/1Q84 disallow: /archive ``` |

**Affected products**Crawling preferences addressed to the `GoogleOther-Video` user agent don't affect any specific product, similar to GoogleOther. GoogleOther-Video is the version of GoogleOther optimized for fetching publicly accessible video URLs.

## Google-CloudVertexBot

**User-Agent substring in HTTP requests**

```
Google-CloudVertexBot
```

**robots.txt**

| User-agent token in robots.txt | `Google-CloudVertexBot`  ---  `Googlebot` |
| --- | --- |
| Example robots.txt group | ``` user-agent: Google-CloudVertexBot allow: /archive/1Q84 disallow: /archive/ ``` |

**Affected products**Crawling preferences addressed to the `Google-CloudVertexBot` user agent affect crawls requested by the site owners' for building [Vertex AI Agents](https://cloud.google.com/generative-ai-app-builder/docs/prepare-data#website). It has no effect on Google Search or other products.

## Google-Extended

**User-Agent in HTTP requests**Google-Extended doesn't have a separate HTTP request user agent string. Crawling is done with existing Google user agent strings; the robots.txt user-agent token is used in a control capacity.**robots.txt**

| User-agent token in robots.txt | `Google-Extended` |
| --- | --- |
| Example robots.txt group | ``` user-agent: Google-Extended allow: /archive/1Q84 disallow: /archive/ ``` |

**Affected products**

`Google-Extended` is a standalone product token that web publishers can use to manage whether content Google crawls from their sites may be used for training future generations of Gemini models that power [Gemini Apps](https://support.google.com/gemini/answer/13594961#gemini_apps&zippy=%2Cwhat-are-gemini-apps) and [Vertex AI API for Gemini](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/inference) and for grounding (providing content from the Google Search index to the model at prompt time to improve factuality and relevancy) in [Gemini Apps](https://support.google.com/gemini/answer/13594961#gemini_apps&zippy=%2Cwhat-are-gemini-apps) and [Grounding with Google Search on Vertex AI](https://cloud.google.com/vertex-ai/generative-ai/docs/grounding/overview#ground-public).

Google-Extended does not impact a site's inclusion in Google Search nor is it used as a ranking signal in Google Search.

## A note about Chrome/W.X.Y.Z in user agents

The string **Chrome/ *W.X.Y.Z*** in the user agent strings in the list is a placeholder that represents the version of the Chrome browser used by that user agent: for example, `41.0.2272.96`. This version number increases over time to [match the latest Chromium release version used by Googlebot](https://developers.google.com/search/blog/2019/05/the-new-evergreen-googlebot).

If you are searching your logs or filtering your server for a user agent with this pattern, use wildcards for the version number rather than specifying an exact version number.