// Search (press / anywhere), hover meanings for words, and the dictionary's filter and sort.
// Every page reads fine without this file.
(function () {
  // Light/dark toggle: starts from the system setting, remembers a choice.
  var tb = document.getElementById("theme"), root = document.documentElement;
  function dark() {
    return root.dataset.theme ? root.dataset.theme === "dark" : matchMedia("(prefers-color-scheme: dark)").matches;
  }
  function label() { tb.textContent = dark() ? "light" : "dark"; }
  tb.hidden = false; label();
  tb.addEventListener("click", function () {
    root.dataset.theme = dark() ? "light" : "dark";
    try { localStorage.setItem("theme", root.dataset.theme); } catch (e) {}
    label();
  });

  var data = null, waiting = [];
  function load(cb) {
    if (data) return cb(data);
    waiting.push(cb);
    if (waiting.length > 1) return;
    fetch("index.json").then(function (r) { return r.json(); }).then(function (d) {
      data = d; waiting.forEach(function (f) { f(d); });
    });
  }
  function esc(s) { return s.replace(/[&<>"]/g, function (c) { return {"&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;"}[c]; }); }

  // Rank: exact word or title first, then title prefix, then title contains, then text contains.
  function search(q, d, max) {
    q = q.trim().toLowerCase();
    if (!q) return [];
    var scored = [];
    d.pages.forEach(function (e) {
      var t = e.t.toLowerCase(), x = e.x.toLowerCase(), s = 0;
      if (t === q || x === q) s = 4;
      else if (t.indexOf(q) === 0) s = 3;
      else if (t.indexOf(q) >= 0) s = 2;
      else if (new RegExp("\\b" + q.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")).test(x)) s = 1;
      if (s) scored.push([s, e]);
    });
    scored.sort(function (a, b) { return b[0] - a[0]; });
    return scored.slice(0, max).map(function (p) { return p[1]; });
  }
  function item(e, q) {
    var x = e.x, i = x.toLowerCase().indexOf(q.toLowerCase());
    var snip = i < 0 ? x.slice(0, 90) : (i > 40 ? "…" : "") + x.slice(Math.max(0, i - 40), i + 60);
    return '<li><a href="' + e.u + '"><b>' + esc(e.t) + "</b> <small>" + (e.p === e.t ? "" : esc(e.p)) + "</small><br><small>" + esc(snip) + "</small></a></li>";
  }

  var q = document.getElementById("q"), hits = document.getElementById("hits"), sel = -1;
  function show() {
    load(function (d) {
      var r = search(q.value, d, 12);
      hits.innerHTML = r.map(function (e) { return item(e, q.value.trim()); }).join("");
      hits.hidden = !r.length; sel = -1;
    });
  }
  function mark() {
    [].forEach.call(hits.children, function (li, i) { li.className = i === sel ? "on" : ""; });
    if (hits.children[sel]) hits.children[sel].scrollIntoView({block: "nearest"});
  }
  q.addEventListener("input", show);
  q.addEventListener("focus", function () { load(function () {}); });
  q.addEventListener("keydown", function (ev) {
    var n = hits.children.length;
    if (ev.key === "ArrowDown") { sel = (sel + 1) % n; mark(); ev.preventDefault(); }
    else if (ev.key === "ArrowUp") { sel = (sel - 1 + n) % n; mark(); ev.preventDefault(); }
    else if (ev.key === "Enter" && n) { location.href = hits.children[Math.max(sel, 0)].querySelector("a").href; ev.preventDefault(); }
    else if (ev.key === "Escape") { q.value = ""; hits.hidden = true; q.blur(); }
  });
  document.addEventListener("click", function (ev) { if (!q.form.contains(ev.target)) hits.hidden = true; });
  document.addEventListener("keydown", function (ev) {
    var tag = (ev.target.tagName || "").toLowerCase();
    if (ev.key === "/" && tag !== "input" && tag !== "select" && tag !== "textarea") { ev.preventDefault(); q.focus(); q.select(); }
  });

  // search.html?q=...: full results (the form's no-dropdown fallback)
  var results = document.getElementById("results");
  if (results) {
    var term = new URLSearchParams(location.search).get("q") || "";
    q.value = term;
    load(function (d) {
      var r = search(term, d, 200);
      results.innerHTML = r.length ? r.map(function (e) { return item(e, term); }).join("") : "<li>No results.</li>";
    });
  }

  // Hover meanings: a bold run made only of known words gets their meanings as a tooltip.
  load(function (d) {
    [].forEach.call(document.querySelectorAll("main b, main strong"), function (el) {
      if (el.closest("th, h1, h2, h3, table.dict")) return;
      var ws = el.textContent.toLowerCase().replace(/[.,?!:;…"]/g, " ").trim().split(/\s+/);
      if (!ws[0] || !ws.every(function (w) { return d.words[w]; })) return;
      el.title = ws.map(function (w) { return w + ": " + d.words[w]; }).join("\n");
    });
  });

  // Example texts: every known word in a paragraph marked {.apu} shows its meaning on hover or tap.
  var apu = document.querySelectorAll(".apu");
  if (apu.length) load(function (d) {
    var tip = document.createElement("div");
    tip.id = "tip"; tip.hidden = true; document.body.appendChild(tip);
    [].forEach.call(apu, function (el) {
      var walk = document.createTreeWalker(el, NodeFilter.SHOW_TEXT), nodes = [];
      while (walk.nextNode()) nodes.push(walk.currentNode);
      nodes.forEach(function (n) {
        var frag = document.createDocumentFragment();
        n.textContent.split(/([a-z]+)/).forEach(function (part) {
          if (d.words[part]) {
            var w = document.createElement("span");
            w.className = "w"; w.textContent = part; w.title = d.words[part];
            frag.appendChild(w);
          } else frag.appendChild(document.createTextNode(part));
        });
        n.parentNode.replaceChild(frag, n);
      });
    });
    document.addEventListener("click", function (ev) {
      var w = ev.target.closest && ev.target.closest(".w");
      if (!w) { tip.hidden = true; return; }
      var r = w.getBoundingClientRect();
      tip.textContent = w.textContent + ": " + w.title;
      tip.style.left = Math.max(4, Math.min(r.left + scrollX, scrollX + innerWidth - 260)) + "px";
      tip.style.top = (r.bottom + scrollY + 4) + "px";
      tip.hidden = false;
    });
  });

  // Dictionary: filter as you type, by topic, and sort any table by clicking its heading.
  var f = document.getElementById("dict-filter"), field = document.getElementById("dict-field");
  if (f) {
    var rows = [].slice.call(document.querySelectorAll("table.dict tbody tr")), count = document.getElementById("dict-count");
    var apply = function () {
      var v = f.value.trim().toLowerCase(), t = field.value, n = 0;
      rows.forEach(function (r) {
        var ok = (!t || r.dataset.f === t) && (!v || r.textContent.toLowerCase().indexOf(v) >= 0);
        r.hidden = !ok; n += ok;
      });
      count.textContent = n + " shown";
      history.replaceState(null, "", v || t ? "#" + encodeURIComponent(v) + (t ? "@" + t : "") : location.pathname);
    };
    f.addEventListener("input", apply); field.addEventListener("change", apply);
    var h = decodeURIComponent(location.hash.slice(1));
    if (h && !document.getElementById(h)) { f.value = h.split("@")[0]; field.value = h.split("@")[1] || ""; }
    apply();
  }
  [].forEach.call(document.querySelectorAll("table.sortable th"), function (th, col) {
    th.addEventListener("click", function () {
      var tb = th.closest("table").tBodies[0], asc = th.getAttribute("aria-sort") !== "ascending";
      [].forEach.call(th.parentNode.children, function (o) { o.removeAttribute("aria-sort"); });
      th.setAttribute("aria-sort", asc ? "ascending" : "descending");
      var rs = [].slice.call(tb.rows);
      rs.sort(function (a, b) {
        var x = a.cells[col].textContent, y = b.cells[col].textContent;
        var c = isNaN(x) || isNaN(y) || x === "" || y === "" ? x.localeCompare(y) : x - y;
        return asc ? c : -c;
      });
      rs.forEach(function (r) { tb.appendChild(r); });
    });
  });
})();
