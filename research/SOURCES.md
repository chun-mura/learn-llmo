# 一次情報の目録

収集日: 2026-08-21。教材の主張はここに列挙した公開文書に根拠を置く。二次解説（代理店ブログ、プレイブック）は用語の流通状況を見るために一部残したが、事実の根拠には使わない。

## 学術

| ファイル | 出典 | 何が一次か |
|---|---|---|
| `sources/2024-aggarwal-geo-paper.md` | Aggarwal et al., *GEO: Generative Engine Optimization*, KDD 2024 / arXiv:2311.09735 | GEO という語と、引用可視性の実験・指標・ベンチマークの導入論文 |
| `sources/geo-optim-github-readme.md` | [GEO-optim/GEO](https://github.com/geo-optim/geo) | 論文著者のコードと GEO-bench の所在 |

## Google（公式）

| ファイル | 出典 | 何が一次か |
|---|---|---|
| `sources/google-ai-features.md` | [AI features and your website](https://developers.google.com/search/docs/appearance/ai-features) | AI Overviews / AI Mode の適格条件、query fan-out、追加の技術要件はないこと |
| `sources/google-ai-optimization-guide.md` | [Optimizing for generative AI features](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) | Google 自身による「GEO/AEO ハック」否定と、公式に勧めること |
| `sources/google-succeeding-in-ai-search.md` | [Succeeding in AI search](https://developers.google.com/search/blog/2025/05/succeeding-in-ai-search) (2025-05-21) | 独自コンテンツ、プレビュー制御、構造化データは表示内容と一致させること |
| `sources/google-helpful-content.md` | [Creating helpful, people-first content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) | E-E-A-T は単一のランキング因子ではないこと、people-first の自己点検 |
| `sources/google-structured-data.md` | [Intro to structured data](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data) | 構造化データはリッチリザルト適格化。ページに見えない情報をマークアップしない |
| `sources/google-common-crawlers.md` | [Google's common crawlers](https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers) | Google-Extended は Search の掲載・順位に影響しない |
| `sources/google-search-generative-ai-control.md` | [Search generative AI control](https://support.google.com/webmasters/answer/16908024) | Search Console の生成 AI 掲載トグル。学習オプトアウトとは別 |
| `sources/google-new-controls-website-owners.md` | [New opportunities, control and insights](https://blog.google/products-and-platforms/products/search/new-controls-website-owners/) (2026-06-03) | AI Overviews 月間 25 億 MAU 等の製品側発表、UK からのトグル試験 |

## OpenAI / Anthropic / Perplexity（公式）

| ファイル | 出典 | 何が一次か |
|---|---|---|
| `sources/openai-crawlers.md` | [Overview of OpenAI Crawlers](https://developers.openai.com/api/docs/bots) | GPTBot / OAI-SearchBot / ChatGPT-User の独立、ChatGPT-User は robots.txt が適用されない場合がある |
| `sources/openai-introducing-chatgpt-search.md` | [Introducing ChatGPT search](https://openai.com/index/introducing-chatgpt-search/) (2024-10-31) | ChatGPT search の公開、第三者検索プロバイダ＋パートナーコンテンツ |
| `sources/anthropic-crawlers.md` | [Anthropic crawler FAQ](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler) | ClaudeBot / Claude-User / Claude-SearchBot。robots.txt と Crawl-delay を尊重 |
| `sources/perplexity-crawlers.md` | [Perplexity Crawlers](https://docs.perplexity.ai/docs/resources/perplexity-crawlers) | PerplexityBot は学習用ではない。Perplexity-User は一般に robots.txt を無視 |

## 仕様・周辺

| ファイル | 出典 | 何が一次か |
|---|---|---|
| `sources/llmstxt-spec-v2.md` | [The /llms.txt file, v2](https://llmstxt.org/) (Jeremy Howard) | llms.txt の提案仕様。Google Search の公式採用ではない |
| `sources/chrome-lighthouse-llms-txt.md` | [Lighthouse llms.txt audit](https://developer.chrome.com/docs/lighthouse/agentic-browsing/llms-txt) | 任意。404 は N/A。サーバーエラーだけフラグ |

## 用語の流通（二次。定義の根拠にはしない）

| ファイル | 出典 | 使い方 |
|---|---|---|
| `sources/searchengineland-llmo-guide.md` | [What is LLMO?](https://searchengineland.com/guides/large-language-model-optimization-llmo) | 英語圏マーケで LLMO がどう説明されているかの記録。実験事実ではない |
