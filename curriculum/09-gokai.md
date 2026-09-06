# 第 9 課: よくある誤解

一次情報で止められるものだけ書く。止められない噂は「未検証」とラベルする。

## 1. LLMO をやれば SEO は不要

Google の生成 AI 機能は Search インデックスからの RAG である。スニペット可能なインデックスが入場条件で、追加の技術要件はない。[出典: AI features and your website, AI optimization guide]

ChatGPT / Perplexity も、検索用ボットが取れないページは出典候補に入りにくい。土台は取得である。

## 2. GEO 論文の「最大 40%」は Google AI Overviews の公式効果

論文の内部エンジンは GPT-3.5 と Google **上位 5 件**。指標は著者が定義した impression。Google 公式ガイドは GEO/AEO ハックの多くを Search では無効と書いている。数字を使うなら「どのエンジン、どの指標、どの手法」を付ける。

## 3. キーワードを増やせば生成 AI にも効く

論文では Keyword Stuffing が位置補正単語数を下げた。内部 GE と Perplexity の両方。Google は同義語を理解するので、バリエーション用の薄いページは scaled content abuse になりうると案内している。

## 4. llms.txt を置けば ChatGPT と Google に載る

llms.txt は提案仕様。Lighthouse では任意。Google Search は使わないと明記。ドキュメントをエージェントに案内する用途と、Search の出典選定は別である。

## 5. 構造化データを入れれば AI に引用される

構造化データはリッチリザルト適格化と、ページ内容の手がかりである。生成 AI 検索に必須ではなく、特別な型も不要。本文に無い情報を JSON-LD だけに書くのはガイドライン違反である。

## 6. GPTBot を拒否すると ChatGPT search に出ない

GPTBot は学習。検索掲載は OAI-SearchBot。独立である。逆に、学習は許可して検索だけ拒否することもできる。

## 7. Google-Extended を拒否すると AI Overviews に出ない

Google-Extended は Gemini アプリと Vertex の学習・接地。Search の掲載・順位には使わない。AI Overviews を止めたいなら Search generative AI control（展開中）か、プレビュー制御 / `noindex`。

## 8. robots.txt で全 AI を止められる

Perplexity-User は一般に robots.txt を無視する。ChatGPT-User は適用されない場合がある。Anthropic の Claude-User は尊重すると書いている。秘密の URL は認証する。

## 9. 権威的な文体にすれば選ばれる

論文では Authoritative の押しは弱く、統計・引用・流暢さの方が強い。Google は不自然な言及集めより、高品質コンテンツとスパム対策側を見ると書いている。

## 10. AI Overviews に出ないのは常に失敗

AI Overviews は、通常検索に追加価値があるときだけ出る。出ないクエリでは青リンクが本戦である。出ているのに自社が無いことと、機能自体が無いことを分ける。

## 11. robots.txt に書けば、利用を禁止したことになる

RFC 9309 は "These rules are not a form of access authorization." と書いている。規格の側に学習・検索・エージェントという用途の区別も無い。用途はベンダーが UA を分けて実現しているだけである。禁止したいものは認証で止める。

## 12. 引用が付いている＝その文書を根拠に生成した

正しく見える引用のうち最大 57% が後付け（post-rationalization）だった、という報告がある（Wallat et al., arXiv:2412.18004）。引用の存在は根拠の存在を保証しない。第 11 課。

## 13. 論文で効いた改変は、競合も同じことをしても効く

C-SEO Bench は、競合採用と複数ドメインの条件で、多くの手法が効かないどころか順位を下げると報告している（第 5 課）。

## 未検証として残す（この教材では断言しない）

- 日本語クエリと英語クエリで、同じ手法の効果差
- 2026 年時点の ChatGPT search の第三者プロバイダの中身
- 「見出し直下 40〜60 語」などの業界数値（GEO 論文の指標定義には無い）
- Reddit 等 UGC が何割引用されるか（調査は多いが、本教材の一次セットには入れていない）
- Bytespider（ByteDance）の robots.txt 遵守（到達可能な公式文書が無い）

## 次の課

手を動かす。[10-enshu.md](10-enshu.md)
