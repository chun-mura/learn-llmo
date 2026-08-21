# 消化メモ（Phase 2）

教材に残す主張だけを、出典つきで残す。通るフィルタは「同じ出典の別箇所でも言っているか」「新しい問題に対して予測できるか」「その分野の公式文書なら誰でも言うか」。

## 残す（2〜3を満たす）

1. **生成エンジンは「検索してから生成する」**。クエリを分解し、文書を取り、LLM が引用つき回答を書く。GEO 論文 §2.1、Google の RAG + query fan-out 説明。
2. **可視性の単位が変わる**。従来 SEO は順位リスト。生成エンジンは回答文中の引用位置・分量・主観的な目立ち方。GEO 論文 §2.2。
3. **学習用クローラと検索用クローラは別**。片方を拒否してももう片方は動く。OpenAI・Anthropic・Perplexity・Google-Extended の公式文書が同じ構造を取る。
4. **Google の AI 機能に出るための追加技術要件はない**。インデックスされ、スニペット表示可能な Search の技術要件を満たせば候補。Google AI features 文書。
5. **Google が公式に勧めるのは SEO の土台と独自コンテンツ**。llms.txt、チャンク分割、AI 向けの書き直し、不自然な言及集めは Google Search では不要と明記。AI optimization guide。
6. **GEO 論文の実験では、統計・引用・引用文の追加が効き、キーワードスタッフィングは効かない**。内部 GE（GPT-3.5 + Google 上位5件）と Perplexity.ai。上限は Position-Adjusted Word Count で約 41%、Subjective Impression で約 28%。下位ページほど相対改善が大きい。
7. **robots.txt は「ユーザー起動の取得」では破られることがある**。Perplexity-User は一般に無視。ChatGPT-User は適用されない場合がある。Anthropic の Claude-User は尊重すると書いている。矛盾は消さない。

## 背景に落とす（1だけ）

- Search Engine Land の LLMO 定義、エンティティ最適化のチェックリスト。用語の流通記録として読む。
- Chrome Lighthouse の llms.txt 監査。任意で、エージェント向け。Search ランキングの話ではない。
- Google の MAU 数字（AI Overviews 25億、AI Mode 10億超）。製品ブログの自己報告。

## 切る

- 「LLMO をやればゼロクリック時代を逆転できる」系のマーケ約束。
- GEO 論文の数字を Google AI Overviews の公式効果として読むこと。実験条件が違う。
- 「構造化データを入れれば AI に引用される」を因果として書くこと。Google は生成 AI 検索に必須ではないと言っている。
- 日本語の代理店記事に出てくる「最初の 40〜60 語」などの数値。一次実験に見当たらない。

## 矛盾（両論を教材に残す）

| 論点 | 一方 | 他方 |
|---|---|---|
| コンテンツ改変は効くか | GEO 論文: 統計・引用・引用文で最大約 40% | Google: GEO/AEO と呼ばれるハックの多くは Search では無効 |
| llms.txt | 提案仕様。Chrome が任意監査。ドキュメントサイトで普及 | Google Search は使わないと明記 |
| ユーザー起動フェッチャと robots.txt | Anthropic: 尊重 | OpenAI: 適用されない場合あり / Perplexity: 一般に無視 |
| Google-Extended | Gemini アプリと Vertex の学習・グラウンディング | Search の AI Overviews 掲載とは別。Search Console の生成 AI 制御とも別 |
