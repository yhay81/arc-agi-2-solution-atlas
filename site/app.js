const COLORS = ["#000", "#0074d9", "#ff4136", "#2ecc40", "#ffdc00", "#aaaaaa", "#f012be", "#ff851b", "#7fdbff", "#870c25"];

const state = { tasks: [], query: "", split: "all", selected: null };
const list = document.querySelector("#task-list");
const view = document.querySelector("#task-view");

function gridElement(grid) {
  const element = document.createElement("div");
  element.className = "grid";
  element.style.gridTemplateColumns = `repeat(${grid[0].length}, 1fr)`;
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

function renderTask(task) {
  state.selected = task.id;
  history.replaceState(null, "", `#${task.id}`);
  view.replaceChildren();
  const header = document.createElement("header");
  header.className = "task-header";
  header.innerHTML = `<h2>${task.id}</h2><div class="badges"><span class="badge">${task.split}</span>${task.concepts.map(value => `<span class="badge">${value}</span>`).join("")}</div>`;
  const rule = document.createElement("pre");
  rule.className = "rule";
  rule.textContent = task.documentation;
  const pairs = document.createElement("section");
  pairs.className = "pairs";
  for (const split of ["train", "test"]) task.task[split].forEach((pair, index) => {
    const item = document.createElement("section");
    item.className = "pair";
    item.innerHTML = `<h3>${split} ${index + 1}</h3>`;
    const grids = document.createElement("div");
    grids.className = "grids";
    grids.append(gridElement(pair.input));
    const arrow = document.createElement("span");
    arrow.className = "arrow";
    arrow.textContent = "→";
    grids.append(arrow, gridElement(pair.output));
    item.append(grids);
    pairs.append(item);
  });
  view.append(header, rule, pairs);
  renderList();
}

function filteredTasks() {
  const query = state.query.toLowerCase();
  return state.tasks.filter(task =>
    (state.split === "all" || task.split === state.split) &&
    `${task.id} ${task.documentation} ${task.concepts.join(" ")}`.toLowerCase().includes(query)
  );
}

function renderList() {
  const tasks = filteredTasks();
  document.querySelector("#result-count").textContent = `${tasks.length} RESULTS`;
  list.replaceChildren(...tasks.map(task => {
    const button = document.createElement("button");
    button.className = `task-link${task.id === state.selected ? " active" : ""}`;
    button.innerHTML = `<strong>${task.id}</strong><span>${task.concepts.slice(0, 3).join(" · ")}</span>`;
    button.addEventListener("click", () => renderTask(task));
    return button;
  }));
}

document.querySelector("#search").addEventListener("input", event => {
  state.query = event.target.value;
  renderList();
});
document.querySelectorAll(".filter").forEach(button => button.addEventListener("click", () => {
  document.querySelectorAll(".filter").forEach(item => item.classList.remove("active"));
  button.classList.add("active");
  state.split = button.dataset.split;
  renderList();
}));

fetch("catalog.json").then(response => response.json()).then(catalog => {
  state.tasks = catalog.tasks;
  document.querySelector("#task-count").textContent = catalog.tasks.length.toLocaleString();
  document.querySelector("#pair-count").textContent = catalog.pair_count.toLocaleString();
  renderList();
  const requested = location.hash.slice(1);
  renderTask(state.tasks.find(task => task.id === requested) || state.tasks[0]);
});

