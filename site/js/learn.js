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
};

const STORE = "llmo-learn-v1";

function loadState() {
  try {
    return JSON.parse(localStorage.getItem(STORE) || "{}");
  } catch {
    return {};
  }
}

function saveState(state) {
  localStorage.setItem(STORE, JSON.stringify(state));
}

function markProgress(id, chunk, total) {
  const state = loadState();
  state[id] = Math.max(state[id] || 0, chunk);
  if (chunk >= total) state.done = Object.assign({}, state.done, { [id]: true });
  saveState(state);
}

function hashFor(id, chunk) {
  if (id === "00") return "#l00";
  if (chunk && chunk > 1) return `#l${id}/c${chunk}`;
  return `#l${id}`;
}

function parseHash() {
  const m = location.hash.match(/^#l(\d{2}|g)(?:\/c(\d+))?/);
  if (!m) return { id: "00", chunk: 1 };
  return { id: m[1], chunk: m[2] ? Number(m[2]) : 1 };
}

function renderRail(currentId) {
  const rail = document.querySelector("[data-rail]");
  if (!rail) return;
  const state = loadState();
  const items = LESSONS.filter((l) => l.id !== "00" && l.id !== "g")
    .map((l) => {
      const current = l.id === currentId ? ' aria-current="page"' : "";
      const done = state.done && state.done[l.id] ? " done" : "";
      return `<li><a class="${done.trim()}" href="${hashFor(l.id)}"${current}><span class="num">${l.id}</span><span>${l.short}</span></a></li>`;
    })
    .join("");
  rail.innerHTML = `
    <a class="rail-brand" href="#l00">LLMO 教材<strong>一塊ずつ読む</strong></a>
    <nav aria-label="課の順">
      <ol>${items}</ol>
    </nav>
    <div class="rail-foot">
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
  document.title = meta && id !== "00" ? `${meta.title} · LLMO` : "LLMO を一塊ずつ読む";
  renderRail(id);
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
    meter.innerHTML = `いま読む塊 <b>${stepIndex + 1}</b> / ${stepNodes.length}`;
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
    const prev = e.target.closest("[data-prev]");
    const next = e.target.closest("[data-next]");
    const allBtn = e.target.closest("[data-all]");
    const id = document.body.dataset.lesson;
    if (prev) {
      if (stepIndex > 0) {
        stepIndex -= 1;
        paintSteps(id, false);
      }
    }
    if (next) {
      if (stepIndex < stepNodes.length - 1) {
        stepIndex += 1;
        paintSteps(id, false);
      } else if (stepNodes.length) {
        markProgress(id, stepNodes.length, stepNodes.length);
        nextLesson(id);
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
initTerms();
applyHash();
