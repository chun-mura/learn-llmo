# 教材アウトライン

各節の典拠は `research/SOURCES.md` のファイル名。典拠のない節は作らない。

1. **LLMO とは何か** — 問題設定。検索結果の順位ではなく、生成回答の中で言及・引用されること。用語は日本で LLMO、論文では GEO。典拠: GEO 論文 abstract、SEL は流通記録のみ。
2. **生成エンジンの仕組み** — クエリ分解、検索、要約、引用つき生成。query fan-out。典拠: GEO §2.1、Google AI features、Google AI optimization guide。
3. **用語地図** — SEO / GEO / LLMO / AEO。Google は Search では SEO の延長と言う。典拠: GEO §7、Google AI optimization guide「Mythbusting」。
4. **プラットフォーム別の取得と引用** — Google / ChatGPT / Claude / Perplexity。学習と検索を分ける。典拠: 各社クローラ文書、ChatGPT search 発表。
5. **GEO 論文を読む** — 指標、9手法、結果、限界。典拠: GEO 論文 Table 1–5、Limitations。
6. **中身が引用される条件** — 独自性、出典、統計、引用。Google の people-first と論文の手法を並べる。典拠: helpful content、AI optimization guide、GEO §4。
7. **技術的な準備** — インデックス、robots.txt、プレビュー制御、構造化データ、llms.txt の位置づけ。典拠: AI features、crawlers、structured data、llmstxt.org、Lighthouse。
8. **測定とコントロール** — Search Console、生成 AI トグル、Google-Extended。ChatGPT 側は robots.txt。典拠: Search Console ヘルプ、Google ブログ、OpenAI bots。
9. **よくある誤解** — 論文数字の誤用、学習ブロック＝検索ブロック、llms.txt 必須説。典拠: 上記の矛盾表。
10. **演習** — robots.txt、ページ添削、測定設計。前レッスンの手順を使う。
