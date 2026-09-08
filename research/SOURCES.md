# 一次情報の目録

収集日: 2026-08-21、追補 2026-09-06。教材の主張はここに列挙した公開文書に根拠を置く。二次解説（代理店ブログ、プレイブック）は用語の流通状況を見るために一部残したが、事実の根拠には使わない。

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

## 追補（2026-09-06 確認）

この節は原文の取得コピーを置かず、URL を正本として直接参照する。教材に載せた文言は、いずれもこの一覧の原文で確認した。

### 標準・インフラ

| 出典 | 何が一次か |
|---|---|
| [RFC 9309, Robots Exclusion Protocol](https://www.rfc-editor.org/rfc/rfc9309.html) | 規則はアクセス認可ではないこと（§1）、最長一致（§2.2.2）、UA は case-insensitive（§2.2.1）、4xx は許可（MAY）・5xx は全面禁止（MUST。30 日規模の継続は例外）（§2.3.1.3, §2.3.1.4）、24 時間キャッシュ（SHOULD NOT、§2.4）、500 KiB（§2.5） |
| [IETF aipref WG charter](https://datatracker.ietf.org/doc/charter-ietf-aipref/) / [draft-ietf-aipref-attach](https://datatracker.ietf.org/doc/draft-ietf-aipref-attach/) | 利用意向の表現を標準化する作業。`Content-Usage` は Internet-Draft であり RFC ではない |
| [Cloudflare, Your site, your rules: new AI traffic options for all customers](https://blog.cloudflare.com/content-independence-day-ai-options/)（2026-07-01） / [managed robots.txt](https://developers.cloudflare.com/bots/additional-configurations/managed-robots-txt/) | Search / Agent / Training の三分類、2026-09-15 からの新規ドメイン既定ブロック、`Content-Signal:` ディレクティブ |

### ベンダーのクローラ（四社の外側）

| 出典 | 何が一次か |
|---|---|
| [Meta, Web crawlers](https://developers.facebook.com/docs/sharing/webmasters/web-crawlers/) | Meta-ExternalAgent / -WebIndexer / -ExternalFetcher の役割。ExternalFetcher は robots.txt を迂回しうる |
| [Apple, About Applebot](https://support.apple.com/en-us/119829)（2026-09-04 更新） | Applebot-Extended は自身クロールせず、学習利用だけを制御。拒否しても検索結果には残る |
| [Amazonbot](https://developer.amazon.com/amazonbot) | Amazonbot は学習に使われうる。`noarchive` で学習除外。robots.txt キャッシュは最大 30 日。Amzn-SearchBot / Amzn-User は学習に使わない |
| [Mistral, Robots](https://docs.mistral.ai/robots/) | MistralAI-Training / -Index / -User の分離 |
| [DuckAssistBot](https://duckduckgo.com/duckduckgo-help-pages/results/duckassistbot/) | AI 回答用のライブ取得。学習には使わない。反映 72 時間。検索順位に影響しない |
| [Common Crawl, CCBot](https://commoncrawl.org/ccbot) | 公開アーカイブ用。なりすまし注意と IP 検証 |

Bytespider（ByteDance）は到達可能な公式文書を確認できなかった。**未確認**として教材に明記する。

### 回答面と計測

| 出典 | 何が一次か |
|---|---|
| [Search Console ヘルプ, Generative AI performance report](https://support.google.com/webmasters/answer/16984139) | 対象は AI Overviews と AI Mode。指標は表示回数のみで、クリック・順位・CTR は無く、両面の内訳も出ない |
| [Bing Webmaster Blog, Introducing AI Performance in Bing Webmaster Tools](https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview)（2026-02-10, Public Preview） | Total Citations / Average Cited Pages / Grounding Queries / URL 単位。Grounding Queries はサンプル |
| [Bing Webmaster Blog, NOCACHE / NOARCHIVE](https://blogs.bing.com/webmaster/september-2023/Announcing-new-options-for-webmasters-to-control-usage-of-their-content-in-Bing-Chat)（2023-09-22） | Copilot 回答と学習の制御。両方あれば NOCACHE 扱い。通常の検索表示は変えない |
| [Google Analytics ヘルプ, Default channel group](https://support.google.com/analytics/answer/9756891) | AI Assistant チャネルの定義。Google 自身の AI Overviews と AI Mode は除外される |
| [IndexNow ドキュメント](https://www.indexnow.org/documentation) | 参加エンジン間で URL 通知を共有する仕組み。AI 回答との関係の記述は無い |

### 学術（GEO 論文以降）

| 出典 | 何が一次か |
|---|---|
| Puerto, Gubri, Green, Oh & Yun, *C-SEO Bench: Does Conversational SEO Work?*, NeurIPS 2025 Datasets & Benchmarks / [arXiv:2506.11097](https://arxiv.org/abs/2506.11097) | 競合採用・複数ドメイン条件で、多くの C-SEO 手法が無効〜逆効果。従来 SEO 的手法が有効。ゼロサム性 |
| Wallat, Heuss, de Rijke & Anand, *Correctness is not Faithfulness in RAG Attributions*, [arXiv:2412.18004](https://arxiv.org/abs/2412.18004) | 引用の correctness と faithfulness の分離。最大 57% が post-rationalization |
| Liu et al., *Lost in the Middle: How Language Models Use Long Contexts*, TACL 2024 (Vol. 12) / [arXiv:2307.03172](https://arxiv.org/abs/2307.03172) | 入力文脈の位置バイアス |
| Zhang et al., *Practical Poisoning Attacks against RAG*（CorruptRAG）, ACM SACMAT 2026 / [arXiv:2504.03957](https://arxiv.org/abs/2504.03957) | 毒入りテキスト 1 件での RAG 出力操作。UGC 面のリスクとして引く |

## 教材の作り方の根拠（学習科学）

教材の内容ではなく、`site/` の作り（想起カード、間隔反復、インターリーブ、進捗の見せ方）の根拠。

| 出典 | 何を根拠にしているか |
|---|---|
| Adesope, Trevisan & Sundararajan 2017, *Review of Educational Research* 87(3) | 練習テストのメタ分析 g = 0.61。再読その他すべての比較条件を上回る |
| Dunlosky, Rawson, Marsh, Nathan & Willingham 2013, *Psychological Science in the Public Interest* 14(1) | 練習テストと分散学習が high utility、再読・ハイライト・要約は low utility |
| Cepeda, Pashler, Vul, Wixted & Rohrer 2006, *Psychological Bulletin* 132(3) / Cepeda et al. 2008, *Psychological Science* 19(11) | 分散学習。最適間隔は保持目標までの日数に対する割合で決まる |
| Bertsch, Pesta, Wiscott & McDaniel 2007, *Memory & Cognition* 35(2) | 生成効果 d ≈ 0.40。答えを見る前に自分で出させる根拠 |
| Butler, Karpicke & Roediger 2007, *JEP: Applied* 13(4) | フィードバックのタイミング。誤答カードを翌日固定にしない根拠 |
| Brunmair & Richter 2019, *Psychological Bulletin* 145(11) | 交互配置 g = 0.42。効果は条件依存で万能ではない |
| Koriat & Bjork 2005, *JEP: LMC* 31(2) | 流暢性の錯覚。進捗の主指標を「読んだ量」にしない根拠 |
| Mayer & Moreno 2003, *Educational Psychologist* 38(1) | segmenting / signaling / coherence / redundancy |
| Pashler, McDaniel, Rohrer & Bjork 2008, *PSPI* 9(3) | 学習スタイルに合わせた指導の根拠は無い。実装しない根拠 |
| Murre & Dros 2015, *PLOS ONE* 10(7) | 忘却曲線の再現。教科書的な滑らかな指数曲線は正確ではない。図として使わない根拠 |

間隔反復のアルゴリズム（Leitner / SM-2 / FSRS）の優劣を比較した人対象の対照試験は見当たらなかった。実装は Leitner の箱に留め、根拠を主張するのは「間隔をあけること」までとする。

## 用語の流通（二次。定義の根拠にはしない）

| ファイル | 出典 | 使い方 |
|---|---|---|
| `sources/searchengineland-llmo-guide.md` | [What is LLMO?](https://searchengineland.com/guides/large-language-model-optimization-llmo) | 英語圏マーケで LLMO がどう説明されているかの記録。実験事実ではない |
