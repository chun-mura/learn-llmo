# 第 11 課: 引用は根拠とは限らない

## この課のゴール

引用が付いていても根拠とは限らないことを、論文の数字つきで言える。生成エンジン側の限界と、自サイトが攻撃の入口になる筋を、施策と分けて扱える。

## 引用の correctness と faithfulness

生成回答に出典リンクが付いていると、その文はその文書から書かれた、と読みたくなる。研究はそこを分ける。

- **correctness**: 引用先を読むと、その文と矛盾しない
- **faithfulness**: モデルが実際にその文書を使って書いた

Wallat, Heuss, de Rijke & Anand, *Correctness is not Faithfulness in RAG Attributions*（[arXiv:2412.18004](https://arxiv.org/abs/2412.18004), 2024-12-23 提出）は、"current attributed answers often lack citation faithfulness (up to 57 percent of the citations)" と報告している。生成してから、それらしい出典を後付けする post-rationalization である。

この 57% は特定の構成を測った数字であって、「どの製品でも 57%」ではない。教材として引くのは「引用の存在は根拠の存在を保証しない」まで。

## 位置バイアス（lost in the middle）

取られた文書は、モデルへの入力の中に並べられる。並べる位置は効く。

Liu et al., *Lost in the Middle: How Language Models Use Long Contexts*（TACL 2023 / [arXiv:2307.03172](https://arxiv.org/abs/2307.03172)）は、"performance is often highest when relevant information occurs at the beginning or end of the input context, and significantly degrades when models must access relevant information in the middle of long contexts" と述べている。長文脈をうたうモデルでも起きる。

実務への含意は限定的である。各製品が取得した文書をどう並べるかは公開されていない。言えるのは「同じ文書でも置かれ方で使われ方が変わりうる」まで。「見出し直下 40〜60 語」のような具体値はここからは出ない（第 9 課の未検証リスト）。

## 全員が同じ手を打つと

C-SEO Bench（第 5 課）は、競合も同じ C-SEO 手法を採用していく条件で、多くの手法が効かないどころか順位を下げると報告した。採用が広がるほど混雑し、ゼロサムに近づく。

つまり、文体テンプレートの一括適用は、時間が経つほど効きが落ちる方向にある。残るのは、他社が真似できない一次情報のほうである。

## 自サイトが入口になる

ここは施策ではなく防御の話である。生成エンジンは web の本文をそのままモデルに渡す。本文は入力である。

Zhang et al., *Practical Poisoning Attacks against Retrieval-Augmented Generation*（CorruptRAG, ACM SACMAT 2026 / [arXiv:2504.03957](https://arxiv.org/abs/2504.03957)）は、検索対象に毒入りテキストを **1 件**注入するだけで RAG の出力を操作できることを示した。多数の注入を前提にした従来手法より現実的だ、というのが主張である。

自社側で見るのは、自分が書いた本文ではなく、**他人が書ける面**である。

- レビュー、コメント、Q&A、掲示板などの UGC
- ユーザーが本文を作れるプロフィールページ
- 外部から取り込んで丸ごと出している一覧やフィード

対策は普通のものになる。投稿の審査、インデックスさせない、`noindex`、公開前の目視。攻撃の作り方はこの教材では扱わない。

## 線引き

| やる | やらない |
|---|---|
| 引用されたら、引用先の文が本当にその主張を支えているか読む | 引用があることを根拠の証拠として社内に報告する |
| 競合も同じ改稿をする前提で、独自の一次情報を作る | 文体テンプレートを全ページに一括適用する |
| 他人が書ける面を点検する | 他社の回答を操作しにいく |

## 未検証として残す

- 日本語圏での再現（上記はいずれも英語中心の評価）
- 各製品が取得文書をどう並べているか
- UGC 経由のポイズニングによる実被害の規模

## 確認問題

1. 「AI 回答に自社が引用された」と報告を受けた。次に確認することを二つ挙げよ。
2. 引用の correctness と faithfulness の違いを、一文ずつで書け。
