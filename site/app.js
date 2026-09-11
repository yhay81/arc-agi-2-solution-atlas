const COLORS = ["#000", "#0074d9", "#ff4136", "#2ecc40", "#ffdc00", "#aaa", "#f012be", "#ff851b", "#7fdbff", "#870c25"];
const COLOR_NAMES = ["black", "blue", "red", "green", "yellow", "gray", "magenta", "orange", "light blue", "maroon"];
let tasks = [];
let currentIndex = 0;

function gridElement(grid, label) {
  const longestSide = Math.max(grid.length, grid[0].length);
  const cellSize = Math.max(7, Math.min(26, Math.floor(280 / longestSide)));
  const element = document.createElement("div");
  element.className = "grid";
  element.style.gridTemplateColumns = `repeat(${grid[0].length}, ${cellSize}px)`;
  element.style.setProperty("--cell-size", `${cellSize}px`);
  const rows = grid.map(row => row.map(value => COLOR_NAMES[value]).join(", ")).join("; ");
  element.setAttribute("role", "img");
  element.setAttribute("aria-label", `${label}: ${grid.length} rows by ${grid[0].length} columns. Colors by row: ${rows}.`);
  for (const row of grid) for (const value of row) {
    const cell = document.createElement("span");
    cell.className = "cell";
    cell.style.background = COLORS[value];
    cell.title = `${value} · ${COLOR_NAMES[value]}`;
    cell.setAttribute("aria-hidden", "true");
    element.append(cell);
  }
  return element;
}

function pairElement(pair, label) {
  const card = document.createElement("article");
  card.className = "pair";
  const title = document.createElement("h3");
  title.className = "pair-title";
  title.textContent = label;
  const grids = document.createElement("div");
  grids.className = "grids";
  grids.append(gridElement(pair.input, `${label} input`));
  const arrow = document.createElement("span");
  arrow.className = "arrow";
  arrow.textContent = "→";
  arrow.setAttribute("aria-hidden", "true");
  grids.append(arrow, gridElement(pair.output, `${label} output`));
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
    groupElement("Examples", item.task.train, "Example"),
    groupElement("Test", item.task.test, "Test"),
  );
  const reference = document.createElement("div");
  reference.className = "reference";
  const notesSection = document.createElement("section");
  const notesHeading = document.createElement("h2");
  notesHeading.textContent = "Solution notes";
  notesSection.append(notesHeading);
  const concepts = document.createElement("div");
  concepts.className = "concepts";
  concepts.setAttribute("role", "list");
  concepts.setAttribute("aria-label", "Concepts");
  for (const value of item.concepts) {
    const concept = document.createElement("span");
    concept.className = "concept";
    concept.setAttribute("role", "listitem");
    concept.textContent = value;
    concepts.append(concept);
  }
  const documentation = document.createElement("pre");
  documentation.className = "notes";
  documentation.textContent = item.documentation;
  notesSection.append(concepts, documentation);
  const programSection = document.createElement("section");
  const programHeading = document.createElement("h2");
  programHeading.textContent = "Python transformation";
  programSection.append(programHeading);
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
    const id = document.createElement("strong");
    id.textContent = item.id;
    const split = document.createElement("span");
    split.textContent = item.split.toUpperCase();
    const concepts = document.createElement("span");
    concepts.textContent = item.concepts.join(" · ");
    button.append(id, split, concepts);
    button.addEventListener("click", () => {
      render(tasks.indexOf(item));
      document.querySelector("#task-index").close();
    });
    return button;
  });
  if (buttons.length === 0) {
    const empty = document.createElement("p");
    empty.className = "index-empty";
    empty.textContent = "No matching tasks.";
    buttons.push(empty);
  }
  document.querySelector("#index-grid").replaceChildren(...buttons);
}

document.querySelector("#previous").addEventListener("click", () => render(currentIndex - 1));
document.querySelector("#next").addEventListener("click", () => render(currentIndex + 1));
document.querySelector(".skip-link").addEventListener("click", event => {
  event.preventDefault();
  document.querySelector("#task-view").focus();
});
document.querySelector("#open-index").addEventListener("click", () => {
  document.querySelector("#index-search").value = "";
  renderIndex();
  document.querySelector("#task-index").showModal();
  document.querySelector("#index-search").focus();
});
document.querySelector("#close-index").addEventListener("click", () => document.querySelector("#task-index").close());
document.querySelector("#index-search").addEventListener("input", event => renderIndex(event.target.value));
document.addEventListener("keydown", event => {
  const isInteractive = event.target instanceof Element && event.target.closest("button, input, a");
  if (document.querySelector("#task-index").open || isInteractive) return;
  if (event.key === "ArrowLeft" && currentIndex > 0) render(currentIndex - 1);
  if (event.key === "ArrowRight" && currentIndex < tasks.length - 1) render(currentIndex + 1);
});
document.querySelector("#task-search").addEventListener("submit", event => {
  event.preventDefault();
  const taskId = document.querySelector("#task-id").value.trim().toLowerCase();
  const index = tasks.findIndex(item => item.id === taskId);
  const status = document.querySelector("#task-search-status");
  if (index >= 0) {
    status.textContent = "";
    render(index);
  } else {
    status.textContent = `Task ${taskId || "ID"} was not found.`;
  }
});

fetch("catalog.json").then(response => {
  if (!response.ok) throw new Error(`Catalog request failed with status ${response.status}`);
  return response.json();
}).then(catalog => {
  tasks = catalog.tasks;
  const options = tasks.map(item => {
    const option = document.createElement("option");
    option.value = item.id;
    return option;
  });
  document.querySelector("#task-ids").append(...options);
  document.querySelector("#open-index").disabled = false;
  const requested = location.hash.slice(1);
  const index = tasks.findIndex(item => item.id === requested);
  render(index >= 0 ? index : 0);
}).catch(() => {
  const error = document.createElement("p");
  error.className = "loading";
  error.setAttribute("role", "alert");
  error.textContent = "The task catalog could not be loaded. Please refresh the page to try again.";
  document.querySelector("#task-view").replaceChildren(error);
});
