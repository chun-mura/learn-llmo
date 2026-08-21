# 第 1 課: LLMO とは何か

## この課のゴール

「LLMO は何を最適化するのか」を、SEO の順位と混ぜずに説明できる。

## 何が変わったか

従来の検索エンジンは、クエリに対して **ページのリスト** を返す。クリックされなければ、中身は読まれない。生成エンジン（Generative Engine）は、複数のページから文を組み立てて **一つの回答** を返し、途中に出典リンクを埋め込む。

Aggarwal らはこの仕組みを次のように定式化した。生成エンジンはユーザークエリを受け取り、検索で文書を取り、生成モデルが引用つきの自然言語応答を返す。ユーザーの利便は上がるが、サイト運営者は「何位に出たか」ではなく「回答のどの文が自分のページに紐づいたか」を見ることになる。[出典: GEO 論文 Abstract および §1]

OpenAI は 2024-10-31 に ChatGPT search を公開し、回答にウェブ上の出典リンクを付ける形にした。検索は会話の流れで自動的に走ることも、ユーザーが明示することもできる。裏側はファインチューンした GPT-4o と、第三者の検索プロバイダおよび提携メディアのコンテンツだと説明している。[出典: Introducing ChatGPT search]

Google は AI Overviews と AI Mode を、通常の Search の延長として位置づけている。2026-06-03 の製品ブログでは、AI Overviews の月間アクティブユーザーを 25 億超、AI Mode を 10 億超と自己報告している。数字の第三者検証は公開されていない。[出典: New opportunities, control and insights for website owners]

## LLMO という名前

**LLMO** は Large Language Model Optimization の略で、生成 AI の回答の中で自社が言及・引用される状態を改善する、という実務用語である。英語圏の業界記事でも同じ略語が使われる。[出典: Search Engine Land の LLMO ガイド。流通記録であり実験ではない]

学術側の導入語は **GEO（Generative Engine Optimization）** である。論文の目的は「クローズドな生成エンジンに対して、サイト運営者がブラックボックス最適化で可視性を上げる枠組み」を置くことだった。[出典: GEO 論文 Abstract]

実務では同じ棚に、次のラベルも並ぶ。

- **AEO**（Answer Engine Optimization）: 質問に直接答える面。強調スニペット時代からの言い回しが残っている
- **AIO**: 文脈によって AI Optimization 全体、または Google の AI Overviews だけを指す

Google の公式ガイドは、AEO や GEO という呼び方自体を否定はしないが、Search の生成 AI 面で効くとされる「ハック」の多くは、実際の仕組みと一致しないと書いている。[出典: Google AI optimization guide, Mythbusting]

呼び方を統一する必要はない。会話では相手が使う語に合わせ、社内では **言及**（ブランド名が出る）と **引用**（URL が出典として付く）を分けて測る方が混線しない。

## SEO との関係

SEO は、クロールされ、インデックスされ、クエリに対してページが選ばれるまでの最適化である。生成エンジンのうち Google の AI 機能は、同じ Search インデックスからページを取り出す（RAG / grounding）。ページが Search に出る資格がなければ、AI Overviews の出典候補にもならない。[出典: AI features and your website]

LLMO は SEO の代替ではない。土台（取得できる、本文がある、独自の情報がある）の上に、回答面での観測と、サービスごとのクローラ方針が乗る。

ChatGPT や Perplexity は Google のインデックスとは別の取得経路を持つ。こちらは第 4 課で扱う。

## 可視性の単位

検索結果では「何位か」が可視性の近似になる。生成回答では、同じ URL でも次が変わる。

- 回答の先頭付近で引用されるか、末尾か
- 何文が自分のページに紐づくか
- ユーザーがリンクを辿りそうか

GEO 論文はこれを impression（可視性）と呼び、単語数、位置補正した単語数、主観的な印象の束で測った。[出典: GEO 論文 §2.2]

実務の観測では、少なくとも次を分けて記録する。

1. **取得された**（クローラや検索がページに届いた）
2. **言及された**（回答文にブランド名がある。リンクは無いこともある）
3. **引用された**（出典 URL が付いている）

1 は 3 の前提だが、1 でも 3 にならないことは普通にある。Google も、query fan-out で裏で読んだページが、画面上のリンク集合と一致するとは限らない書き方をしている。[出典: AI features and your website]

## 確認問題

1. 「自社サイトが Google で 3 位なのに ChatGPT に出ない」は、LLMO の失敗か、別経路の問題か。何を調べれば切り分けられるか。
2. 言及と引用の違いを、自分のブランド名で一文ずつ書け。

答えの指針は [第 10 課](10-enshu.md) にある。

## 次の課

生成エンジンがクエリをどう分解し、どの文書を読み、どう引用を付けるか。[02-seisei-engine.md](02-seisei-engine.md)

## 出典

- Aggarwal et al., GEO: Generative Engine Optimization, KDD 2024. https://arxiv.org/abs/2311.09735
- OpenAI, Introducing ChatGPT search, 2024-10-31. https://openai.com/index/introducing-chatgpt-search/
- Google, AI features and your website. https://developers.google.com/search/docs/appearance/ai-features
- Google, Optimizing your website for generative AI features. https://developers.google.com/search/docs/fundamentals/ai-optimization-guide
- Google, New opportunities, control and insights for website owners, 2026-06-03. https://blog.google/products-and-platforms/products/search/new-controls-website-owners/
