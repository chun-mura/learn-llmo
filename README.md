# LLMO を理解する

公開されている一次情報（論文、公式ドキュメント、仕様）をもとに、Large Language Model Optimization（LLMO）を自分の言葉で説明できるようにする教材です。調査日は **2026-08-21**。この領域の製品仕様は数ヶ月で変わるので、各課の末尾にある出典 URL で原文を確認してください。

## 誰向けか

- SEO やコンテンツ制作の仕事をしていて、ChatGPT・Google の AI 回答・Perplexity に自社が出てこない理由を整理したい人
- 「LLMO 対策」という言葉は聞いたが、論文とベンダー公式のどこまでが検証済みか切り分けたい人

プログラミングの前提はありません。`robots.txt` を読めると第 4 課以降が楽です。

## 先に結論

LLMO は、生成 AI が返す回答の中で、自社のページやブランドが **言及・引用される状態** を改善する取り組みです。学術側の呼び名は **GEO（Generative Engine Optimization）** で、Aggarwal らが KDD 2024 で定式化しました。

Google Search の公式見解では、AI Overviews や AI Mode に出るために新しいファイル形式や「AI 向けの書き方」は不要で、既存の SEO（クロール・インデックス・独自で役立つコンテンツ）が土台です。GEO 論文の実験（GPT-3.5 に Google 上位 5 件を渡す構成、および Perplexity.ai）では、統計・出典・引用文の追加が可視性を押し上げ、キーワードの詰め込みは効きませんでした。

この二つは同じ現象を別の条件で見ています。教材ではどちらかに寄せず、対象プロダクトを決めてから手を動かします。

## 読み方

順番どおりに読む想定です。各課の所要は 20〜40 分。

| 課 | ファイル | 終わったときにできること |
|---|---|---|
| 1 | [curriculum/01-llmo-to-wa.md](curriculum/01-llmo-to-wa.md) | LLMO が最適化する対象を一文で言える |
| 2 | [curriculum/02-seisei-engine.md](curriculum/02-seisei-engine.md) | 生成エンジンの段取りを図なしで再現できる |
| 3 | [curriculum/03-yogo.md](curriculum/03-yogo.md) | SEO / GEO / LLMO / AEO を混ぜずに使える |
| 4 | [curriculum/04-platform.md](curriculum/04-platform.md) | 学習用ボットと検索用ボットを分けて robots.txt を書ける |
| 5 | [curriculum/05-geo-paper.md](curriculum/05-geo-paper.md) | GEO 論文の数字を、実験条件つきで引用できる |
| 6 | [curriculum/06-content.md](curriculum/06-content.md) | ページを「引用されうる塊」として直せる |
| 7 | [curriculum/07-technical.md](curriculum/07-technical.md) | インデックス、構造化データ、llms.txt の役割を切り分けられる |
| 8 | [curriculum/08-measure.md](curriculum/08-measure.md) | 測定面と、掲載を止めるスイッチを混同しない |
| 9 | [curriculum/09-gokai.md](curriculum/09-gokai.md) | よく出回る誤解を一次情報で潰せる |
| 10 | [curriculum/10-enshu.md](curriculum/10-enshu.md) | 自サイトで点検できる |

用語は [glossary.md](glossary.md) にまとめています。

## このリポジトリの中身

```
curriculum/          教材本文
glossary.md          用語
research/SOURCES.md  一次情報の目録
research/sources/    取得した原文（Markdown）
research/DIGEST.md   採用した主張と切り捨てた主張
research/OUTLINE.md  教材の骨格
```

二次の解説記事は、用語が市場でどう使われているかの記録として `research/sources/searchengineland-llmo-guide.md` だけ残しています。施策の根拠には使いません。

## さらに読む

教材を終えたあと、原文に進む順です。

1. [Google: Optimizing for generative AI features](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) — Search の生成 AI 面で公式が勧めること／しなくてよいこと。ここから始める。
2. [AI features and your website](https://developers.google.com/search/docs/appearance/ai-features) — 適格条件と query fan-out。
3. [GEO 論文 (arXiv:2311.09735)](https://arxiv.org/abs/2311.09735) — 可視性の定義と実験。数字は §3 の条件とセットで読む。
4. [OpenAI crawlers](https://developers.openai.com/api/docs/bots) / [Anthropic crawlers](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler) / [Perplexity crawlers](https://docs.perplexity.ai/docs/resources/perplexity-crawlers) — 学習と検索を分ける一次情報。
5. [llms.txt 仕様](https://llmstxt.org/) — エージェント向け地図。Search の出典選定とは別物だと分かったうえで読む。

## 出典の読み方

本文中の `[出典: …]` は `research/sources/` のファイル、または公式 URL を指します。数字や「必須ではない」といった否定は、必ず原文に当たってください。`research/sources/` は学習用の取得コピーであり、正本は各 URL です。

## この教材がやらないこと

- 特定ベンダーでの掲載を約束する手順書にはしない
- 論文の改善率を、Google AI Overviews の公式効果として扱わない
- 非公開のランキング式を推測して「必勝法」にしない
