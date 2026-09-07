const LESSONS = [
  { id: "00", title: "机に着く", short: "はじめに" },
  { id: "01", title: "LLMO とは何か", short: "何を最適化するか" },
  { id: "02", title: "生成エンジン", short: "検索してから書く" },
  { id: "03", title: "用語の地図", short: "SEO GEO LLMO AEO" },
  { id: "04", title: "ボットを分ける", short: "学習と検索は別" },
  { id: "05", title: "GEO 論文", short: "数字の条件" },
  { id: "06", title: "中身", short: "引用される塊" },
  { id: "07", title: "技術", short: "届く・意味・地図" },
  { id: "08", title: "測定", short: "スイッチを混ぜない" },
  { id: "09", title: "誤解", short: "一次情報で止める" },
  { id: "10", title: "演習", short: "手を動かす" },
  { id: "11", title: "引用と根拠", short: "引用は根拠ではない" },
  { id: "r", title: "復習", short: "間隔をあけて思い出す" },
  { id: "g", title: "用語集", short: "定義" },
];

const TERMS = {
  LLMO: "Large Language Model Optimization。生成 AI の回答で言及・引用される状態を改善する実務用語。",
  GEO: "Generative Engine Optimization。Aggarwal ら KDD 2024 の枠組み。回答内の可視性をテキスト改変で上げる。",
  SEO: "検索エンジン向けの発見・理解・掲載の最適化。Google は生成 AI 面でも土台だとする。",
  AEO: "Answer Engine Optimization。直接回答面への最適化という業界用語。Google の製品名ではない。",
  "query fan-out": "一つの質問から複数の関連検索を同時に出すこと。Google 公式。",
  RAG: "検索で取ったページに回答を接地する手法。Google の生成 AI 機能の土台。",
  言及: "回答文にブランド名が出ること。リンクは無いこともある。",
  引用: "出典 URL が回答に付くこと。",
  "OAI-SearchBot": "ChatGPT search 用のインデックスボット。拒否すると検索回答に出ない。",
  GPTBot: "OpenAI の学習用クローラ。検索掲載とは独立。",
  "Google-Extended": "Gemini アプリと Vertex の学習・接地用トークン。Search の掲載・順位には使わない。",
  "llms.txt": "Jeremy Howard 提案の Markdown 地図。Google Search は使わない。",
  impression: "GEO 論文の可視性。単語数、位置補正単語数、主観印象。",
  "RFC 9309": "robots.txt を標準化した RFC。規則はアクセス認可ではない、と明記している。",
  "Content-Usage": "IETF aipref が定義中の利用意向フィールド。Internet-Draft であり RFC ではない。",
  "Content-Signal": "Cloudflare の robots.txt 用ディレクティブ。search / ai-input / ai-train の可否を書く。",
  NOARCHIVE: "Bing のメタタグ。Copilot の回答に含めず、学習にも使わせない。通常の検索表示は残る。",
  faithfulness: "引用がその文書を実際に根拠にしているか。正しく見えることとは別の性質。",
  "C-SEO Bench": "Puerto ら NeurIPS 2025 のベンチマーク。競合下では C-SEO 手法が効かない、と報告した。",
  "post-rationalization": "生成したあとで、それらしい出典を後付けすること。",
};

/* 間隔反復。箱 1〜5 の日数。Cepeda et al. 2006 / 2008 の「間隔を広げる」原理だけを取る。
   アルゴリズムの巧拙（SM-2 / FSRS）を比べた人対象の対照試験は乏しいため、Leitner で足りる。 */
const BOX_DAYS = [1, 3, 7, 16, 35];
const STORE = "llmo-learn-v2";
const STORE_V1 = "llmo-learn-v1";

function today() {
  const d = new Date();
  const p = (n) => String(n).padStart(2, "0");
  return `${d.getFullYear()}-${p(d.getMonth() + 1)}-${p(d.getDate())}`;
}

function shiftDate(date, delta) {
  const d = new Date(`${date}T00:00:00`);
  d.setDate(d.getDate() + delta);
  const p = (n) => String(n).padStart(2, "0");
  return `${d.getFullYear()}-${p(d.getMonth() + 1)}-${p(d.getDate())}`;
}

function addDays(days) {
  return shiftDate(today(), days);
}

function daysUntil(date) {
  const ms = new Date(`${date}T00:00:00`) - new Date(`${today()}T00:00:00`);
  return Math.round(ms / 86400000);
}

function migrateV1() {
  const state = { v: 2, read: {}, done: {}, cards: {} };
  try {
    const old = JSON.parse(localStorage.getItem(STORE_V1) || "{}");
    Object.keys(old).forEach((k) => {
      if (k === "done") state.done = Object.assign({}, old.done);
      else if (typeof old[k] === "number") state.read[k] = old[k];
    });
  } catch {
    /* 旧データが壊れていても初期状態で続ける */
  }
  return state;
}

function loadState() {
  let state;
  try {
    state = JSON.parse(localStorage.getItem(STORE) || "null");
  } catch {
    state = null;
  }
  if (!state) state = migrateV1();
  state.read = state.read || {};
  state.done = state.done || {};
  state.cards = state.cards || {};
  state.days = state.days || {};
  return state;
}

function saveState(state) {
  try {
    localStorage.setItem(STORE, JSON.stringify(state));
  } catch {
    /* 保存できなくても学習自体は続けられる */
  }
}

function markProgress(id, chunk, total) {
  const state = loadState();
  const before = state.read[id] || 0;
  state.read[id] = Math.max(before, chunk);
  if (chunk >= total) state.done[id] = true;
  /* 連続日数は「その日に何かしたか」だけを見る。読み進めた日と採点した日を同じ扱いにする。 */
  if (chunk > before) state.days[today()] = true;
  saveState(state);
}

/* 連続日数。今日の記録が無ければ昨日から数える（その日はまだ手をつけていないだけ）。 */
function streakDays() {
  const days = loadState().days || {};
  let cursor = today();
  if (!days[cursor]) {
    cursor = shiftDate(cursor, -1);
    if (!days[cursor]) return 0;
  }
  let n = 0;
  while (days[cursor]) {
    n += 1;
    cursor = shiftDate(cursor, -1);
  }
  return n;
}

/* --- カード（想起練習） --- */

function cardState(id) {
  return loadState().cards[id] || null;
}

function gradeCard(id, good) {
  const state = loadState();
  const card = state.cards[id] || { box: 0, due: today(), r: 0, w: 0 };
  if (good) {
    card.box = Math.min(card.box + 1, BOX_DAYS.length);
    card.due = addDays(BOX_DAYS[card.box - 1]);
    card.r += 1;
  } else {
    card.box = 0;
    card.due = today();
    card.w += 1;
  }
  card.seen = today();
  state.days[today()] = true;
  state.cards[id] = card;
  saveState(state);
  return card;
}

function dueCards() {
  const state = loadState();
  const now = today();
  return [...document.querySelectorAll("[data-card]")]
    .map((el) => el.dataset.card)
    .filter((id, i, all) => all.indexOf(id) === i)
    .filter((id) => {
      const card = state.cards[id];
      return card && card.due <= now;
    });
}

function cardIds(lesson) {
  const scope = lesson ? `[data-view="${lesson}"] [data-card]` : "[data-card]";
  return [...new Set([...document.querySelectorAll(scope)].map((el) => el.dataset.card))];
}

function cardStats(lesson) {
  const state = loadState();
  const ids = cardIds(lesson);
  const seen = ids.filter((id) => state.cards[id]);
  const held = seen.filter((id) => state.cards[id].box >= 2);
  /* 箱ごとの枚数。箱 0 は「次も当日に出る」、箱 5 は「35 日あけて言えた」。 */
  const boxes = [0, 0, 0, 0, 0, 0];
  let right = 0;
  let wrong = 0;
  let soonest = null;
  seen.forEach((id) => {
    const card = state.cards[id];
    boxes[Math.min(card.box, 5)] += 1;
    right += card.r || 0;
    wrong += card.w || 0;
    if (!soonest || card.due < soonest) soonest = card.due;
  });
  const graded = right + wrong;
  return {
    total: ids.length,
    seen: seen.length,
    held: held.length,
    due: lesson ? ids.filter((id) => state.cards[id] && state.cards[id].due <= today()).length : dueCards().length,
    boxes,
    right,
    wrong,
    rate: graded ? Math.round((right / graded) * 100) : null,
    soonest,
  };
}

/* 課をまたいで混ぜる。同じ課が続かないよう並べ替える。
   Brunmair & Richter 2019 の効果量は中程度で、万能ではない。順序だけの工夫と割り切る。 */
function interleave(ids) {
  const shuffled = ids.slice();
  for (let i = shuffled.length - 1; i > 0; i -= 1) {
    const j = Math.floor(Math.random() * (i + 1));
    [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
  }
  const lessonOf = (id) => id.split("-")[1];
  const left = {};
  shuffled.forEach((id) => {
    left[lessonOf(id)] = (left[lessonOf(id)] || 0) + 1;
  });
  const out = [];
  const rest = shuffled.slice();
  while (rest.length) {
    const last = out.length ? lessonOf(out[out.length - 1]) : null;
    // 残りが多い課から先に出す。ここを最初に見つけた候補にすると、
    // 終盤に同じ課だけが残って連続してしまう。
    let pick = -1;
    rest.forEach((id, i) => {
      if (lessonOf(id) === last) return;
      if (pick < 0 || left[lessonOf(id)] > left[lessonOf(rest[pick])]) pick = i;
    });
    if (pick < 0) pick = 0;
    const [id] = rest.splice(pick, 1);
    left[lessonOf(id)] -= 1;
    out.push(id);
  }
  return out;
}

function resetCard(el) {
  el.classList.remove("is-open", "is-good", "is-again");
  const answer = el.querySelector(".a");
  const grade = el.querySelector(".grade");
  const sched = el.querySelector("[data-sched]");
  const field = el.querySelector("textarea");
  const reveal = el.querySelector("[data-reveal]");
  if (answer) answer.hidden = true;
  if (grade) grade.hidden = true;
  if (sched) sched.hidden = true;
  if (field) field.value = "";
  if (reveal) reveal.hidden = false;
}

function openCard(el) {
  const answer = el.querySelector(".a");
  const grade = el.querySelector(".grade");
  const reveal = el.querySelector("[data-reveal]");
  if (answer) answer.hidden = false;
  if (grade) grade.hidden = false;
  if (reveal) reveal.hidden = true;
  el.classList.add("is-open");
  grade?.querySelector("[data-grade]")?.focus({ preventScroll: true });
}

function paintSchedule(el, card) {
  const sched = el.querySelector("[data-sched]");
  if (!sched) return;
  const gap = daysUntil(card.due);
  sched.hidden = false;
  sched.textContent =
    card.box === 0 ? "この回の終わりにもう一度出ます。" : `次は ${gap} 日後（箱 ${card.box}）。`;
}

/* --- 復習面 --- */

let reviewQueue = [];
let reviewIndex = 0;
let reviewAgain = [];

function reviewSlot() {
  return document.querySelector("[data-review-slot]");
}

function paintReview() {
  const slot = reviewSlot();
  const meter = document.querySelector("[data-review-meter]");
  const emptyBox = document.querySelector("[data-review-empty]");
  if (!slot) return;
  slot.innerHTML = "";
  const id = reviewQueue[reviewIndex];
  if (!id) {
    if (meter) meter.textContent = reviewQueue.length ? "この回は終わりです。" : "";
    if (emptyBox) {
      emptyBox.hidden = false;
      emptyBox.querySelector("[data-review-done]").textContent = reviewQueue.length
        ? `${reviewQueue.length} 枚やりました。続きはまた日をあけて。`
        : "今日の期限のカードはありません。課を読み進めるか、日をあけて戻ってきてください。";
    }
    return;
  }
  if (emptyBox) emptyBox.hidden = true;
  if (meter) {
    const ratio = (reviewIndex + 1) / reviewQueue.length;
    meter.innerHTML =
      `${reviewIndex + 1} / ${reviewQueue.length} 枚目` +
      `<span class="bar" aria-hidden="true"><i style="transform:scaleX(${ratio})"></i></span>`;
  }
  const source = document.querySelector(`.view:not(.review) [data-card="${id}"]`);
  if (!source) {
    reviewIndex += 1;
    paintReview();
    return;
  }
  const clone = source.cloneNode(true);
  resetCard(clone);
  const lesson = id.split("-")[1];
  const meta = LESSONS.find((l) => l.id === lesson);
  if (meta) {
    const tag = document.createElement("p");
    tag.className = "card-from";
    tag.textContent = `第${Number(lesson)}課 ${meta.title}`;
    clone.prepend(tag);
  }
  slot.appendChild(clone);
  clone.querySelector("textarea")?.focus({ preventScroll: true });
}

function startReview() {
  reviewQueue = interleave(dueCards());
  reviewIndex = 0;
  reviewAgain = [];
  paintReview();
}

function advanceReview(id, good) {
  if (!good && !reviewAgain.includes(id)) {
    reviewAgain.push(id);
    reviewQueue.push(id);
  }
  reviewIndex += 1;
  paintReview();
}

/* --- 課の修了面 ---
   最後の塊で「この課を終える」を押したとき、黙って次の課へ飛ばさない。
   何を言えるようになったか、カードがいつ戻ってくるかを見せてから送り出す。 */

function lessonGoal(id) {
  const el = document.querySelector(`[data-view="${id}"] .goal`);
  if (!el) return "";
  const clone = el.cloneNode(true);
  clone.querySelector("span")?.remove();
  return clone.textContent.trim();
}

function nextLessonMeta(id) {
  const idx = LESSONS.findIndex((l) => l.id === id);
  return LESSONS[idx + 1] || null;
}

function paintFinish(id) {
  const box = document.querySelector(`[data-view="${id}"] [data-finish]`);
  if (!box) return;
  const heading = document.querySelector(`[data-view="${id}"] .lesson-head h1`);
  const stats = cardStats(id);
  const nxt = nextLessonMeta(id);
  const goal = lessonGoal(id);
  const gap = stats.soonest === null ? null : Math.max(0, daysUntil(stats.soonest));
  const back = stats.soonest === null ? "—" : gap === 0 ? "今日" : `${gap} 日後`;
  const untouched = stats.total - stats.seen;
  const nextLabel = nxt
    ? nxt.id === "r"
      ? "復習へ"
      : `第${Number(nxt.id)}課「${nxt.title}」へ`
    : "ホームへ";
  box.innerHTML = `
    <p class="kicker">第${Number(id)}課 おわり</p>
    <h2>${heading ? heading.textContent : ""}</h2>
    ${goal ? `<p class="finish-goal"><span>言えるようになったこと</span>${goal}</p>` : ""}
    <div class="finish-stats">
      <div><b>${stats.seen} / ${stats.total}</b><span>この課のカードに答えた</span></div>
      <div><b>${back}</b><span>次にこの課のカードが出る日</span></div>
      <div class="quiet"><b>${untouched}</b><span>まだ答えていないカード</span></div>
    </div>
    <p class="finish-note">${
      untouched
        ? "答えていないカードは復習に出てきません。戻って先に自分の答えを出してください。"
        : "読み返すより、間をあけて思い出すほうが残ります。期限の日に復習面へ戻ってください。"
    }</p>
    <div class="finish-nav">
      <button type="button" class="btn" data-finish-next>${nextLabel}</button>
      <button type="button" class="btn ghost" data-finish-back>最後の塊に戻る</button>
      ${stats.due ? `<a class="btn ghost" href="#lr">期限のカード ${stats.due} 枚</a>` : ""}
    </div>
  `;
}

function showFinish(id) {
  const box = document.querySelector(`[data-view="${id}"] [data-finish]`);
  if (!box) {
    nextLesson(id);
    return;
  }
  paintFinish(id);
  document.body.classList.add("is-finish");
  box.hidden = false;
  const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;
  window.scrollTo({ top: 0, behavior: reduce ? "instant" : "smooth" });
  box.querySelector("[data-finish-next]")?.focus({ preventScroll: true });
}

function hideFinish() {
  document.body.classList.remove("is-finish");
  document.querySelectorAll("[data-finish]").forEach((el) => {
    el.hidden = true;
  });
}

/* --- ダッシュボード --- */

function paintDash() {
  const dash = document.querySelector("[data-dash]");
  if (!dash) return;
  const stats = cardStats();
  const readChunks = Object.values(loadState().read).reduce((a, b) => a + b, 0);
  const streak = streakDays();
  const boxMax = Math.max(1, ...stats.boxes);
  const boxBars = stats.boxes
    .map((n, i) => {
      const label = i === 0 ? "当日にもう一度" : `${BOX_DAYS[i - 1]} 日あけて言えた`;
      return `<i class="box-bar" style="--h:${n / boxMax}" title="${label}: ${n} 枚"><em>${n}</em></i>`;
    })
    .join("");
  dash.innerHTML = `
    <a class="dash-cell ${stats.due ? "is-due" : ""}" href="#lr">
      <b>${stats.due}</b><span>今日の復習</span>
    </a>
    <div class="dash-cell"><b>${streak}<small> 日</small></b><span>続けている日数</span></div>
    <div class="dash-cell"><b>${stats.rate === null ? "—" : `${stats.rate}<small>%</small>`}</b><span>言えた率（${stats.right + stats.wrong} 回中）</span></div>
    <div class="dash-cell"><b>${stats.held}</b><span>間をあけて言えた</span></div>
    <div class="dash-cell"><b>${stats.seen} / ${stats.total}</b><span>手をつけたカード</span></div>
    <div class="dash-cell quiet"><b>${readChunks}</b><span>読んだ塊</span></div>
  `;
  const boxes = document.querySelector("[data-boxes]");
  if (boxes) {
    boxes.innerHTML =
      `<p class="boxes-head">箱の分布<small>右へ行くほど長い間隔で言えたカード</small></p>` +
      `<div class="boxes-row">${boxBars}</div>` +
      `<p class="boxes-foot"><span>当日</span><span>1 日</span><span>3 日</span><span>7 日</span><span>16 日</span><span>35 日</span></p>`;
  }
}

function hashFor(id, chunk) {
  if (id === "00") return "#l00";
  if (chunk && chunk > 1) return `#l${id}/c${chunk}`;
  return `#l${id}`;
}

function parseHash() {
  const m = location.hash.match(/^#l(\d{2}|g|r)(?:\/c(\d+))?/);
  if (!m) return { id: "00", chunk: 1 };
  return { id: m[1], chunk: m[2] ? Number(m[2]) : 1 };
}

function renderRail(currentId) {
  const rail = document.querySelector("[data-rail]");
  if (!rail) return;
  const state = loadState();
  const due = dueCards().length;
  const items = LESSONS.filter((l) => !["00", "g", "r"].includes(l.id))
    .map((l) => {
      const current = l.id === currentId ? ' aria-current="page"' : "";
      const done = state.done[l.id] ? " done" : "";
      const total = document.querySelectorAll(`[data-view="${l.id}"] .step`).length;
      const read = Math.min(state.read[l.id] || 0, total);
      const ratio = total ? read / total : 0;
      return `<li><a class="${done.trim()}" href="${hashFor(l.id)}"${current} style="--p:${ratio}"><span class="num">${l.id}</span><span>${l.short}</span></a></li>`;
    })
    .join("");
  rail.innerHTML = `
    <a class="rail-brand" href="#l00">LLMO 教材<strong>思い出して覚える</strong></a>
    <nav aria-label="課の順">
      <ol>${items}</ol>
    </nav>
    <div class="rail-foot">
      <a class="rail-review${due ? " is-due" : ""}" href="#lr">復習${due ? `<b>${due}</b>` : ""}</a>
      <a href="#lg">用語集</a>
      <p class="kb">J / K で塊を移動 · A で全部表示</p>
    </div>
  `;
}

function showView(id) {
  document.querySelectorAll("[data-view]").forEach((el) => {
    const on = el.dataset.view === id;
    el.classList.toggle("is-on", on);
    el.hidden = !on;
  });
  document.body.dataset.lesson = id;
  const meta = LESSONS.find((l) => l.id === id);
  document.title = meta && id !== "00" ? `${meta.title} · LLMO` : "LLMO を思い出しながら読む";
  renderRail(id);
  if (id === "00") paintDash();
  if (id === "r") startReview();
}

let stepIndex = 0;
let stepNodes = [];

function bindSteps(id, startChunk) {
  const view = document.querySelector(`[data-view="${id}"]`);
  stepNodes = view ? [...view.querySelectorAll(".step")] : [];
  stepIndex = 0;
  if (!stepNodes.length) return;
  stepNodes.forEach((el) => el.setAttribute("tabindex", "-1"));
  stepIndex = Math.min(stepNodes.length - 1, Math.max(0, startChunk - 1));
  paintSteps(id, true);
}

function paintSteps(id, first) {
  const all = document.body.classList.contains("is-all");
  stepNodes.forEach((el, n) => {
    const on = n === stepIndex || all;
    el.classList.toggle("is-on", n === stepIndex);
    el.hidden = !on;
  });
  const meter = document.querySelector(`[data-view="${id}"] [data-meter]`);
  const prev = document.querySelector(`[data-view="${id}"] [data-prev]`);
  const next = document.querySelector(`[data-view="${id}"] [data-next]`);
  if (meter && stepNodes.length) {
    const ratio = (stepIndex + 1) / stepNodes.length;
    meter.innerHTML =
      `いま読む塊 <b>${stepIndex + 1}</b> / ${stepNodes.length}` +
      `<span class="bar" aria-hidden="true"><i style="transform:scaleX(${ratio})"></i></span>`;
  }
  if (prev) prev.disabled = stepIndex === 0;
  if (next) {
    next.disabled = false;
    next.textContent = stepIndex === stepNodes.length - 1 ? "この課を終える" : "次の塊";
  }
  if (stepNodes.length) {
    const nextHash = hashFor(id, stepIndex + 1);
    if (location.hash !== nextHash) {
      try {
        history.replaceState(null, "", nextHash);
      } catch {
        location.hash = nextHash;
      }
    }
    markProgress(id, stepIndex + 1, stepNodes.length);
  }
  if (!first && stepNodes[stepIndex]) {
    stepNodes[stepIndex].focus({ preventScroll: true });
    const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;
    window.scrollTo({ top: 0, behavior: reduce ? "instant" : "smooth" });
  }
}

function go(id, chunk) {
  hideFinish();
  document.body.classList.remove("is-all");
  const allBtn = document.querySelector(`[data-view="${id}"] [data-all]`);
  if (allBtn) allBtn.textContent = "全部見る";
  showView(id);
  bindSteps(id, chunk || 1);
}

function nextLesson(id) {
  const idx = LESSONS.findIndex((l) => l.id === id);
  const nxt = LESSONS[idx + 1];
  if (nxt) location.hash = hashFor(nxt.id);
}

function initControls() {
  document.addEventListener("click", (e) => {
    const reveal = e.target.closest("[data-reveal]");
    const grade = e.target.closest("[data-grade]");
    if (reveal) {
      openCard(reveal.closest(".card"));
      return;
    }
    if (grade) {
      const card = grade.closest(".card");
      const good = grade.dataset.grade === "good";
      const next = gradeCard(card.dataset.card, good);
      card.classList.add(good ? "is-good" : "is-again");
      paintSchedule(card, next);
      renderRail(document.body.dataset.lesson);
      if (document.body.classList.contains("is-finish")) paintFinish(document.body.dataset.lesson);
      if (card.closest(".review")) {
        advanceReview(card.dataset.card, good);
      }
      return;
    }

    const finishNext = e.target.closest("[data-finish-next]");
    const finishBack = e.target.closest("[data-finish-back]");
    if (finishNext) {
      const id = document.body.dataset.lesson;
      hideFinish();
      nextLesson(id);
      return;
    }
    if (finishBack) {
      hideFinish();
      paintSteps(document.body.dataset.lesson, false);
      return;
    }

    const prev = e.target.closest("[data-prev]");
    const nextBtn = e.target.closest("[data-next]");
    const allBtn = e.target.closest("[data-all]");
    const id = document.body.dataset.lesson;
    if (prev) {
      if (stepIndex > 0) {
        stepIndex -= 1;
        paintSteps(id, false);
      }
    }
    if (nextBtn) {
      if (stepIndex < stepNodes.length - 1) {
        stepIndex += 1;
        paintSteps(id, false);
      } else if (stepNodes.length) {
        markProgress(id, stepNodes.length, stepNodes.length);
        renderRail(id);
        showFinish(id);
      }
    }
    if (allBtn) {
      document.body.classList.toggle("is-all");
      allBtn.textContent = document.body.classList.contains("is-all") ? "一塊ずつに戻す" : "全部見る";
      paintSteps(id, true);
    }
  });

  document.addEventListener("keydown", (e) => {
    if (e.target.closest("textarea, input, summary, .term")) return;
    const id = document.body.dataset.lesson;
    if (document.body.classList.contains("is-finish")) {
      if (e.key === "j" || e.key === "ArrowRight") {
        e.preventDefault();
        document.querySelector("[data-finish-next]")?.click();
      }
      if (e.key === "k" || e.key === "ArrowLeft") {
        e.preventDefault();
        document.querySelector("[data-finish-back]")?.click();
      }
      return;
    }
    if (id === "r") {
      const card = document.querySelector(".review .card");
      if (!card) return;
      if (e.key === " ") {
        e.preventDefault();
        card.querySelector("[data-reveal]")?.click();
      }
      if (e.key === "1") card.querySelector('[data-grade="again"]')?.click();
      if (e.key === "2") card.querySelector('[data-grade="good"]')?.click();
      return;
    }
    if (e.key === "j" || e.key === "ArrowRight") {
      e.preventDefault();
      document.querySelector(`[data-view="${id}"] [data-next]`)?.click();
    }
    if (e.key === "k" || e.key === "ArrowLeft") {
      e.preventDefault();
      document.querySelector(`[data-view="${id}"] [data-prev]`)?.click();
    }
    if (e.key === "a") {
      document.querySelector(`[data-view="${id}"] [data-all]`)?.click();
    }
  });
}

function initCards() {
  document.querySelectorAll("[data-card]").forEach((el) => {
    const card = cardState(el.dataset.card);
    if (card) el.classList.add("is-known");
  });
}

function initTerms() {
  let pop;
  function hide() {
    pop?.remove();
    pop = null;
  }
  function show(el) {
    const text = TERMS[el.dataset.term];
    if (!text) return;
    hide();
    pop = document.createElement("div");
    pop.className = "term-pop";
    pop.id = "term-pop";
    pop.setAttribute("role", "tooltip");
    pop.textContent = text;
    document.body.appendChild(pop);
    el.setAttribute("aria-describedby", "term-pop");
    const r = el.getBoundingClientRect();
    const w = Math.min(288, innerWidth - 24);
    let left = Math.min(Math.max(12, r.left), innerWidth - w - 12);
    let top = r.bottom + 8;
    pop.style.left = left + "px";
    pop.style.top = top + "px";
    const h = pop.offsetHeight;
    if (top + h > innerHeight - 12) {
      pop.style.top = Math.max(12, r.top - h - 8) + "px";
    }
  }
  document.querySelectorAll("[data-term]").forEach((el) => {
    el.classList.add("term");
    el.tabIndex = 0;
    el.setAttribute("role", "button");
    el.addEventListener("mouseenter", () => show(el));
    el.addEventListener("mouseleave", hide);
    el.addEventListener("focus", () => show(el));
    el.addEventListener("blur", hide);
    el.addEventListener("keydown", (e) => {
      if (e.key === "Escape") {
        hide();
        el.blur();
      }
    });
  });
}

function applyHash() {
  const { id, chunk } = parseHash();
  go(id, chunk);
}

window.addEventListener("hashchange", applyHash);
initControls();
initCards();
initTerms();
applyHash();
