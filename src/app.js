/* Infosec House 3.0 progressive enhancement only; every page works without JS. */
(() => {
  const $ = (s, el = document) => el.querySelector(s);
  const $$ = (s, el = document) => [...el.querySelectorAll(s)];
  const store = {
    get: (k) => { try { return localStorage.getItem(k); } catch { return null; } },
    set: (k, v) => { try { localStorage.setItem(k, v); } catch {} },
  };

  /* ---------- mobile nav ---------- */
  const menuBtn = $('[data-menu]');
  menuBtn?.addEventListener('click', () => {
    const open = $('#nav').classList.toggle('open');
    menuBtn.setAttribute('aria-expanded', String(open));
  });

  /* ---------- search ---------- */
  let index = null;
  let loading = null;
  const loadIndex = () => loading ||= fetch('/api/search.json')
    .then((r) => r.json())
    .then((rows) => (index = rows.map((r) => ({
      kind: r[0], name: r[1], desc: r[2], sub: r[3], cat: r[4], where: r[5], path: r[6],
      hay: `${r[1]} ${r[2]} ${r[3]} ${r[4]} ${r[5]}`.toLowerCase(), lname: r[1].toLowerCase(),
    }))));

  const esc = (s) => String(s ?? '').replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const highlight = (text, terms) => {
    let out = esc(text);
    for (const t of terms) {
      if (t.length < 2) continue;
      out = out.replace(new RegExp(`(${t.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')})`, 'ig'), '<mark>$1</mark>');
    }
    return out;
  };

  function query(q) {
    const terms = q.toLowerCase().split(/\s+/).filter(Boolean);
    if (!terms.length || !index) return [];
    const hits = [];
    for (const item of index) {
      if (!terms.every((t) => item.hay.includes(t))) continue;
      let score = item.kind === 'c' ? 40 : 0;
      const full = terms.join(' ');
      if (item.lname === full) score += 100;
      else if (item.lname.startsWith(full)) score += 60;
      else if (item.lname.includes(full)) score += 35;
      for (const t of terms) if (item.lname.includes(t)) score += 10;
      hits.push([score, item]);
    }
    return hits.sort((a, b) => b[0] - a[0] || a[1].name.localeCompare(b[1].name)).slice(0, 30).map((h) => h[1]);
  }

  function mountSearch(input, results) {
    let active = -1;
    const render = () => {
      const q = input.value.trim();
      active = -1;
      if (!q) { results.innerHTML = ''; return; }
      if (!index) { loadIndex().then(render); return; }
      const terms = q.toLowerCase().split(/\s+/);
      const hits = query(q);
      results.innerHTML = hits.length
        ? hits.map((h) => `<a class="result" href="${esc(h.path)}" role="option">
            <div class="result-top">${h.kind === 'c' ? '<span class="result-kind">Category</span>' : ''}<strong>${highlight(h.name, terms)}</strong>
            <span class="where">${esc(h.kind === 'c' ? '' : h.cat + (h.where ? ' › ' + h.where : ''))}</span></div>
            <p>${highlight(h.desc || h.sub, terms)}</p></a>`).join('')
        : `<div class="search-empty">No matches for “${esc(q)}”. Try a broader term.</div>`;
      results.setAttribute('role', 'listbox');
    };
    input.addEventListener('focus', loadIndex, { once: true });
    input.addEventListener('input', render);
    input.addEventListener('keydown', (ev) => {
      const items = $$('.result', results);
      if (ev.key === 'ArrowDown' || ev.key === 'ArrowUp') {
        ev.preventDefault();
        if (!items.length) return;
        active = (active + (ev.key === 'ArrowDown' ? 1 : -1) + items.length) % items.length;
        items.forEach((el, i) => el.setAttribute('aria-selected', String(i === active)));
        items[active].scrollIntoView({ block: 'nearest' });
      } else if (ev.key === 'Enter') {
        const target = items[Math.max(active, 0)];
        if (target) { ev.preventDefault(); location.href = target.href; }
      } else if (ev.key === 'Escape' && !input.closest('dialog')) {
        input.value = ''; render(); input.blur();
      }
    });
    // Same-page anchor results: close the palette so the highlighted row is visible
    results.addEventListener('click', () => $('#palette')?.open && $('#palette').close());
  }

  $$('[data-search-input]').forEach((input) => mountSearch(input, $('[data-search-results]', input.closest('.hero-search, .palette-box'))));

  const palette = $('#palette');
  const heroInput = $('.hero-search [data-search-input]');
  const openSearch = () => {
    if (heroInput) { heroInput.focus(); heroInput.scrollIntoView({ block: 'center', behavior: 'smooth' }); return; }
    palette.showModal();
    $('[data-search-input]', palette).focus();
    loadIndex();
  };
  $$('[data-open-search]').forEach((b) => b.addEventListener('click', openSearch));
  // SEO SearchAction: open search when arriving with ?q=
  try {
    const q = new URLSearchParams(location.search).get('q');
    if (q && heroInput) { heroInput.value = q; heroInput.dispatchEvent(new Event('input')); heroInput.focus(); }
    else if (q) { openSearch(); const pi = $('[data-search-input]', palette); if (pi) { pi.value = q; pi.dispatchEvent(new Event('input')); } }
  } catch (e) {}

  palette?.addEventListener('click', (ev) => { if (ev.target === palette) palette.close(); });
  document.addEventListener('keydown', (ev) => {
    const typing = /^(INPUT|TEXTAREA|SELECT)$/.test(document.activeElement?.tagName);
    if ((ev.key === '/' && !typing) || (ev.key === 'k' && (ev.metaKey || ev.ctrlKey))) {
      ev.preventDefault();
      openSearch();
    }
  });
  document.addEventListener('click', (ev) => {
    if (!ev.target.closest('.hero-search')) $$('.hero-search [data-search-results]').forEach((r) => (r.innerHTML = ''));
  });

  /* ---------- card grids (home categories, vendors) ---------- */
  const cards = $('[data-cards]');
  if (cards) {
    const filter = $('[data-card-filter]');
    const sort = $('[data-card-sort]');
    const empty = $('[data-empty]');
    let group = '';
    const apply = () => {
      const q = (filter?.value || '').toLowerCase().trim();
      let shown = 0;
      for (const c of cards.children) {
        const ok = (!group || c.dataset.group === group) && (!q || c.dataset.search.includes(q));
        c.hidden = !ok;
        shown += ok;
      }
      if (empty) empty.hidden = shown > 0;
    };
    const order = () => {
      const by = sort.value;
      const items = [...cards.children].sort((a, b) => by === 'count'
        ? b.dataset.count - a.dataset.count
        : a.dataset.name.localeCompare(b.dataset.name));
      cards.append(...items);
      store.set(`ih-sort:${location.pathname}`, by);
    };
    filter?.addEventListener('input', apply);
    if (sort) {
      sort.value = store.get(`ih-sort:${location.pathname}`) || 'name';
      sort.addEventListener('change', order);
      order();
    }
    $$('[data-group]', $('.tabs') || document).filter((b) => b.tagName === 'BUTTON').forEach((btn) => {
      btn.addEventListener('click', () => {
        group = btn.dataset.group;
        $$('.tabs [data-group]').forEach((b) => b.setAttribute('aria-pressed', String(b === btn)));
        apply();
      });
    });
  }

  /* ---------- code copy buttons ---------- */
  $$('[data-copy]').forEach((btn) => btn.addEventListener('click', async () => {
    const code = btn.closest('.code').querySelector('code').innerText;
    try { await navigator.clipboard.writeText(code); btn.textContent = 'Copied'; } catch { btn.textContent = 'Press ⌘C'; }
    setTimeout(() => (btn.textContent = 'Copy'), 1500);
  }));

  /* ---------- category table ---------- */
  const rows = $('[data-rows]');
  if (rows) {
    // Whole row opens the tool page; links inside the row and text selection keep working
    rows.addEventListener('click', (ev) => {
      const tr = ev.target.closest('tr[data-href]');
      if (!tr || ev.target.closest('a, button') || String(getSelection())) return;
      if (ev.metaKey || ev.ctrlKey) window.open(tr.dataset.href, '_blank');
      else location.href = tr.dataset.href;
    });
    const filter = $('[data-row-filter]');
    const count = $('[data-row-count]');
    const desc = $('[data-tab-desc]');
    const empty = $('[data-empty]');
    const tabs = $$('[data-tab]');
    let tab = '';
    const apply = () => {
      const terms = (filter.value || '').toLowerCase().split(/\s+/).filter(Boolean);
      let shown = 0;
      for (const r of rows.children) {
        const ok = (!tab || r.dataset.section.split(' ').includes(tab)) && terms.every((t) => r.dataset.search.includes(t));
        r.hidden = !ok;
        shown += ok;
      }
      count.textContent = shown;
      empty.hidden = shown > 0;
    };
    const select = (btn, push) => {
      tab = btn.dataset.tab;
      tabs.forEach((b) => b.setAttribute('aria-pressed', String(b === btn)));
      desc.textContent = btn.dataset.desc || '';
      desc.hidden = !btn.dataset.desc;
      if (push) history.replaceState(null, '', tab ? `#s/${tab}` : location.pathname);
      apply();
    };
    tabs.forEach((b) => b.addEventListener('click', () => select(b, true)));
    filter.addEventListener('input', apply);
    const fromHash = location.hash.startsWith('#s/') && tabs.find((b) => b.dataset.tab === location.hash.slice(3));
    if (fromHash) select(fromHash, false);
  }
})();
