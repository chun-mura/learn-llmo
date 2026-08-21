# 第 2 課: 生成エンジンの仕組み

## この課のゴール

生成エンジンの処理を、自分で段取りとして書き起こせる。query fan-out が「元クエリの順位」と引用元がずれる理由だと説明できる。

## 共通の骨格

GEO 論文は、当時の BingChat に近い構成を次のように置いた。[出典: GEO 論文 §2.1]

1. クエリ書き換えモデルが、入力を検索しやすい部分クエリに分ける
2. 検索エンジンが文書集合を返す
3. 要約モデルが文書ごとの要約を作る（実装によっては全文を渡す）
4. 応答モデルが、出典つきの一つの回答を書く

論文の実験実装はさらに単純で、Google の上位 5 件を取り、GPT-3.5-turbo に「提供された検索結果だけを使い、文ごとにインライン引用を付けよ」と指示する 2 段階だった。要約ステップは省略している。[出典: GEO 論文 §3.1 および Listing 1]

この骨格は、今の製品でも名前を変えて残っている。Google は生成 AI 機能がコアのランキングシステムでページを取り、その内容を使って回答を接地する（RAG / grounding）と書いている。[出典: Google AI optimization guide]

## Query fan-out

Google は AI Overviews と AI Mode の両方で、query fan-out を使うことがあると明記している。一つのユーザー質問に対し、関連する検索を複数発行し、通常のウェブ検索より多様なリンクを回答に付ける、という説明である。[出典: AI features and your website]

公式ガイドの例: 元クエリが「雑草だらけの芝生の直し方」なら、ファンアウト側は「芝生向けの除草剤」「化学薬品なしで雑草を取る」「雑草の予防」などになりうる。[出典: Google AI optimization guide]

ここから実務で使える帰結は一つだけである。**引用されたページは、元クエリの SERP 上位である必要がない**。ファンアウト先のクエリで強く、かつ回答のその段落を支えられるページが選ばれる余地がある。逆に、元クエリで 1 位でも、回答が必要としている部分クエリを満たさなければ落ちる。

AI Overviews は、通常検索に対して追加価値があると判断されたときだけ出る。常時出る機能ではない。[出典: AI features and your website]

AI Mode と AI Overviews はモデルも手法も異なり、出るリンク集合は一致しない、とも書かれている。同じクエリで両方を見て「どっちが正しい引用か」を決めるのは無意味である。

## 引用が付く理由

生成モデルは、根拠のない文を書く（幻覚）。そのため製品側は、文を検索結果に紐づける制約を入れる。GEO 論文のプロンプトは「すべての文の直後に、その文を完全に支える検索結果のインライン引用を付けよ」とまで書いている。[出典: GEO 論文 Listing 1]

実際の製品の厳密さはこのプロンプトより緩い。出典ボタンの一覧と、文の隣の番号が 1 対 1 でないこともある。それでも、**自己完結していて、検証可能な主張がある塊** は、引用の単位になりやすい、という作業仮説は論文の設計と矛盾しない。

Google はサイト運営者向けに、重要な情報はテキストとして存在する必要がある、と繰り返し書いている。画像や動画は補助であり、テキストが無いと AI 機能の出典にも通常検索にも乗りにくい。[出典: AI features and your website]

## 対話型への拡張

論文の付録は、履歴 \(H = (q_t, r_t)\) を入力にする会話型生成エンジンを定義している。フォローアップ質問の提案は、滞在を伸ばすためでもあり、追加の引用機会でもある。[出典: GEO 論文 Appendix A]

ChatGPT search の発表も、フォローアップで会話全体の文脈を使う、と述べている。[出典: Introducing ChatGPT search]

測定するなら、初回クエリだけでなく、よく出るフォローアップ（比較、価格、手順の次の一歩）に対しても言及を取る。

## 確認問題

1. 自社ページが「元クエリでは 40 位、関連する部分クエリでは 3 位」だとする。fan-out があるエンジンでは、引用候補になりうるか。根拠を課の本文から引け。
2. 論文の実験 GE と、Google の AI Overviews は、検索結果を何件・どのシステムから取るかが違う。この違いが「論文の +40% を Google にそのまま当てはめられない」理由になるか。

## 次の課

名前の整理。[03-yogo.md](03-yogo.md)

## 出典

- GEO 論文 §2.1, §3.1, Listing 1, Appendix A. https://arxiv.org/abs/2311.09735
- Google, AI features and your website. https://developers.google.com/search/docs/appearance/ai-features
- Google, Optimizing for generative AI features. https://developers.google.com/search/docs/fundamentals/ai-optimization-guide
- OpenAI, Introducing ChatGPT search. https://openai.com/index/introducing-chatgpt-search/
