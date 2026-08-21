# 用語集

定義は教材本文と一次情報に合わせた作業用である。法令上の定義ではない。

**AEO (Answer Engine Optimization)**  
質問に対する直接回答面（強調スニペット、AI 概要など）への最適化という業界用語。Google 公式の製品名ではない。

**AI Mode**  
Google Search の対話型生成 AI 面。AI Overviews とモデル・手法が異なり、出るリンクも一致しないと公式が述べる。

**AI Overviews**  
Google Search の結果ページ上の生成概要。通常検索に追加価値があると判断されたときだけ出る。query fan-out を使うことがある。

**ChatGPT-User**  
OpenAI のユーザー起動フェッチャ。自動クロールではない。robots.txt が適用されない場合がある。検索掲載の判定には使わない。

**ClaudeBot / Claude-SearchBot / Claude-User**  
Anthropic の学習 / 検索インデックス / ユーザー起動。robots.txt と Crawl-delay を尊重すると公式が述べる。

**E-E-A-T**  
Experience, Expertise, Authoritativeness, Trustworthiness。Google の品質評価で使う観点の束。それ自体は単一のランキング因子ではない、と公式が書く。

**GEO (Generative Engine Optimization)**  
Aggarwal ら KDD 2024 の枠組み。生成エンジン回答内の可視性を、ブラックボックスなテキスト改変で上げる。

**GEO-bench**  
同論文の約 1 万クエリの評価セット。

**生成エンジン (Generative Engine)**  
検索で文書を取り、LLM が引用つき回答を書くシステム。論文の呼称。

**Google-Extended**  
robots.txt のトークン。Gemini アプリと Vertex の学習・接地。Search の掲載・順位には使わない。独立した User-Agent 文字列はない。

**GPTBot**  
OpenAI の学習用クローラ。検索掲載とは独立。

**grounding / RAG**  
回答を検索インデックス上のページに接地する手法。Google は生成 AI 機能がこれに根ざすと説明する。

**impression（論文）**  
生成回答における出典の可視性。単語数、位置補正単語数、主観印象。

**llms.txt**  
Jeremy Howard 提案の Markdown 地図。エージェント向け。Google Search は使わないと公式が述べる。

**LLMO (Large Language Model Optimization)**  
LLM 製品の回答で言及・引用される状態を改善する実務用語。論文の導入語ではない。

**言及 / 引用**  
言及は回答文に名前が出ること。引用は出典 URL が付くこと。

**noindex / nosnippet**  
インデックス除外 / スニペット（および AI 面のプレビュー）制限。

**OAI-SearchBot**  
ChatGPT search 用のインデックスボット。拒否すると検索回答に出ない（ナビリンクは残る場合あり）。

**PerplexityBot / Perplexity-User**  
検索掲載用 / ユーザー起動。前者は学習用ではない。後者は一般に robots.txt を無視する。

**Position-Adjusted Word Count**  
GEO 論文の主指標の一つ。先頭の引用ほど重い。

**query fan-out**  
一つの質問から複数の関連検索を同時に出すこと。Google 公式用語。

**Search generative AI control**  
Search Console の、生成 AI 面への掲載・接地を止めるトグル。学習オプトアウトではない。展開は段階的。

**SEO**  
検索エンジン向けの発見・理解・掲載の最適化。Google は生成 AI 面でも土台だとする。

**構造化データ**  
JSON-LD 等でページの意味を明示するマークアップ。リッチリザルト用。生成 AI 検索の必須条件ではない。
