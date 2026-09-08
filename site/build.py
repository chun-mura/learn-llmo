import html
import json
import random
import re
from pathlib import Path

ROOT = Path(__file__).parent
FRAG = ROOT / "_fragments"
OUT = ROOT / "lessons"
OUT.mkdir(exist_ok=True)

# (題、この章のゴール、先出しの問い)
# 先出しの問いは、読む前に一度自分で答えさせるためのもの。当たらなくてよい。
META = {
    "01": (
        "LLMO とは何か",
        "「何を最適化するのか」を、SEO の順位と混ぜずに言える。",
        "「AI に載る」と言うとき、あなたは何が変わった状態を指していますか。順位という言葉を使わずに一文で。",
    ),
    "02": (
        "生成エンジンの仕組み",
        "処理の段取りを書き起こせる。fan-out で引用元がずれる理由を言える。",
        "ChatGPT に質問してから回答が出るまで、裏で何段階あると思いますか。思いつく順に並べてください。",
    ),
    "03": (
        "SEO · GEO · LLMO · AEO",
        "四つの略語を対象面で使い分けられる。Google が Search で SEO と言う範囲を言える。",
        "SEO・GEO・LLMO・AEO のうち、論文で定義された語はどれですか。",
    ),
    "04": (
        "ボットを分ける",
        "学習用と検索用を分けて robots.txt を書ける。ユーザー起動フェッチャーとの差を言える。",
        "robots.txt で GPTBot を拒否したサイトは、ChatGPT の検索回答に出なくなりますか。",
    ),
    "05": (
        "GEO 論文を読む",
        "「最大 40%」を、指標・エンジン・改変対象つきで引用できる。追試の結果も添えられる。",
        "「GEO で可視性が最大 40% 上がる」。この一文に足りない条件を、思いつくだけ挙げてください。",
    ),
    "06": (
        "中身が引用される条件",
        "対象エンジンを決めたうえで、ページを答えの材料として直せる。",
        "自社ページの一段落を思い浮かべてください。そこに数値・日付・出典はありますか。",
    ),
    "07": (
        "技術的な準備",
        "届く・意味が付く・エージェント用地図を混ぜずに点検できる。",
        "構造化データを入れると AI に引用されやすくなる。○か×か。理由も一言で。",
    ),
    "08": (
        "測定とコントロール",
        "学習・AI 面・通常の検索結果を、別の設定として扱える。何が測れて何が測れないかを言える。",
        "Search Console の生成 AI レポートで、クリック数は見られると思いますか。",
    ),
    "09": (
        "よくある誤解",
        "一次情報で止められる誤解を、自分の言葉で潰せる。",
        "あなたが最近見た「LLMO 対策」の主張を一つ思い出してください。出典は付いていましたか。",
    ),
    "10": (
        "演習",
        "自サイト（または架空の店）で点検できる。",
        "いまの自分は、第 1 章から第 9 章のどれを一番あいまいに覚えていますか。",
    ),
    "11": (
        "引用は根拠とは限らない",
        "引用が付いていても根拠とは限らないことを、論文の数字つきで言える。操作の限界も言える。",
        "AI の回答に出典リンクが付いていました。その文はその出典から書かれた、と言い切れますか。",
    ),
}


# --- 用語辞書 ---
# _fragments/terms.json が唯一の定義元。ここから用語集ページ、マウスオーバー用の
# 辞書、本文の自動マーキングの三つを作る。

TERMS_PATH = FRAG / "terms.json"
TERMS = json.loads(TERMS_PATH.read_text(encoding="utf-8")) if TERMS_PATH.exists() else {}

# 長い表記から先に当てる。「C-SEO Bench」を「SEO」で切らないため。
TERM_MATCHES = sorted(
    [(name, name) for name in TERMS]
    + [(alias, name) for name, spec in TERMS.items() for alias in spec.get("aliases", [])],
    key=lambda pair: len(pair[0]),
    reverse=True,
)

# 先頭 1 文字で候補を絞る。TERM_MATCHES は長い表記が先に並んでいる。
TERM_BY_HEAD = {}
for _surface, _canonical in TERM_MATCHES:
    TERM_BY_HEAD.setdefault(_surface[0], []).append((_surface, _canonical))

# 自動マーキングを止める範囲。出典・コード・見出し・表・想起カードには付けない。
SKIP_TAGS = ("code", "pre", "h2", "h3", "details", "card", "table")
TAG_RE = re.compile(r"<[^>]+>")
WORDISH = re.compile(r"[A-Za-z0-9._-]")


def mark_terms(text, seen):
    """地の文を左から一度だけ走査し、その節での初出 1 回に span を付ける。
    付けた span の中は読み直さない。「C-SEO Bench」の中の「C-SEO」のような
    入れ子のマーキングを避けるため。"""
    out = []
    i = 0
    size = len(text)
    while i < size:
        hit = None
        for surface, canonical in TERM_BY_HEAD.get(text[i], ()):
            if canonical in seen or not text.startswith(surface, i):
                continue
            after = text[i + len(surface)] if i + len(surface) < size else " "
            before = text[i - 1] if i else " "
            # 英数字の語の途中（C-SEO の中の SEO など）には付けない
            if WORDISH.match(surface[0]) and (WORDISH.match(before) or WORDISH.match(after)):
                continue
            hit = (surface, canonical)
            break
        if hit:
            surface, canonical = hit
            out.append(f'<span data-term="{html.escape(canonical, quote=True)}">{surface}</span>')
            seen.add(canonical)
            i += len(surface)
        else:
            out.append(text[i])
            i += 1
    return "".join(out)


def autolink_terms(fragment):
    """節（section.step）ごとに、地の文の用語へ data-term を付ける。"""
    if not TERM_MATCHES:
        return fragment
    parts = []
    seen = set()
    skip_depth = 0
    in_marked_span = 0
    pos = 0
    for m in TAG_RE.finditer(fragment):
        text = fragment[pos : m.start()]
        tag = m.group(0)
        parts.append(text if (skip_depth or in_marked_span) else mark_terms(text, seen))
        parts.append(tag)
        pos = m.end()

        body = tag[1:-1].strip()
        closing = body.startswith("/")
        name = body.lstrip("/").split()[0].lower() if body.lstrip("/").split() else ""
        if 'class="step"' in tag:
            seen = set()
        if "data-term=" in tag and not closing:
            in_marked_span += 1
            # 手で付けてある用語も、その節では既出として扱う
            existing = re.search(r'data-term="([^"]+)"', tag)
            if existing:
                seen.add(existing.group(1))
        elif name == "span" and closing and in_marked_span:
            in_marked_span -= 1
        elif name in SKIP_TAGS and not body.endswith("/"):
            skip_depth = max(skip_depth + (-1 if closing else 1), 0)
    tail = fragment[pos:]
    parts.append(tail if (skip_depth or in_marked_span) else mark_terms(tail, seen))
    return "".join(parts)


def glossary_html():
    """用語集ページ。terms.json が無いときは従来の静的な用語集を使う。"""
    if not TERMS:
        return GLOSSARY_STATIC
    rows = "\n".join(
        f"            <dt>{html.escape(name)}</dt><dd>{html.escape(spec.get('long') or spec['short'])}</dd>"
        for name, spec in TERMS.items()
    )
    head, rest = GLOSSARY_STATIC.split("<dl ", 1)
    attrs, body = rest.split(">", 1)
    return f'{head}<dl {attrs}>\n{rows}\n      </dl>{body.split("</dl>", 1)[1]}'


def terms_script():
    """マウスオーバー用の辞書を learn.js へ渡す。"""
    data = {name: spec["short"] for name, spec in TERMS.items()}
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    return f"  <script>window.LLMO_TERMS = {payload};</script>\n"


HEAD = """<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>LLMO を思い出しながら読む</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=BIZ+UDPGothic:wght@400;700&family=Fragment+Mono&family=Shippori+Mincho:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/learn.css">
{{terms}}</head>
<body class="desk" data-lesson="00">
  <a class="skip" href="#stage">本文へ</a>
  <aside class="rail" data-rail>
    <a class="rail-brand" href="#l00">LLMO 教材<strong>思い出して覚える</strong></a>
    <nav aria-label="章の順">
    <ol>
      <li><a href="#l01"><span class="num">01</span><span>何を最適化するか</span></a></li>
      <li><a href="#l02"><span class="num">02</span><span>検索してから書く</span></a></li>
      <li><a href="#l03"><span class="num">03</span><span>SEO GEO LLMO AEO</span></a></li>
      <li><a href="#l04"><span class="num">04</span><span>学習と検索は別</span></a></li>
      <li><a href="#l05"><span class="num">05</span><span>数字の条件</span></a></li>
      <li><a href="#l06"><span class="num">06</span><span>引用される単位</span></a></li>
      <li><a href="#l07"><span class="num">07</span><span>届く・意味・地図</span></a></li>
      <li><a href="#l08"><span class="num">08</span><span>スイッチを混ぜない</span></a></li>
      <li><a href="#l09"><span class="num">09</span><span>一次情報で止める</span></a></li>
      <li><a href="#l10"><span class="num">10</span><span>手を動かす</span></a></li>
      <li><a href="#l11"><span class="num">11</span><span>引用は根拠ではない</span></a></li>
    </ol>
    </nav>
    <div class="rail-foot"><a class="rail-review" href="#lr">復習</a><a href="#lg">用語集</a></div>
  </aside>
  <div class="stage" id="stage">
"""

HOME = """
    <section class="view is-on" id="l00" data-view="00">
      <div class="home-hero">
        <p class="kicker">調査日 2026-08-21 · 追補 2026-09-06 · 一次情報のみ</p>
        <h1>読むより、思い出す</h1>
        <p>Markdown の長文を、机の上の教科書に組み直したものです。各章は節に切ってあり、次へを押すまで次の節は出ません。節の終わりには、閉じた状態の問いが 1 枚ずつ入っています。</p>
        <div class="dash" data-dash></div>
        <div class="boxes" data-boxes></div>
        <p><a class="btn" href="#l01">第 1 章から始める</a></p>
      </div>
      <div class="pair" style="max-width:42rem">
        <div class="seal paper"><small>朱 · 論文</small>GEO（KDD 2024）。すでに検索上位に入ったページを、生成が厚く引用するか。追試の C-SEO Bench（NeurIPS 2025）もここに入ります。</div>
        <div class="seal official"><small>藍 · 公式</small>Google Search。入場条件はインデックスとスニペット。SEO の土台が先。ベンダー各社のクローラー方針もここ。</div>
      </div>
      <p style="max-width:42rem">論文と公式は同じ「AI に載せる」を指していても、見ている層が違います。混ぜないことが、この教材の核です。</p>
      <nav class="path" id="path" aria-label="章の順">
        <a href="#l01"><span class="n">01</span><strong>LLMO とは何か</strong><em>何を最適化するか</em></a>
        <a href="#l02"><span class="n">02</span><strong>生成エンジン</strong><em>検索してから書く</em></a>
        <a href="#l03"><span class="n">03</span><strong>用語の地図</strong><em>SEO GEO LLMO AEO</em></a>
        <a href="#l04"><span class="n">04</span><strong>ボットを分ける</strong><em>学習と検索は別</em></a>
        <a href="#l05"><span class="n">05</span><strong>GEO 論文</strong><em>数字の条件と追試</em></a>
        <a href="#l06"><span class="n">06</span><strong>中身</strong><em>引用される単位</em></a>
        <a href="#l07"><span class="n">07</span><strong>技術</strong><em>届く · 意味 · 地図</em></a>
        <a href="#l08"><span class="n">08</span><strong>測定</strong><em>スイッチを混ぜない</em></a>
        <a href="#l09"><span class="n">09</span><strong>誤解</strong><em>一次情報で止める</em></a>
        <a href="#l10"><span class="n">10</span><strong>演習</strong><em>手を動かす</em></a>
        <a href="#l11"><span class="n">11</span><strong>引用と根拠</strong><em>引用は根拠ではない</em></a>
      </nav>
      <div class="method" style="max-width:42rem">
        <h2>この作りにした理由</h2>
        <p>読み返す量を増やすより、閉じた状態から思い出す回数を増やすほうが、あとで残ります。練習テストは 272 件のメタ分析で再読その他すべての比較条件を上回りました（g = 0.61）。</p>
        <ul class="plain">
          <li><strong>正誤は答え合わせを押すまで出しません。</strong>選択肢から選ぶ形ですが、先に自分の言葉で答えを言い切ってから選んでください。自分で答えを作るほうが、選ぶだけよりも残ります（生成効果のメタ分析で d ≈ 0.40）。選択式は再認なので、この効果の分は割り引いて考えてください。</li>
          <li><strong>復習の間隔は 1 → 3 → 7 → 16 → 35 日と広げます。</strong>間隔をあけるほど長く残るという分散学習の結果に沿わせています。</li>
          <li><strong>復習は章をまたいで混ぜます。</strong>ただし交互配置の効果量は中程度で、条件によって反転します。順序の工夫として使います。</li>
          <li><strong>進捗の主指標は「読んだ節」ではなく「間をあけて言えたカード」です。</strong>読めた感じは、覚えた証拠になりません。</li>
          <li><strong>やらないこと</strong>：学習タイプ別モード（効果の根拠がない）、忘却曲線の飾り図（よく描かれる滑らかな指数曲線は原データの単純化）、独自の高度な復習アルゴリズム（人を対象にした比較試験が乏しい）。</li>
        </ul>
        <details class="source"><summary>出典</summary>
          <ul>
            <li>Adesope, Trevisan &amp; Sundararajan 2017, <em>Review of Educational Research</em> 87(3)（練習テストのメタ分析、g = 0.61）</li>
            <li>Dunlosky et al. 2013, <em>Psychological Science in the Public Interest</em> 14(1)（練習テストと分散学習が high utility、再読・ハイライトは low utility）</li>
            <li>Cepeda et al. 2006, <em>Psychological Bulletin</em> 132(3) / 2008, <em>Psychological Science</em> 19(11)（分散学習と最適間隔）</li>
            <li>Bertsch et al. 2007, <em>Memory &amp; Cognition</em> 35(2)（生成効果 d ≈ 0.40）</li>
            <li>Brunmair &amp; Richter 2019, <em>Psychological Bulletin</em> 145(11)（交互配置 g = 0.42、条件依存）</li>
            <li>Koriat &amp; Bjork 2005, <em>JEP:LMC</em> 31(2)（流暢性の錯覚）</li>
            <li>Pashler et al. 2008, <em>PSPI</em> 9(3)（学習スタイルの根拠なし）／ Murre &amp; Dros 2015, <em>PLOS ONE</em> 10(7)（忘却曲線の再現）</li>
          </ul>
        </details>
      </div>
      <p class="note home-note">キーボード: J / 右で次の節、K / 左で戻る、A で全部表示。復習面では 1〜4 で選択肢を選び、Space で答え合わせ、もう一度 Space で次のカードへ。進捗はこのブラウザーにだけ残ります。</p>
    </section>
"""

REVIEW = """
    <section class="view review" id="lr" data-view="r" hidden>
      <header class="lesson-head">
        <p class="kicker">復習</p>
        <h1>間をあけて思い出す</h1>
        <p class="goal"><span>ここで起きること</span>期限が来たカードだけを、章をまたいで混ぜて出します。正解したカードは次の間隔が伸び、外したカードはこの回の終わりにもう一度出ます。</p>
      </header>
      <p class="chunk-meter" data-review-meter></p>
      <div data-review-slot></div>
      <div class="review-empty" data-review-empty hidden>
        <p data-review-done></p>
        <p><a class="btn" href="#l00">机に戻る</a></p>
      </div>
    </section>
"""

GLOSSARY_STATIC = r"""
    <section class="view" id="lg" data-view="g" hidden>
      <header class="lesson-head">
        <p class="kicker">付録</p>
        <h1>用語集</h1>
        <p class="goal"><span>使い方</span>作業用の定義です。法令上の定義ではありません。点線の語にマウスを置くと同じ説明が出ます。</p>
      </header>
      <dl class="dl" style="max-width:38rem">
        <dt>AEO</dt><dd>質問に対する直接回答面への最適化という業界用語。Google の製品名ではない。</dd>
        <dt>AI Mode / AI Overviews</dt><dd>Google Search の生成 AI 面。両者はモデルも手法も違い、出るリンクも一致しない。Overviews は追加価値があるときだけ出る。</dd>
        <dt>Amazonbot / Amzn-SearchBot / Amzn-User</dt><dd>Amazon の収集 / 検索 / ユーザー起動。Amazonbot は学習に使われうる。ページ単位の <code>noarchive</code> で学習から外せる。</dd>
        <dt>Applebot-Extended</dt><dd>Apple の学習利用だけを制御する二次トークン。自身はクロールしない。拒否しても検索結果には残る。</dd>
        <dt>C-SEO Bench</dt><dd>Puerto ら NeurIPS 2025 のベンチマーク。競合下では多くの C-SEO 手法が無効か逆効果だったと報告。</dd>
        <dt>CCBot</dt><dd>Common Crawl のクローラー。公開アーカイブ用。なりすましがあるため UA だけで判定しない。</dd>
        <dt>ChatGPT-User</dt><dd>ユーザー起動の取得。robots.txt が適用されない場合がある。検索掲載の判定には使わない。</dd>
        <dt>ClaudeBot / SearchBot / User</dt><dd>Anthropic の学習 / 検索 / ユーザー起動。robots.txt を尊重すると公式が述べる。</dd>
        <dt>Content-Signal</dt><dd>Cloudflare が提案する robots.txt のディレクティブ。search / ai-input / ai-train の可否を書く。</dd>
        <dt>Content-Usage</dt><dd>IETF aipref が定義中の利用意向フィールド。HTTP ヘッダと robots.txt の両方に付ける。Internet-Draft であり RFC ではない。</dd>
        <dt>DuckAssistBot</dt><dd>DuckDuckGo の AI 回答用。学習には使わないと明記。反映は 72 時間。拒否しても検索順位に影響しない。</dd>
        <dt>E-E-A-T</dt><dd>経験・専門性・権威性・信頼性。単一のランキング因子ではない。</dd>
        <dt>faithfulness</dt><dd>引用がその文書を実際に根拠にしているか。引用が正しく見えることとは別。</dd>
        <dt>GEO</dt><dd>Generative Engine Optimization。KDD 2024 の枠組み。</dd>
        <dt>Google-Extended</dt><dd>Gemini アプリと Vertex の学習・接地。Search の掲載・順位には使わない。</dd>
        <dt>GPTBot</dt><dd>OpenAI の学習用。検索掲載とは独立。</dd>
        <dt>grounding / RAG</dt><dd>検索で取ったページに回答を接地する。</dd>
        <dt>impression</dt><dd>論文の可視性。単語数、位置補正単語数、主観印象。</dd>
        <dt>IndexNow</dt><dd>参加検索エンジンに URL の更新を通知する仕組み。公式文書に AI 回答との関係の記述はなく、Google も出てこない。</dd>
        <dt>llms.txt</dt><dd>エージェント向けの Markdown 地図。Google Search は使わない。</dd>
        <dt>LLMO</dt><dd>LLM の回答で言及・引用される状態を改善する実務用語。</dd>
        <dt>lost in the middle</dt><dd>長い文脈の中央に置かれた情報の利用が落ちる現象。Liu ら TACL 2023。</dd>
        <dt>Meta-ExternalAgent / -ExternalFetcher / -WebIndexer</dt><dd>Meta の学習・収集 / ユーザー起動 / 検索品質。ExternalFetcher は robots.txt を迂回しうると明記。</dd>
        <dt>MistralAI-User / -Index / -Training</dt><dd>Mistral のユーザー起動 / 検索 / 学習。学習用だけが生成 AI 学習に使われる。</dd>
        <dt>言及 / 引用</dt><dd>言及は名前が出ること。引用は出典 URL が付くこと。</dd>
        <dt>NOCACHE / NOARCHIVE</dt><dd>Bing のメタタグ。NOARCHIVE は Copilot の回答からも学習からも外れる。通常の Bing 検索表示は残る。</dd>
        <dt>OAI-SearchBot</dt><dd>ChatGPT search 用インデックス。拒否すると検索回答に出ない。</dd>
        <dt>PerplexityBot / User</dt><dd>検索掲載 / ユーザー起動。後者は一般に robots.txt を無視する。</dd>
        <dt>post-rationalization</dt><dd>生成したあとで、それらしい出典を後付けすること。</dd>
        <dt>query fan-out</dt><dd>一つの質問から複数の関連検索を同時に出すこと。</dd>
        <dt>RFC 9309</dt><dd>robots.txt の標準。規則はアクセス認可ではないと明記。4xx は許可、5xx は全面禁止とみなす。</dd>
        <dt>Search generative AI control</dt><dd>Search Console の生成 AI 面トグル。学習オプトアウトではない。</dd>
        <dt>SEO</dt><dd>検索向けの発見・理解・掲載。Google は生成 AI 面でも土台だとする。</dd>
        <dt>構造化データ</dt><dd>JSON-LD 等。リッチリザルト用。生成 AI 検索の必須条件ではない。</dd>
      </dl>
    </section>
"""

FOOT = """
  </div>
  <script src="js/learn.js"></script>
</body>
</html>
"""

REDIRECT = """<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="utf-8">
  <meta http-equiv="refresh" content="0;url=../index.html#{hash}">
  <title>移動します</title>
</head>
<body>
  <p><a href="../index.html#{hash}">教材へ進む</a></p>
</body>
</html>
"""

CARD = """<div class="card" data-card="{cid}">
          <p class="q">{q}</p>
          <div class="try">
            <ul class="choices">
{choices}
            </ul>
            <button type="button" class="btn" data-reveal>答え合わせ</button>
            <p>選ぶ前に、声か頭の中で自分の答えを言い切ってください。</p>
          </div>
          <p class="verdict" hidden></p>
          <div class="a" hidden>{ans}</div>
          <p data-sched hidden></p>
          <div class="after" hidden><button type="button" class="btn" data-next-card>次のカード</button></div>
        </div>"""

CHOICE = """              <li><label class="choice"><input type="radio" name="{cid}" value="{n}"{correct}><span class="key">{key}</span><span class="body">{text}</span></label></li>"""

# 選択肢をまだ書いていないカードは、従来の自由記述のまま残す。
CARD_FREE = """<div class="card" data-card="{cid}">
          <p class="q">{q}</p>
          <div class="try">
            <textarea rows="2" aria-label="思い出したことを書く"></textarea>
            <button type="button" class="btn" data-reveal>答え合わせ</button>
            <p>書かずに、声か頭の中で言い切ってからでも構いません。</p>
          </div>
          <div class="a" hidden>{ans}</div>
          <div class="grade" hidden>
            <button type="button" class="btn ghost" data-grade="again">もう一度</button>
            <button type="button" class="btn" data-grade="good">言えた</button>
          </div>
          <p data-sched hidden></p>
        </div>"""

CARD_RE = re.compile(
    r'<card id="(?P<cid>[^"]+)">(?P<body>.*?)</card>',
    re.DOTALL,
)
PART_RE = re.compile(r"<(?P<tag>q|ans)>(?P<text>.*?)</(?P=tag)>", re.DOTALL)
OPT_RE = re.compile(r"<opt(?P<correct>\s+correct)?>(?P<text>.*?)</opt>", re.DOTALL)


def expand_cards(html_text):
    """<card id><q>問い</q><opt correct>…</opt><opt>…</opt><ans>解説</ans></card> を
    多肢選択の想起カードに開く。<opt> が無いカードは自由記述のまま残す。"""
    free = []

    def sub(m):
        cid = m.group("cid")
        body = m.group("body")
        parts = {p.group("tag"): p.group("text").strip() for p in PART_RE.finditer(body)}
        opts = [(bool(o.group("correct")), o.group("text").strip()) for o in OPT_RE.finditer(body)]
        if "q" not in parts or "ans" not in parts:
            raise SystemExit(f"card {cid}: <q> か <ans> がありません")
        if not opts:
            free.append(cid)
            return CARD_FREE.format(cid=cid, q=parts["q"], ans=parts["ans"])
        if sum(1 for correct, _ in opts if correct) != 1:
            raise SystemExit(f"card {cid}: 正解の <opt correct> はちょうど 1 つにしてください")
        if len(opts) < 3:
            raise SystemExit(f"card {cid}: 選択肢は 3 つ以上にしてください")
        # 並びはカード ID から決める。ビルドのたびに動くと覚え直しになるため。
        random.Random(cid).shuffle(opts)
        choices = "\n".join(
            CHOICE.format(
                cid=cid,
                n=n,
                key="ABCDE"[n],
                text=text,
                correct=' data-correct="1"' if correct else "",
            )
            for n, (correct, text) in enumerate(opts)
        )
        return CARD.format(cid=cid, q=parts["q"], ans=parts["ans"], choices=choices)

    out, count = CARD_RE.subn(sub, html_text)
    if "<card " in out:
        raise SystemExit("card タグの書式が違います: " + out.split("<card ")[1][:80])
    return out, count, free


# 表記チェック（_fragments/STYLE.md のルール 5・6）。警告のみでビルドは止めない。
BANNED = [
    (r"ファンアウト", "query fan-out に統一"),
    (r"(?<!Overviews（)AI 概要", "AI Overviews に統一（初出のみ「AI Overviews（AI 概要）」）"),
    (r"内部エンジン", "内部 GE に統一"),
    (r"生成 AI 制御", "生成 AI control に統一"),
    (r"(?<!位置補正単語数（)Position-Adjusted Word Count", "位置補正単語数に統一（初出のみ英語併記）"),
    (r"MAU", "月間アクティブユーザー と書く"),
    (r"青リンク", "検索結果一覧のリンク と書く"),
    (r"本戦", "勝負どころ と書く"),
    (r"入場(?!条件)", "入場条件 と書く"),
    (r"サーバ(?!ー)", "サーバー（長音符を付ける）"),
    (r"クローラ(?!ー)", "クローラー（長音符を付ける）"),
    (r"パーサ(?!ー)", "パーサー（長音符を付ける）"),
    (r"ユーザ(?!ー)", "ユーザー（長音符を付ける）"),
    (r"ブラウザ(?!ー)", "ブラウザー（長音符を付ける）"),
    (r"フェッチャ(?!ー)", "フェッチャー（長音符を付ける）"),
    (r"塊", "段落（UI の読み進み単位は「節」）"),
    (r"課", "章（章 → 節 → 想起カード）"),
]


def lint_notation(lid, text):
    """禁止表記を行番号つきで警告する。件数を返す。"""
    hits = 0
    for n, line in enumerate(text.splitlines(), 1):
        for pattern, hint in BANNED:
            if re.search(pattern, line):
                where = f"_fragments/{lid}.html:{n}" if lid.isdigit() else f"build.py の {lid}:{n} 行目"
                print(f"  表記: {where} {pattern} → {hint}")
                hits += 1
    return hits


parts = [HEAD.replace("{{terms}}", terms_script()), HOME]
total_cards = 0
lint_hits = 0
free_cards = []
for lid, (title, goal, prime) in META.items():
    raw = (FRAG / f"{lid}.html").read_text(encoding="utf-8")
    lint_hits += lint_notation(lid, raw)
    lint_hits += lint_notation(f"META {lid}", "\n".join((title, goal, prime)))
    steps, made, free = expand_cards(autolink_terms(raw))
    free_cards.extend(free)
    total_cards += made
    parts.append(
        f"""
    <section class="view" id="l{lid}" data-view="{lid}" hidden>
      <header class="lesson-head">
        <p class="kicker">第{int(lid)}章</p>
        <h1>{title}</h1>
        <p class="goal"><span>この章のゴール</span>{goal}</p>
        <div class="prime"><b>読む前に一度だけ</b><p>{prime}</p></div>
      </header>
      <p class="chunk-meter" data-meter>節</p>
      <div class="steps">
{steps}
      </div>
      <section class="finish" data-finish hidden aria-live="polite"></section>
      <nav class="step-nav" aria-label="節の移動">
        <button type="button" class="ghost" data-prev>前の節</button>
        <button type="button" data-next>次の節</button>
        <span class="grow"></span>
        <button type="button" class="ghost" data-all>全部見る</button>
        <button type="button" class="ghost quiet" data-reset>この章をリセット</button>
      </nav>
    </section>
"""
    )
    (OUT / f"{lid}.html").write_text(
        REDIRECT.replace("{hash}", f"l{lid}"), encoding="utf-8"
    )
    print("redirect", lid)

for name, chunk in (("HOME", HOME), ("REVIEW", REVIEW), ("GLOSSARY", GLOSSARY_STATIC)):
    lint_hits += lint_notation(name, chunk)

parts.append(REVIEW)
parts.append(glossary_html())
parts.append(FOOT)
(ROOT / "index.html").write_text("".join(parts), encoding="utf-8")
(OUT / "glossary.html").write_text(
    REDIRECT.replace("{hash}", "lg"), encoding="utf-8"
)
(OUT / "review.html").write_text(REDIRECT.replace("{hash}", "lr"), encoding="utf-8")
print(f"wrote index.html ({total_cards} cards)")
if free_cards:
    print("選択肢が未作成のカード", len(free_cards), "枚:", ", ".join(free_cards[:8]))
if lint_hits:
    print(f"表記の警告 {lint_hits} 件（_fragments/STYLE.md 参照）")
