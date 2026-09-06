# 第 7 課: 技術的な準備

## この課のゴール

「届く」「意味が付く」「エージェント用の地図」を混ぜずに点検できる。llms.txt を、Google Search 対策として必須視しない。

## 1. 届く（クロールとインデックス）

Google の AI 機能に出典リンクとして出る条件は、通常 Search と同じである。インデックスされ、スニペット表示可能であること。追加要件はない。[出典: AI features and your website]

確認すること:

- Googlebot（および使いたい他社の検索ボット）が robots.txt と CDN/WAF で止まっていない
- 対象 URL が HTTP 200 で本文を返す
- 重要情報が HTML テキストとして存在する。JS だけに閉じない。Google は JS を処理できるが、JS SEO は通常より失敗しやすいと案内している
- 内部リンクで重要ページに辿れる
- 重複 URL を減らし、クロール予算を無駄にしない

Search Console の URL 検査で、Googlebot が見た HTML を確認する。プレビュー制御（`nosnippet` 等）を付けたのに AI 面に本文が出る場合は、ボットが受け取った HTML にそのタグがあるか、再クロール待ちかを見る。[出典: AI features, troubleshooting]

ChatGPT / Perplexity / Claude は第 4 課のボットと IP リスト。WAF の「ボットスコア」一括拒否は、検索用ボットまで落とす。

## 2. プレビュー制御（出す量を制限する）

Search の一覧と AI 面の両方に効く。

- `noindex`: Search 全体から外す。AI 機能の出典にも使えない
- `nosnippet` / `data-nosnippet` / `max-snippet`: プレビューに出すテキスト量

厳しいほど AI 面での出方も細くなる、と 2025-05 の公式ブログは書いている。[出典: succeeding in AI search]

秘密情報は robots.txt だけに頼らない。ユーザー起動フェッチャは robots.txt を無視しうる（第 4 課）。

## 3. 構造化データ（意味のヒント。生成 AI の入場券ではない）

Google は構造化データを、ページ内容の明示的な手がかりとして使い、リッチリザルトの適格化に使う。推奨形式は JSON-LD。schema.org 全体ではなく、Search Central の機能ドキュメントが Search での振る舞いに対する一次情報である。[出典: intro to structured data]

制約:

- マークアップは **そのページに見える内容** と一致させる。見えない正確な情報も付けない
- 空ページに JSON-LD だけ置かない
- 生成 AI 検索のために特別な schema は不要、必須でもない。SEO 全体の一部としては続けてよい。[出典: Google AI optimization guide, Mythbusting]

よく使う型の例（リッチリザルト目的）: `Article`, `FAQPage`, `HowTo`, `Product`, `Organization`, `Person`。FAQ をマークアップするなら、ページ上に同じ Q&A が見えていること。

## 4. llms.txt（提案仕様。Search とは別系統）

Jeremy Howard の提案（v2）。サイトまたはサブパスに Markdown の `/llms.txt` を置き、プロジェクト名（必須の H1）、短い要約、詳細な `.md` へのリンクを載せる。エージェントはまず小さく、必要ならリンク先を取る。ページの Markdown 版は `page.html.md` または拡張子を `.md` にしたもの。発見用に `rel="alternate" type="text/markdown"` と `rel="describedby"`（HTML または HTTP `Link` ヘッダ）。[出典: llmstxt.org v2]

Chrome Lighthouse の agentic browsing 監査は、llms.txt を取得して **サーバーエラーならフラグ、404 なら N/A（任意）**。[出典: Lighthouse llms.txt]

Google Search は llms.txt を使わない、と公式に書いている。OpenAI / Anthropic / Gemini は自社の開発者ドキュメントで llms.txt を公開している、と仕様側は述べる。これは「自社ドキュメントをエージェントに読ませる」用途であり、AI Overviews の順位表ではない。

置く価値があるのは、ドキュメントサイト、API リファレンス、エージェントが手順を踏む必要がある製品である。マーケティングブログ全ページに機械生成の llms.txt を足すのは、仕様の意図（厳選した地図）から外れる。

最小例:

```markdown
# Example Cloud Billing API

> 請求イベントを REST で送受信する。認証は API キー。本番の料金表は /pricing.md。

## Docs

- [Authentication](https://example.com/docs/auth.html.md): API キーとスコープ
- [Error codes](https://example.com/docs/errors.html.md): 4xx/5xx の意味

## Optional

- [Status](https://status.example.com): 障害情報
```

## 5. エージェント向け（余裕があれば）

Google の公式ガイド末尾は、ブラウザエージェントがスクリーンショット・DOM・アクセシビリティツリーを読む、と案内し、[agent-friendly website best practices](https://web.dev/articles/ai-agent-site-ux) と Universal Commerce Protocol に送っている。セマンティック HTML は「完璧である必要はないが、支援技術にもエージェントにも効く」という位置づけである。[出典: Google AI optimization guide]

これは LLMO（回答内引用）より一段先の、操作可能なサイトの話である。混線させない。

## Bing / Copilot の別スイッチ

Google の話をそのまま Bing に持っていくと外す。Bing は 2023-09-22 の [Webmaster Blog](https://blogs.bing.com/webmaster/september-2023/Announcing-new-options-for-webmasters-to-control-usage-of-their-content-in-Bing-Chat) で、既存のメタタグを AI 側の制御に転用すると発表している。

| タグ | Copilot / Bing Chat の回答 | 学習 | 通常の Bing 検索表示 |
|---|---|---|---|
| `NOCACHE` | "may be included in Bing Chat answers. We will only display URL/Snippet/Title" | URL・タイトル・スニペットのみ使われうる | 変わらない |
| `NOARCHIVE` | "will not be included in Bing Chat answers, not be linked to in the answers" | 使わない | 変わらない |

両方あるときは NOCACHE として扱う、と明記されている。

IndexNow は、参加検索エンジンに URL の更新を通知する仕組みで、"submitted URLs will be automatically shared with all other participating search engines" と書かれている。**公式文書に AI 回答との関係の記述は無く、Google も出てこない**。AI 対策として売られている場合、その根拠は一次情報に無い。

## 点検順

1. 200 とテキスト本文と内部リンク
2. 検索用ボットの許可（学習用とは別）
3. スニペット可能か、意図せず `noindex` / `nosnippet` していないか
4. JSON-LD が見える本文と一致するか
5. ドキュメントサイトなら llms.txt と `.md` ミラー

## 確認問題

1. FAQ の JSON-LD だけ正しく、画面上の FAQ が空である。Google の構造化データガイドラインに対して何が問題か。AI Overviews の必須条件を満たさないことか、別の違反か。
2. Lighthouse が llms.txt で N/A を出した。Search の失敗か。

## 次の課

測ると、止める。[08-measure.md](08-measure.md)
