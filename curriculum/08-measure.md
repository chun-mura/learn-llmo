# 第 8 課: 測定とコントロール

## この課のゴール

「学習されたくない」「検索の AI 面に出したくない」「通常の青リンクは残したい」を、別スイッチで扱える。測定指標をクリック数だけにしない理由を、Google 自身の文言で言える。

## Google Search（AI Overviews / AI Mode / Discover の生成 AI）

### 測定

公式は次を案内している。

- AI 機能の掲載も Search Console のパフォーマンス（Web 検索タイプ）に含まれる。[出典: AI features and your website]
- Generative AI performance report で、生成 AI 面の見え方を見る。[出典: Google AI optimization guide / Search Console ヘルプ]
- AI Overviews 経由のクリックは滞在が長い、という Google 側の観察。クリック数だけ最適化すると、この面の価値を落とす。[出典: succeeding in AI search, AI features]

2026-06-03 の製品ブログは、生成 AI 面のインプレッションや、どのページがどの国の AI 回答に出たか、の洞察を Search Console に出し始めている、と述べる。展開は段階的。

自前で足すなら、サーバーログの Googlebot、ランディングの直帰ではなく「資料請求・購入・滞在」、ブランドクエリの増減。AI 面からのセッションを Analytics で完全分離できるとは限らない。

### コントロール（3 層。混ぜない）

| スイッチ | 場所 | 止まると | 止まらないもの |
|---|---|---|---|
| Googlebot / `noindex` | robots.txt, meta | Search 全体 | — |
| プレビュー制御 | `nosnippet` 等 | スニペットと AI 面に出る本文量 | インデックス自体（`noindex` 以外） |
| Search generative AI control | Search Console → Settings → Search generative AI | AI Overviews, AI Mode, Discover の生成 AI。接地にも使われない | 通常検索の順位シグナルには使わない。Merchant Center や広告は上書きしない。Search 全体の言語理解には使われうる。**モデル学習は止まらない** |
| Google-Extended | robots.txt のトークン | Gemini アプリと Vertex の学習・接地 | **Search の掲載と順位** |

Search generative AI control の公式注意:

- 既定は掲載する
- 除外すると、他サイトの似た内容は残る。自社だけ沈黙する
- 反映は通常数日、キャッシュで遅れることがある（ヘルプは 1–2 日とも書く）
- 子プロパティは親の設定を継承する。上書きは子の Search Console で行う
- 2026-06 時点では一部サイトオーナー（製品ブログではまず UK）への試験展開

学習だけ止めたいのに生成 AI control を除外する、は取り違えである。

## ChatGPT

掲載のオプトアウトは **OAI-SearchBot**。約 24 時間。ChatGPT-User は検索掲載の判定に使わない。[出典: OpenAI crawlers]

測定は公式コンソールが無い。実務では:

- 対象プロンプトの固定セットを、検索オンで定期実行し、言及・引用 URL・誤情報を記録する
- 紹介文が公式の社名、価格、拠点と一致するか（正確性）
- ログに OAI-SearchBot が来ているか

サンプルサイズと日付を残す。モデルと検索の有無で答えが変わる。

## Claude / Perplexity

同様に、検索ボットの許可と、固定プロンプトの定点観測。Perplexity は回答に番号つき出典が載る製品なので、引用 URL の記録がしやすい。論文もここを実世界エンジンに使った。

ユーザー起動フェッチャを robots.txt で止められるかは第 4 課のとおりベンダー差がある。測定結果が「ブロックしたのに引用された」なら、まず公式の「無視しうる」行に当たる。

## 指標の分け方（最小セット）

1. **技術準備度**: 検索ボットが 200 で本文を取れているか。構造化データが本文と一致するか。これは引用率ではない
2. **言及率**: 固定プロンプトのうち、ブランド名が出た割合
3. **引用率**: 公式ドメインが出典に付いた割合
4. **正確性**: 価格・在庫・拠点の誤り件数
5. **Search Console**: 通常検索と、使えるなら生成 AI レポート

1 を上げても 2 がゼロのことはある。1 が落ちているのに 2 をコンテンツ改稿で取りに行かない。

## 確認問題

1. 「AI に学習されたくないが、AI Overviews には出したい」。どのスイッチを入れ、どれを触らないか。
2. 生成 AI control で除外したあと、通常検索 3 位のまま、という状態は公式説明と矛盾するか。

## 次の課

出回っている誤解。[09-gokai.md](09-gokai.md)
