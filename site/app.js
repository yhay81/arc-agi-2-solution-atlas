const COLORS = ["#000", "#0074d9", "#ff4136", "#2ecc40", "#ffdc00", "#aaa", "#f012be", "#ff851b", "#7fdbff", "#870c25"];
let tasks = [];
let currentIndex = 0;

function gridElement(grid) {
  const longestSide = Math.max(grid.length, grid[0].length);
  const cellSize = Math.max(7, Math.min(26, Math.floor(280 / longestSide)));
  const element = document.createElement("div");
  element.className = "grid";
  element.style.gridTemplateColumns = `repeat(${grid[0].length}, ${cellSize}px)`;
  element.style.setProperty("--cell-size", `${cellSize}px`);
  element.setAttribute("aria-label", `${grid.length} by ${grid[0].length} grid`);
  for (const row of grid) for (const value of row) {
    const cell = document.createElement("span");
    cell.className = "cell";
    cell.style.background = COLORS[value];
    cell.title = String(value);
    element.append(cell);
  }
  return element;
}

function pairElement(pair, label) {
  const card = document.createElement("article");
  card.className = "pair";
  const title = document.createElement("h3");
  title.className = "pair-title";
  title.textContent = `${label} · INPUT → OUTPUT`;
  const grids = document.createElement("div");
  grids.className = "grids";
  grids.append(gridElement(pair.input));
  const arrow = document.createElement("span");
  arrow.className = "arrow";
  arrow.textContent = "→";
  grids.append(arrow, gridElement(pair.output));
  card.append(title, grids);
  return card;
}

function groupElement(title, pairs, prefix) {
  const section = document.createElement("section");
  const heading = document.createElement("h2");
  heading.className = "group-title";
  heading.textContent = title;
  const list = document.createElement("div");
  list.className = "pairs";
  list.append(...pairs.map((pair, index) => pairElement(pair, `${prefix} ${index + 1}`)));
  section.append(heading, list);
  return section;
}

function render(index) {
  currentIndex = Math.max(0, Math.min(tasks.length - 1, index));
  const item = tasks[currentIndex];
  history.replaceState(null, "", `#${item.id}`);
  document.title = `${item.id} · ARC-AGI-2 Solution Atlas`;
  document.querySelector("#position").textContent = `TASK ${item.id.toUpperCase()} · ${currentIndex + 1} / ${tasks.length}`;
  document.querySelector("#dataset").textContent = `ARC-AGI-2 PUBLIC ${item.split.toUpperCase()}`;
  document.querySelector("#task-id").value = item.id;
  document.querySelector("#previous").disabled = currentIndex === 0;
  document.querySelector("#next").disabled = currentIndex === tasks.length - 1;

  const view = document.querySelector("#task-view");
  view.replaceChildren();
  const title = document.createElement("h1");
  title.className = "task-title";
  title.textContent = `Task ${item.id}`;
  const boards = document.createElement("div");
  boards.className = "boards";
  boards.append(
    groupElement("EXAMPLES", item.task.train, "EXAMPLE"),
    groupElement("TEST", item.task.test, "TEST"),
  );
  const reference = document.createElement("div");
  reference.className = "reference";
  const notesSection = document.createElement("section");
  notesSection.innerHTML = "<h2>SOLUTION NOTES</h2>";
  const concepts = document.createElement("div");
  concepts.className = "concepts";
  for (const value of item.concepts) {
    const concept = document.createElement("span");
    concept.className = "concept";
    concept.textContent = value;
    concepts.append(concept);
  }
  const documentation = document.createElement("pre");
  documentation.className = "notes";
  documentation.textContent = item.documentation;
  notesSection.append(concepts, documentation);
  const programSection = document.createElement("section");
  programSection.innerHTML = "<h2>PYTHON PROGRAM</h2>";
  const program = document.createElement("pre");
  const code = document.createElement("code");
  code.textContent = item.program;
  program.append(code);
  programSection.append(program);
  reference.append(notesSection, programSection);
  view.append(title, boards, reference);
}

function renderIndex(query = "") {
  const normalized = query.toLowerCase();
  const matches = tasks.filter(item =>
    `${item.id} ${item.split} ${item.concepts.join(" ")}`.toLowerCase().includes(normalized)
  );
  document.querySelector("#index-count").textContent = `${matches.length} of ${tasks.length} tasks`;
  const buttons = matches.map(item => {
    const button = document.createElement("button");
    button.className = "index-item";
    button.innerHTML = `<strong>${item.id}</strong><span>${item.split.toUpperCase()}</span><span>${item.concepts.join(" · ")}</span>`;
    button.addEventListener("click", () => {
      render(tasks.indexOf(item));
      document.querySelector("#task-index").close();
    });
    return button;
  });
  document.querySelector("#index-grid").replaceChildren(...buttons);
}

document.querySelector("#previous").addEventListener("click", () => render(currentIndex - 1));
document.querySelector("#next").addEventListener("click", () => render(currentIndex + 1));
document.querySelector("#open-index").addEventListener("click", () => {
  renderIndex();
  document.querySelector("#task-index").showModal();
  document.querySelector("#index-search").focus();
});
document.querySelector("#close-index").addEventListener("click", () => document.querySelector("#task-index").close());
document.querySelector("#index-search").addEventListener("input", event => renderIndex(event.target.value));
document.addEventListener("keydown", event => {
  if (document.querySelector("#task-index").open || document.activeElement.matches("input")) return;
  if (event.key === "ArrowLeft" && currentIndex > 0) render(currentIndex - 1);
  if (event.key === "ArrowRight" && currentIndex < tasks.length - 1) render(currentIndex + 1);
});
document.querySelector("#task-search").addEventListener("submit", event => {
  event.preventDefault();
  const taskId = document.querySelector("#task-id").value.toLowerCase();
  const index = tasks.findIndex(item => item.id === taskId);
  if (index >= 0) render(index);
});

fetch("catalog.json").then(response => response.json()).then(catalog => {
  tasks = catalog.tasks;
  const options = tasks.map(item => {
    const option = document.createElement("option");
    option.value = item.id;
    return option;
  });
  document.querySelector("#task-ids").append(...options);
  const requested = location.hash.slice(1);
  const index = tasks.findIndex(item => item.id === requested);
  render(index >= 0 ? index : 0);
});
