# LLMO を理解する

公開されている一次情報（論文、公式ドキュメント、仕様）をもとに、Large Language Model Optimization（LLMO）を自分の言葉で説明できるようにする教材です。調査日は **2026-08-21**、追補は **2026-09-06**。

**学習用の画面は HTML です。** [`site/index.html`](site/index.html) をブラウザで開いてください。教材は 1 ファイルで、左の章名や番号をクリックすると同じページ内で移動します。各章は一節ずつ出ます。Markdown 原文は `curriculum/` に残してあります。

読むだけで終わらない作りにしてあります。各節の終わりに、閉じた状態の問い（想起カード）が入っています。選択肢から選び、答え合わせを押すと正誤と解説が出ます。正解すると次の出題日が 1 → 3 → 7 → 16 → 35 日と伸び、期限が来たカードだけが「復習」面に、章をまたいで混ぜて出ます。根拠は画面のホームと `research/SOURCES.md` の学習科学の節にあります。

## 誰向けか

- SEO やコンテンツ制作の仕事をしていて、ChatGPT・Google の AI 回答・Perplexity に自社が出てこない理由を整理したい人
- 「LLMO 対策」という言葉は聞いたが、論文とベンダー公式のどこまでが検証済みか切り分けたい人

プログラミングの前提はありません。`robots.txt` を読めると第 4 章以降が楽です。

## 先に結論

LLMO は、生成 AI が返す回答の中で、自社のページやブランドが **言及・引用される状態** を改善する取り組みです。学術側の呼び名は **GEO（Generative Engine Optimization）** で、Aggarwal らが KDD 2024 で定式化しました。

Google Search の公式見解では、AI Overviews や AI Mode に出るために新しいファイル形式や「AI 向けの書き方」は不要で、既存の SEO（クロール・インデックス・独自で役立つコンテンツ）が土台です。GEO 論文の実験（GPT-3.5 に Google 上位 5 件を渡す構成、および Perplexity.ai）では、統計・出典・引用文の追加が可視性を押し上げ、キーワードの詰め込みは効きませんでした。

この二つは同じ現象を別の条件で見ています。教材ではどちらかに寄せず、対象プロダクトを決めてから手を動かします。

## 読み方

[`site/index.html`](site/index.html) をブラウザで開きます。順番どおり、一節ずつです。各章 20〜40 分。全部見たいときは画面下の「全部見る」、または `A` キー。復習面では `1`〜`4` で選択肢を選び、Space で答え合わせ、もう一度 Space で次のカードへ。章ごとの回答は「この章をリセット」で消せます。進捗と復習の期限はブラウザの localStorage にだけ残ります。

| 章 | 画面 | 終わったときにできること |
|---|---|---|
| 1 | [site/index.html#l01](site/index.html#l01) | LLMO が最適化する対象を一文で言える |
| 2 | [site/index.html#l02](site/index.html#l02) | 生成エンジンの段取りを書き起こせる |
| 3 | [site/index.html#l03](site/index.html#l03) | SEO / GEO / LLMO / AEO を混ぜずに使える |
| 4 | [site/index.html#l04](site/index.html#l04) | 学習用ボットと検索用ボットを分けて robots.txt を書ける |
| 5 | [site/index.html#l05](site/index.html#l05) | GEO 論文の数字を、実験条件つきで引用できる |
| 6 | [site/index.html#l06](site/index.html#l06) | ページを「引用されうる単位」として直せる |
| 7 | [site/index.html#l07](site/index.html#l07) | インデックス、構造化データ、llms.txt の役割を切り分けられる |
| 8 | [site/index.html#l08](site/index.html#l08) | 測定面と、掲載を止めるスイッチを混同しない |
| 9 | [site/index.html#l09](site/index.html#l09) | よく出回る誤解を一次情報で潰せる |
| 10 | [site/index.html#l10](site/index.html#l10) | 自サイトで点検できる |
| 11 | [site/index.html#l11](site/index.html#l11) | 引用が根拠とは限らないことを、数字つきで言える |
| 復習 | [site/index.html#lr](site/index.html#lr) | 期限の来たカードを、日をあけて思い出す |

用語は画面左の「用語集」、または点線の語にマウスを置くと出ます。Markdown 原文は `curriculum/` です。

## このリポジトリの中身

```
site/                学習用 HTML（ここを開く。index.html は build.py の生成物）
site/_fragments/     各章の本文。ここを直して `python3 site/build.py`
curriculum/          Markdown 原文
glossary.md          用語（HTML 版は site/index.html#lg）
research/SOURCES.md  一次情報の目録
research/sources/    取得した原文
```

二次の解説記事は、用語が市場でどう使われているかの記録として `research/sources/searchengineland-llmo-guide.md` だけ残しています。施策の根拠には使いません。

## さらに読む

教材を終えたあと、原文に進む順です。

1. [Google: Optimizing for generative AI features](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) — Search の生成 AI 面で公式が勧めること／しなくてよいこと。ここから始める。
2. [AI features and your website](https://developers.google.com/search/docs/appearance/ai-features) — 適格条件と query fan-out。
3. [GEO 論文 (arXiv:2311.09735)](https://arxiv.org/abs/2311.09735) — 可視性の定義と実験。数字は §3 の条件とセットで読む。
4. [C-SEO Bench (arXiv:2506.11097)](https://arxiv.org/abs/2506.11097) — 上の追試。競合も同じ手を打つ条件では結果が変わる。3 とセットで読む。
5. [OpenAI crawlers](https://developers.openai.com/api/docs/bots) / [Anthropic crawlers](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler) / [Perplexity crawlers](https://docs.perplexity.ai/docs/resources/perplexity-crawlers) — 学習と検索を分ける一次情報。
6. [llms.txt 仕様](https://llmstxt.org/) — エージェント向け地図。Search の出典選定とは別物だと分かったうえで読む。

## 出典の読み方

本文中の `[出典: …]` は `research/sources/` のファイル、または公式 URL を指します。数字や「必須ではない」といった否定は、必ず原文に当たってください。`research/sources/` は学習用の取得コピーであり、正本は各 URL です。

## この教材がやらないこと

- 特定ベンダーでの掲載を約束する手順書にはしない
- 論文の改善率を、Google AI Overviews の公式効果として扱わない
- 非公開のランキング式を推測して「必勝法」にしない
