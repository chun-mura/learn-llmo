# 第 5 課: GEO 論文を読む

## この課のゴール

「最大 40%」を、指標名・エンジン・改変対象つきで引用できる。限界節を読んだうえで、自社に使うかどうかを決められる。

論文: Pranjal Aggarwal, Vishvak Murahari, Tanmay Rajpurohit, Ashwin Kalyan, Karthik Narasimhan, Ameet Deshpande. *GEO: Generative Engine Optimization*. KDD 2024. arXiv:2311.09735。コードと GEO-bench は著者リポジトリ [GEO-optim/GEO](https://github.com/geo-optim/geo)。

## 何を測ったか

従来 SEO の「平均順位」は、回答が一つの散文で出典が文中に散らばる生成エンジンには使えない。論文は impression を定義した。[出典: §2.2]

- **Word Count**: その出典に紐づく文の単語数の割合
- **Position-Adjusted Word Count**: 先頭の文ほど指数的に重くする。検索の CTR が上位に偏る観察に倣っている
- **Subjective Impression**: 関連性、影響、独自性、主観的な位置と分量、クリックしやすさ、多様性。G-Eval 流に LLM で採点し、較正が悪いので Position-Adjusted Word Count と同じ平均・分散に正規化している

改善率は、同じクエリで **ソースの 1 つだけ** を改変した前後の相対差である。改変するソースはクエリごとにランダムだが、手法間では固定。

## 実験エンジン

内部 GE: 各クエリについて Google 上位 5 件を取り、gpt-3.5-turbo、temperature 0.7 で 5 回生成。プロンプトは「検索結果だけを使え。文の直後に引用を付けよ」。[出典: §3.1]

実世界チェック: Perplexity.ai。[出典: §6]

ベンチマーク GEO-bench: 約 1 万クエリ（train 8k / val 1k / test 1k）。MS MARCO、ORCAS-1、Natural Questions に加え、All Souls の論述、LIMA、ディベート、Perplexity Discover、ELI5、GPT-4 生成クエリ。情報検索 80%、トランザクションとナビゲーション 10% ずつ、と書いている。ドメインタグは GPT-4 で付け、テスト分割は人手確認だが、Limitation でタグのノイズを認めている。

## 9 つの改変

LLM に指示してソース HTML テキストを書き換える。3, 4, 5 以外は既存文の見せ方を変えるだけで、新しい事実は必須ではない、と著者は述べる。4 と 5 とキーワード追加は追加コンテンツが要ることがある。[出典: §2.2.2]

| 手法 | 何をするか |
|---|---|
| Authoritative | 説得的・権威的な文体 |
| Statistics Addition | 定性を定量に置き換えられる箇所へ統計を足す |
| Keyword Stuffing | クエリの語を増やす（古典 SEO） |
| Cite Sources | 信頼できる出典を足す |
| Quotation Addition | 信頼できる引用文を足す |
| Easy-to-Understand | 言い回しを易しくする |
| Fluency Optimization | 流暢さを上げる |
| Unique Words | 独特な語を足す |
| Technical Terms | 専門用語を足す |

## 結果（内部 GE）

Table 1 の読み方。ベースライン（改変なし）の Overall Position-Adjusted Word Count は 19.3。トップ手法の相対改善は、同節の本文で Position-Adjusted Word Count 約 41%、Subjective Impression 約 28%。[出典: Table 1 キャプションと §4]

絶対スコア（Overall / Subjective Average）の概数:

| 手法 | Overall | Subjective 平均 | 論文の位置づけ |
|---|---|---|---|
| 改変なし | 19.3 | 19.3 | ベースライン |
| Keyword Stuffing | 17.7 | 20.2 | 非パフォーマンス。単語数系は悪化 |
| Unique Words | 20.5 | 20.4 | 弱い |
| Easy-to-Understand | 22.0 | 20.5 | 中程度 |
| Authoritative | 21.3 | 22.9 | 文体。主観は上がるが全体は限定的 |
| Technical Terms | 22.7 | 21.4 | 中程度 |
| Fluency Optimization | 24.7 | 21.9 | 高 |
| Cite Sources | 24.6 | 21.9 | 高 |
| Statistics Addition | 25.2 | 23.7 | 高 |
| Quotation Addition | 27.2 | 24.7 | 最高 |

本文の要約:

- 統計・引用文・出典追加が 30–40%（位置補正単語数）と 15–30%（主観）
- 流暢さ・分かりやすさだけでも 15–30%
- 権威的トーンは「指示に従うモデルなら効きそう」だが、有意な押し上げはなかった
- キーワードスタッフィングは生成エンジンではほぼ効かない

Table 2: 検索順位が低いソースほど GEO の相対改善が大きい。Cite Sources は 5 位ソースで +115.1%、1 位ソースは −30.3%。著者が「小規模サイトの民主化」と呼ぶ根拠。ただしこれは **すでに上位 5 件に入っている 5 位** の話であり、圏外ページの話ではない。

Table 3: 手法とドメインの相性。Cite Sources は事実・法令、Statistics は法令・ディベート・意見、Quotation は社会・説明・歴史、Authoritative はディベート・歴史・科学。

組み合わせ（テスト 200 件のサブセット、コスト制約）: Fluency + Statistics が単体より 5.5% 以上良い。Cite Sources は単体より組み合わせで伸びる。[出典: §5.3。数値は Table 1 と一致させないこと]

## Perplexity.ai（Table 5）

Position-Adjusted Word Count / Subjective Impression:

- 改変なし: 24.1 / 24.7
- Keyword Stuffing: 21.9 / 28.1（単語数系は悪化、主観は上がる）
- Quotation Addition: 29.1 / 32.1（位置補正で約 +22%）
- Statistics Addition: 26.2 / 33.9（主観で約 +37%）

本文は Cite Sources も最大 9% と 37% の改善に触れる。内部 GE と同じ方向で、キーワード詰め込みは再び弱い。

## 限界（§9）を先に使う

著者自身が書いている制約:

- エンジンが変われば手法も更新が要る（SEO と同じ）
- クエリ分布は将来変わる
- GEO 改変が **従来検索の順位** に与える影響は、検索アルゴリズムがブラックボックスのため未評価。テキスト中心の変更でバックリンク等は触っていない、という推測のみ
- コンテキストが長くなれば取り込めるソース数が増え、検索順位の影響は下がるだろう、という予想
- タグは主観と誤ラベルがありうる

加えて、教材側で明示する条件:

- 内部 GE は 2024 年の gpt-3.5-turbo と Google 上位 5 件
- 可視性は著者が定義した impression であり、クリックや売上ではない
- Google 公式は、この種の GEO ハックの多くを Search では無効と述べている（第 3 課）

## 追試（C-SEO Bench, NeurIPS 2025）

GEO 論文は「他が動かないときに 1 者が動いたら」を測っている。競合も同じ手を打つ状況は測っていない。

C-SEO Bench（Puerto, Gubri, Green, Oh & Yun, NeurIPS 2025 Datasets & Benchmarks / [arXiv:2506.11097](https://arxiv.org/abs/2506.11097)）は、そこに二つの条件を足した。

- 質問応答と商品推薦の 2 タスク × 各 3 ドメイン
- 競合も同じ手法を採用していく状況（採用率を変える）

結果は "most current C-SEO methods are not only largely ineffective but also frequently have a negative impact on document ranking"。従来の SEO 的手法のほうが有効で、採用が広がるほど混雑しゼロサムに近づく、とも書いている。

GEO 論文が間違っていた、という読み方はしない。条件が違う。実務が置かれているのは C-SEO Bench 側の条件である。社内で GEO の数字を引くときは、実験条件とこの追試をセットで言う。

## 確認問題

1. 「引用を足したら 115% 上がる」を、誰のどの順位のソースの、どの指標の話か、に直して書け。
2. Keyword Stuffing の Subjective が Perplexity で上がっている。位置補正単語数は下がっている。どちらを「効いた」と呼ぶべきか。論文の主指標はどれか。

## 次の課

ページの中身。[06-content.md](06-content.md)
