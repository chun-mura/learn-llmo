---
title: "Search generative AI control - Search Console Help"
site: "support.google.com"
source: "https://support.google.com/webmasters/answer/16908024"
domain: "support.google.com"
language: "en"
description: "Note: We're rolling out this control to a subset of website owners, allowing for thorough testing before rolling it out further. Use the Search generative AI control to manage your site's inclusi"
word_count: 969
---

## Search generative AI control

**Note**: We're rolling out this control to a subset of website owners, allowing for thorough testing before rolling it out further.

Use the Search generative AI control to manage your site's inclusion in the following generative AI features on Google Search. We expect to update this list over time as we develop Google Search.

See and manage the Search generative AI control for your property under **Settings** \> **Search generative AI** in Search Console.

## Change your control

To change your Search generative AI control choice, open the [Search generative AI control page](https://search.google.com/search-console/settings/search-gen-ai) and choose one of the following:

To measure how your content is performing in Search generative AI features, use the [Generative AI performance report](https://support.google.com/webmasters/answer/16984139). This can help you get an idea of how changing your control may impact traffic to your site.

## What happens if I exclude my site?

If you exclude your site, links to your site and your site's content won't appear in [Search generative AI features](#gen-ai-features). Content from other sites will still be available in those features, and it may appear similar to yours. Content crawled from your site won't be eligible to be used as an input to generate an AI response or preview in [Search generative AI features](#gen-ai-features).

This control only affects whether your content can appear in certain Search generative AI features; this control isn't used as a ranking or inclusion signal affecting other parts of Search. This control doesn't override publishers' other choices to participate in particular services, such as Merchant Center and Google Ads. Your site's content may still be used to power Google Search as a whole, like helping our systems better understand the [language of users’ queries](https://blog.google/products-and-platforms/products/search/search-language-understanding-bert/) and the language on pages on the web. This control doesn't affect AI training; to limit training of the models used to generate responses in Search generative AI features, use [Google-Extended](https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers#google-extended). To block your content from appearing in Google Search completely, use [noindex](https://developers.google.com/search/docs/crawling-indexing/block-indexing).

## How long it takes for a control change to take effect

Once you change your control in Search Console, it generally takes a few days for your site's content to be excluded from the [applicable Search generative AI features](#gen-ai-features). Content will be excluded within 1-2 days after the control goes live, but some content may take longer to be excluded due to caching and propagation across Google systems.

## How Search generative AI control inheritance works

By default, a property inherits its Search generative AI control from its closest parent that has changed its control to stop inheriting. For a property in which none of its parents manually-configured their control to stop inheriting, the property is set to inherit the control of its top-level domain property.

For example, the child property ([URL-prefix property](https://support.google.com/webmasters/answer/10432366) `https://example.com/business/cats`) would inherit the control of its parent (domain property `example.com`) by default, unless an owner of a closer parent property (`https://example.com/business/` or `https://example.com/`) [manually configured the control](#configure-child) to stop inheriting. You can check whether your property is inheriting its control and [manually configure the control](#configure-child) for your property at any time.

### About parent and child properties

**Note**: Many properties can be both a parent and a child of other properties.

- **Parent property**: A higher-level property that has child property nested below it. It may be a top-level domain (the highest-level domain for a single site on the web) property, a subdomain property, or a [URL-prefix property](https://support.google.com/webmasters/answer/10432366).  
	Examples of parent properties
	Here are some examples of a **top-level domain**:
	- `example.com`
	- `example.co.uk`
	Here are some examples of a **subdomain property**:
	- `blog.example.com`
	Here are some examples of a **URL-prefix property**:
	- `https://m.example.com/petstore/`
	- `https://example.com/`
	- `http://www.example.com/cats/`
- **Child property**: A lower-level, URL-prefix path property, or a domain property which is not the top-level, that's nested under another property. It may be nested under a top-level domain property or another property.

![](https://lh3.googleusercontent.com/SDQxBGPSDA2ggu-qr57nDcINa-_wlsSU9OZ1wM-NJLG7eAHnNJjrpVRASxrGOWEHfYY=w895)

1. The top-level domain `example.com` is a parent property of all properties below it. Both **2) `https://example.com`** and **3) `https://example.com/blog`** are child properties of `example.com`, and therefore inherit `example.com` 's setting by default, if there was no manually configured setting.
2. The URL-prefix property `https://example.com` is a parent property of the property below it. If `https://example.com` has a setting configured, then 3) `https://example.com/blog` inherits that setting by default, as that property is its closest parent property with a configured setting.

### Examples of parent and child properties

Here are some examples that show how the parent and child relationship works in terms of Search Console properties:

| **Parent property** | **Examples of child properties** | **Not a child property** |
| --- | --- | --- |
| example.com   (top-level domain) | `✅ https://example.com/business/ `  `✅ http://example.com/`  `✅ blog.example.com`  `✅ https://www.blog.example.com/path` | ❌ example.co.uk |
| https://www.example.com/   (URL-prefix property) | `✅ https://www.example.com/business/`  `✅ https://www.example.com/cats/kittens/` | ❌ example.com  ❌ http://www.example.com/  ❌ https://example.com/ |
| https://example.com/business/   (URL-prefix property) | `✅ https://example.com/business/cats/`  `✅ https://example.com/business/dogs/`  `✅ https://example.com/business/cats/kittens` | ❌ https://example.com/  ❌ http://example.com/business/cats/  ❌ https://www.example.com/business/cats/ |
| http://example.com/   (URL-prefix property) | `✅ http://example.com/cat/`  `✅ http://example.com/cat/kittens` | ❌ https://example.com/  ❌ http://www.example.com/cat |
| blog.example.com   (domain property) | `✅ m.blog.example.com`  `✅ https://www.blog.example.com`  `✅ http://blog.example.com`  `✅ https://m.blog.example.com`  `✅ https://blog.example.com/path` | ❌ example.com  ❌ https://example.com/  ❌ bl.example.com |

### Manually configure the Search generative AI control for a child property

Owners of a child property can choose to follow its parent property's Search generative AI control or change it for the specific child property and its subpages. To specify a control for a given child property, log in to that property in Search Console and update its configuration using the Search generative AI control page.

## Submitting feedback

You can [submit feedback on the Search generative AI control](https://docs.google.com/forms/d/e/1FAIpQLScKKRDQnnGxDoyWkargi1ibrgh5Jw7p1FS0f2xLiboJJSEoLA/viewform?usp=preview). Note that this feedback helps improve Search Console overall, and we generally can't act upon individual submissions.

If you have feedback about other Search Console features, use the feedback link within Search Console. If you have questions about how your site appears in Search, visit the [Search Central help community](http://goo.gle/sc-forum) to discuss with peers.