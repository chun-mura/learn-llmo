# 第 4 課: プラットフォーム別の取得と引用

## この課のゴール

学習用クローラと検索・回答用クローラを分けて `robots.txt` を書ける。ユーザー起動のフェッチャが robots.txt を守るかどうかは、会社ごとに違うと説明できる。

## 共通パターン

2024 年以降、主要ベンダーはボットをだいたい次の 3 種に分けている。

| 役割 | 典型的な名前 | 止めたときの意味 |
|---|---|---|
| 学習 | GPTBot, ClaudeBot, Google-Extended | 将来の基盤モデル学習（と、製品によってはアプリ側の接地）から外す |
| 検索インデックス | OAI-SearchBot, Claude-SearchBot, PerplexityBot, Googlebot | その製品の検索・回答の出典候補から外れる（Google は Search 全体） |
| ユーザー起動の取得 | ChatGPT-User, Claude-User, Perplexity-User | 今この質問に答えるためのライブ取得 |

設定は独立である。学習だけ拒否して検索は許可する、が公式に想定されている。

## robots.txt が約束していないこと（RFC 9309）

robots.txt は [RFC 9309](https://www.rfc-editor.org/rfc/rfc9309.html) として標準化されている。読むべきは、そこに書かれていないことである。

- **アクセス認可ではない**。"These rules are not a form of access authorization."（§1.4）。守るかどうかは相手次第
- **用途の区別が無い**。学習か検索かエージェントか、という概念は規格に無い。ベンダーが UA 名を分けて実現しているだけ
- **最長一致**。"The most specific match found MUST be used. The most specific match is the match that has the most octets."（§2.2.2）
- **大小の扱いが逆**。パスの照合は case sensitive（SHOULD, §2.2.2）、UA トークンの照合は case-insensitive（MUST, §2.2.1）
- **4xx と 5xx で振る舞いが逆**。4xx なら "the crawler MAY access any resources on the server."（§2.3.1.3）、5xx なら "the crawler MUST assume complete disallow."（§2.3.1.4）
- キャッシュは 24 時間まで（§2.4）。パーサは最低 500 KiB を読む（§2.5）

秘密の URL を robots.txt で隠すのは筋が悪い、という話がここに繋がる。止めたいものは認証で止める。

## OpenAI

[Overview of OpenAI Crawlers](https://developers.openai.com/api/docs/bots) より。

- **OAI-SearchBot**: ChatGPT の検索結果にサイトを出すためのボット。オプトアウトすると検索回答に出ない。ナビゲーション用リンクとしては残る場合がある。robots.txt の反映は約 24 時間。IP は `https://openai.com/searchbot.json`
- **GPTBot**: 基盤モデルの学習。拒否は「学習に使うな」の合図
- **ChatGPT-User**: ユーザーや Custom GPT の操作に応じた取得。自動クロールではない。**ユーザー起点のため robots.txt が適用されない場合がある**。検索への掲載可否はこれでは決まらず、OAI-SearchBot を使う
- **OAI-AdsBot**: 広告ランディングの検査。学習には使わない

ChatGPT search は 2024-10-31 に公開され、2025-02-05 時点で対象地域では登録なしでも使える、と発表ページに追記されている。検索モデルは GPT-4o のファインチューンで、第三者検索プロバイダと提携コンテンツを使う。[出典: Introducing ChatGPT search]

掲載されたいなら `OAI-SearchBot` を許可する。学習だけ避けたいなら `GPTBot` だけ拒否する。

```
User-agent: GPTBot
Disallow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: ChatGPT-User
Allow: /
```

`ChatGPT-User` を拒否しても、OpenAI は robots.txt を見ない取得がありうると書いている。完全な壁ではない。

## Anthropic

[Help Center のクローラ説明](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler)（ページ上の更新表示: 2026-04-07）より。

| ボット | 用途 | 無効化すると |
|---|---|---|
| ClaudeBot | モデル学習になりうるウェブ収集 | 今後の学習データから外す合図 |
| Claude-User | ユーザー質問に応じたサイト取得 | ユーザー起点のウェブ検索での可視性が下がる |
| Claude-SearchBot | 検索結果の質のためのクロール | 検索用インデックスから外れ、検索回答の精度・可視性が下がる |

Anthropic は次を明記している。

- robots.txt の業界標準ディレクティブを尊重する
- 非標準の `Crawl-delay` をサポートする
- CAPTCHA を迂回しない
- IP ブロックは robots.txt が読めなくなり、オプトアウトが安定しない

OpenAI / Perplexity と違い、**ユーザー起動の Claude-User も robots.txt で止められる** と書いてある。ここはベンダー間で一致しない。

## Perplexity

[Perplexity Crawlers](https://docs.perplexity.ai/docs/resources/perplexity-crawlers) より。反映は最大約 24 時間。

- **PerplexityBot**: 検索結果にサイトを出し、リンクするため。**基盤モデル学習のためのクロールではない**
- **Perplexity-User**: ユーザーの質問に応じてページを取り、回答にリンクするため。学習用ではない。**ユーザーが要求した取得なので、一般に robots.txt を無視する**

WAF でボットをまとめて落としていると、許可したつもりでも届かない。公式は User-Agent と公開 IP（`perplexitybot.json` / `perplexity-user.json`）の両方を見ることを勧めている。

GEO 論文は Perplexity.ai を「実世界の生成エンジン」として使い、内部 GE と同じ方向の改善（引用文・統計）を報告している。キーワードスタッフィングはここでも悪化した。[出典: GEO 論文 §6, Table 5]

## Google

Search の生成 AI 面（AI Overviews, AI Mode）のクロール制御は **Googlebot** である。AI 機能だけ別ボット、ではない。[出典: AI features and your website]

適格条件: インデックスされ、スニペット付きで Search に出せること。**追加の技術要件はない。**

**Google-Extended** は別物である。独立した HTTP User-Agent はなく、既存の Google クローラが robots.txt のトークンだけを見る。影響範囲は Gemini アプリと Vertex AI の Gemini、およびそこでの接地。**Search への掲載や順位には使わない。** [出典: Google's common crawlers]

生成 AI 面だけ掲載を止めたい場合は、Search Console の Search generative AI control が別スイッチになる（第 8 課）。Google-Extended では AI Overviews は止まらない。

プレビューの出し方は `nosnippet` / `data-nosnippet` / `max-snippet` / `noindex`。[出典: AI features and your website, succeeding in AI search]

## 作業例: 方針を一文で決めてから書く

方針: 「学習には使われたくない。ChatGPT・Perplexity・Claude の回答には出典として出てよい。Google Search（AI 含む）も出してよい。」

```
User-agent: GPTBot
Disallow: /

User-agent: ClaudeBot
Disallow: /

User-agent: Google-Extended
Disallow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: Claude-SearchBot
Allow: /

User-agent: PerplexityBot
Allow: /
```

Googlebot は触らない（デフォルト許可）。`Perplexity-User` と `ChatGPT-User` は、公式どおり robots.txt だけでは止まらない／止まらないことがある。秘密のパスは認証と `noindex` で守る。

## 四社の外側

同じ三分類が、他社の公式文書にも出てくる。名前と、公式が明記していることだけ拾う。

| 提供元 | UA | 公式が書いていること |
|---|---|---|
| Meta | Meta-ExternalAgent / Meta-WebIndexer / Meta-ExternalFetcher | 学習・インデックス / Meta AI の検索品質 / ユーザー起動。ExternalFetcher は "may bypass robots.txt rules"。反映は最大 24 時間 |
| Apple | Applebot-Extended | 生成モデルの学習利用だけを制御する。"Applebot-Extended does not crawl webpages."。拒否しても検索結果には残る |
| Amazon | Amazonbot / Amzn-SearchBot / Amzn-User | Amazonbot は学習に使われうる。ページ単位の `noarchive` で学習から外せる。robots.txt のキャッシュは最大 30 日 |
| Mistral | MistralAI-Training / -Index / -User | 学習用だけが生成 AI 学習に使われる。残り二つは学習に使わないと明記 |
| DuckDuckGo | DuckAssistBot | AI 回答用のライブ取得。"This data is not used in any way to train AI models."。反映は 72 時間。検索順位には影響しない |
| Common Crawl | CCBot | 公開アーカイブ用。なりすましがあるため UA だけで判定しない。IP は `https://index.commoncrawl.org/ccbot.json` |

Bytespider（ByteDance）は、到達可能な公式ドキュメントを確認できなかった。robots.txt の遵守についても一次情報が無い。**未確認**として扱う。

## robots.txt の外側で動いているもの

「用途を書けない」という RFC の穴を、二方向から埋めようとしている。どちらもまだ標準ではない。

- **IETF aipref WG**。`Content-Usage` を HTTP レスポンスヘッダと robots.txt の双方に付け、取得と利用を二段に分ける。draft-ietf-aipref-attach は **Internet-Draft** であり RFC ではない（Proposed Standard 志向）
- **Cloudflare**。ボットを Search / Agent / Training に分類し、2026-09-15 から、新規に載せるドメインの広告掲載ページで Training と Agent を既定でブロックする（Search は許可のまま）。robots.txt 用の `Content-Signal:` ディレクティブも出している（例: `Content-Signal: search=yes,ai-train=no`）

実務の含意は一つ。自分が robots.txt に何も書いていなくても、CDN 側の既定でブロックが入ることがある。「許可したつもり」を確かめる先が増えた。

## 確認問題

1. `User-agent: GPTBot` と `Disallow: /` だけ書いたサイトが ChatGPT search に出ない、は正しい推論か。
2. Google-Extended を拒否したのに AI Overviews に出るのはバグか。

## 次の課

論文の実験を、条件つきで読む。[05-geo-paper.md](05-geo-paper.md)
