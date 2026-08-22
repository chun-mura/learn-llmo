from pathlib import Path

ROOT = Path(__file__).parent
FRAG = ROOT / "_fragments"
OUT = ROOT / "lessons"
OUT.mkdir(exist_ok=True)

META = {
    "01": ("LLMO とは何か", "「何を最適化するのか」を、SEO の順位と混ぜずに言える。"),
    "02": ("生成エンジンの仕組み", "処理の段取りを書き起こせる。fan-out で引用元がずれる理由を言える。"),
    "03": ("SEO · GEO · LLMO · AEO", "四つの略語を対象面で使い分けられる。Google が Search で SEO と言う範囲を言える。"),
    "04": ("ボットを分ける", "学習用と検索用を分けて robots.txt を書ける。ユーザー起動フェッチャの差を言える。"),
    "05": ("GEO 論文を読む", "「最大 40%」を、指標・エンジン・改変対象つきで引用できる。"),
    "06": ("中身が引用される条件", "対象エンジンを決めたうえで、ページを答えの材料として直せる。"),
    "07": ("技術的な準備", "届く・意味が付く・エージェント用地図を混ぜずに点検できる。"),
    "08": ("測定とコントロール", "学習・AI 面・青リンクを別スイッチで扱える。"),
    "09": ("よくある誤解", "一次情報で止められる誤解を、自分の言葉で潰せる。"),
    "10": ("演習", "自サイト（または架空の店）で点検できる。"),
}

HEAD = """<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>LLMO を一塊ずつ読む</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=BIZ+UDPGothic:wght@400;700&family=Fragment+Mono&family=Shippori+Mincho:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/learn.css">
</head>
<body class="desk" data-lesson="00">
  <a class="skip" href="#stage">本文へ</a>
  <aside class="rail" data-rail>
    <a class="rail-brand" href="#l00">LLMO 教材<strong>一塊ずつ読む</strong></a>
    <nav aria-label="課の順">
    <ol>
      <li><a href="#l01"><span class="num">01</span><span>何を最適化するか</span></a></li>
      <li><a href="#l02"><span class="num">02</span><span>検索してから書く</span></a></li>
      <li><a href="#l03"><span class="num">03</span><span>SEO GEO LLMO AEO</span></a></li>
      <li><a href="#l04"><span class="num">04</span><span>学習と検索は別</span></a></li>
      <li><a href="#l05"><span class="num">05</span><span>数字の条件</span></a></li>
      <li><a href="#l06"><span class="num">06</span><span>引用される塊</span></a></li>
      <li><a href="#l07"><span class="num">07</span><span>届く・意味・地図</span></a></li>
      <li><a href="#l08"><span class="num">08</span><span>スイッチを混ぜない</span></a></li>
      <li><a href="#l09"><span class="num">09</span><span>一次情報で止める</span></a></li>
      <li><a href="#l10"><span class="num">10</span><span>手を動かす</span></a></li>
    </ol>
    </nav>
    <div class="rail-foot"><a href="#lg">用語集</a></div>
  </aside>
  <div class="stage" id="stage">
"""

HOME = """
    <section class="view is-on" id="l00" data-view="00">
      <div class="home-hero">
        <p class="kicker">調査日 2026-08-21 · 一次情報のみ</p>
        <h1>一度に一塊だけ読む</h1>
        <p>Markdown の長文を、机の上の教科書に組み直したものです。各課は 5〜7 の塊に切ってあり、次へを押すまで次の塊は出ません。出典は閉じてあります。</p>
        <div class="pair">
          <div class="seal paper"><small>朱 · 論文</small>GEO（KDD 2024）。すでに検索上位に入ったページを、生成が厚く引用するか。</div>
          <div class="seal official"><small>藍 · 公式</small>Google Search。入場はインデックスとスニペット。SEO の土台が先。</div>
        </div>
        <p>二つは同じ「AI に載せる」でも、層が違います。混ぜないことが、この教材の核です。</p>
        <p><a class="btn" href="#l01">第 1 課から始める</a></p>
      </div>
      <nav class="path" id="path" aria-label="課の順">
        <a href="#l01"><span class="n">01</span><strong>LLMO とは何か</strong><em>何を最適化するか</em></a>
        <a href="#l02"><span class="n">02</span><strong>生成エンジン</strong><em>検索してから書く</em></a>
        <a href="#l03"><span class="n">03</span><strong>用語の地図</strong><em>SEO GEO LLMO AEO</em></a>
        <a href="#l04"><span class="n">04</span><strong>ボットを分ける</strong><em>学習と検索は別</em></a>
        <a href="#l05"><span class="n">05</span><strong>GEO 論文</strong><em>数字の条件</em></a>
        <a href="#l06"><span class="n">06</span><strong>中身</strong><em>引用される塊</em></a>
        <a href="#l07"><span class="n">07</span><strong>技術</strong><em>届く · 意味 · 地図</em></a>
        <a href="#l08"><span class="n">08</span><strong>測定</strong><em>スイッチを混ぜない</em></a>
        <a href="#l09"><span class="n">09</span><strong>誤解</strong><em>一次情報で止める</em></a>
        <a href="#l10"><span class="n">10</span><strong>演習</strong><em>手を動かす</em></a>
      </nav>
      <p class="note home-note">キーボード: J / 右で次の塊、K / 左で戻る、A で全部表示。進捗はこのブラウザにだけ残ります。</p>
    </section>
"""

GLOSSARY = r"""
    <section class="view" id="lg" data-view="g" hidden>
      <header class="lesson-head">
        <p class="kicker">付録</p>
        <h1>用語集</h1>
        <p class="goal"><span>使い方</span>作業用の定義です。法令上の定義ではありません。点線の語にマウスを置くと同じ説明が出ます。</p>
      </header>
      <dl class="dl" style="max-width:38rem">
        <dt>AEO</dt><dd>質問に対する直接回答面への最適化という業界用語。Google の製品名ではない。</dd>
        <dt>AI Mode / AI Overviews</dt><dd>Google Search の生成 AI 面。両者はモデルも手法も違い、出るリンクも一致しない。Overviews は追加価値があるときだけ出る。</dd>
        <dt>ChatGPT-User</dt><dd>ユーザー起動の取得。robots.txt が適用されない場合がある。検索掲載の判定には使わない。</dd>
        <dt>ClaudeBot / SearchBot / User</dt><dd>Anthropic の学習 / 検索 / ユーザー起動。robots.txt を尊重すると公式が述べる。</dd>
        <dt>E-E-A-T</dt><dd>経験・専門性・権威性・信頼性。単一のランキング因子ではない。</dd>
        <dt>GEO</dt><dd>Generative Engine Optimization。KDD 2024 の枠組み。</dd>
        <dt>Google-Extended</dt><dd>Gemini アプリと Vertex の学習・接地。Search の掲載・順位には使わない。</dd>
        <dt>GPTBot</dt><dd>OpenAI の学習用。検索掲載とは独立。</dd>
        <dt>grounding / RAG</dt><dd>検索で取ったページに回答を接地する。</dd>
        <dt>impression</dt><dd>論文の可視性。単語数、位置補正単語数、主観印象。</dd>
        <dt>llms.txt</dt><dd>エージェント向けの Markdown 地図。Google Search は使わない。</dd>
        <dt>LLMO</dt><dd>LLM の回答で言及・引用される状態を改善する実務用語。</dd>
        <dt>言及 / 引用</dt><dd>言及は名前が出ること。引用は出典 URL が付くこと。</dd>
        <dt>OAI-SearchBot</dt><dd>ChatGPT search 用インデックス。拒否すると検索回答に出ない。</dd>
        <dt>PerplexityBot / User</dt><dd>検索掲載 / ユーザー起動。後者は一般に robots.txt を無視する。</dd>
        <dt>query fan-out</dt><dd>一つの質問から複数の関連検索を同時に出すこと。</dd>
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

parts = [HEAD, HOME]
for lid, (title, goal) in META.items():
    steps = (FRAG / f"{lid}.html").read_text(encoding="utf-8")
    parts.append(
        f"""
    <section class="view" id="l{lid}" data-view="{lid}" hidden>
      <header class="lesson-head">
        <p class="kicker">第{int(lid)}課</p>
        <h1>{title}</h1>
        <p class="goal"><span>この課のゴール</span>{goal}</p>
      </header>
      <p class="chunk-meter" data-meter>塊</p>
      <div class="steps">
{steps}
      </div>
      <nav class="step-nav" aria-label="塊の移動">
        <button type="button" class="ghost" data-prev>前の塊</button>
        <button type="button" data-next>次の塊</button>
        <span class="grow"></span>
        <button type="button" class="ghost" data-all>全部見る</button>
      </nav>
    </section>
"""
    )
    (OUT / f"{lid}.html").write_text(
        REDIRECT.replace("{hash}", f"l{lid}"), encoding="utf-8"
    )
    print("redirect", lid)

parts.append(GLOSSARY)
parts.append(FOOT)
(ROOT / "index.html").write_text("".join(parts), encoding="utf-8")
(OUT / "glossary.html").write_text(
    REDIRECT.replace("{hash}", "lg"), encoding="utf-8"
)
print("wrote index.html")
