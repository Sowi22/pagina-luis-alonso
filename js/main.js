/* Dr. Luis Alonso Salja — interacciones (sin librerías) */
(function () {
  const $ = (s, c = document) => c.querySelector(s);
  const $$ = (s, c = document) => [...c.querySelectorAll(s)];
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const WA_NUMBER = '573022841740';

  /* Header: fondo al hacer scroll y se oculta al bajar */
  const header = $('.header');
  let lastY = 0;
  const onScroll = () => {
    const y = window.scrollY;
    header.classList.toggle('is-scrolled', y > 30);
    header.classList.toggle('is-hidden', y > 500 && y > lastY && !document.body.classList.contains('menu-open'));
    lastY = y;
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* Menú móvil */
  const drawer = $('.drawer');
  const burger = $('.burger');
  const setMenu = (open) => {
    drawer.classList.toggle('is-open', open);
    document.body.classList.toggle('menu-open', open);
    burger.setAttribute('aria-expanded', String(open));
    drawer.setAttribute('aria-hidden', String(!open));
    document.body.style.overflow = open ? 'hidden' : '';
    if (open) $('.drawer__close').focus();
  };
  burger.addEventListener('click', () => setMenu(true));
  $('.drawer__close').addEventListener('click', () => { setMenu(false); burger.focus(); });
  $$('.drawer a').forEach((a) => a.addEventListener('click', () => setMenu(false)));
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape' && drawer.classList.contains('is-open')) setMenu(false); });

  /* Aparición al hacer scroll */
  const io = new IntersectionObserver((entries) => {
    entries.forEach((en) => {
      if (en.isIntersecting) { en.target.classList.add('is-in'); io.unobserve(en.target); }
    });
  }, { threshold: 0.15, rootMargin: '0px 0px -40px 0px' });
  $$('.rv, .scribble, .hero, .hero-full, [data-count]').forEach((el) => io.observe(el));

  /* Contadores */
  const counter = new IntersectionObserver((entries) => {
    entries.forEach((en) => {
      if (!en.isIntersecting) return;
      const el = en.target; counter.unobserve(el);
      const end = parseInt(el.dataset.count, 10);
      if (reduce) { el.textContent = end.toLocaleString('es-CO'); return; }
      const t0 = performance.now(), dur = 1800;
      const tick = (t) => {
        const p = Math.min((t - t0) / dur, 1);
        const v = Math.round(end * (1 - Math.pow(1 - p, 4)));
        el.textContent = v.toLocaleString('es-CO');
        if (p < 1) requestAnimationFrame(tick);
      };
      requestAnimationFrame(tick);
    });
  }, { threshold: 0.6 });
  $$('[data-count]').forEach((el) => counter.observe(el));

  /* Pestañas (índice de procedimientos) */
  $$('[role="tablist"]').forEach((list) => {
    const tabs = $$('[role="tab"]', list);
    const select = (tab) => {
      tabs.forEach((t) => {
        const on = t === tab;
        t.setAttribute('aria-selected', String(on));
        t.tabIndex = on ? 0 : -1;
        const panel = document.getElementById(t.getAttribute('aria-controls'));
        if (panel) panel.hidden = !on;
      });
    };
    tabs.forEach((t, i) => {
      t.addEventListener('click', () => select(t));
      t.addEventListener('keydown', (e) => {
        if (e.key !== 'ArrowRight' && e.key !== 'ArrowLeft') return;
        const next = tabs[(i + (e.key === 'ArrowRight' ? 1 : -1) + tabs.length) % tabs.length];
        select(next); next.focus();
      });
    });
  });

  /* Vista previa que sigue al cursor (solo con mouse) */
  const preview = $('.cursor-preview');
  if (preview && window.matchMedia('(hover: hover) and (pointer: fine)').matches) {
    const box = $('div', preview);
    let x = 0, y = 0, cx = 0, cy = 0, raf;
    const loop = () => {
      cx += (x - cx) * 0.16; cy += (y - cy) * 0.16;
      preview.style.left = cx + 'px'; preview.style.top = cy + 'px';
      raf = requestAnimationFrame(loop);
    };
    $$('[data-preview]').forEach((a) => {
      a.addEventListener('mouseenter', (e) => {
        x = cx = e.clientX; y = cy = e.clientY;
        const src = a.dataset.preview;
        box.innerHTML = src
          ? `<img src="${src}" alt="">`
          : `<div class="ph"><span>${PH_ICON}Foto: ${a.dataset.label}</span></div>`;
        preview.classList.add('is-on');
        cancelAnimationFrame(raf); loop();
      });
      a.addEventListener('mousemove', (e) => { x = e.clientX; y = e.clientY; });
      a.addEventListener('mouseleave', () => { preview.classList.remove('is-on'); cancelAnimationFrame(raf); });
    });
  }

  /* Carrusel de polaroids */
  $$('.team').forEach((team) => {
    const track = $('.team__track', team);
    const prev = $('[data-prev]', team), next = $('[data-next]', team);
    const step = () => ($('.pola', track)?.offsetWidth || 260) + 40;
    const update = () => {
      prev.disabled = track.scrollLeft < 8;
      next.disabled = track.scrollLeft + track.clientWidth > track.scrollWidth - 8;
    };
    prev.addEventListener('click', () => track.scrollBy({ left: -step(), behavior: 'smooth' }));
    next.addEventListener('click', () => track.scrollBy({ left: step(), behavior: 'smooth' }));
    track.addEventListener('scroll', update, { passive: true });
    window.addEventListener('resize', update);
    update();

    // Arrastrar con el mouse
    let down = false, sx = 0, sl = 0, moved = false;
    track.addEventListener('pointerdown', (e) => {
      if (e.pointerType !== 'mouse') return;
      down = true; moved = false; sx = e.clientX; sl = track.scrollLeft;
      track.style.scrollSnapType = 'none'; track.style.scrollBehavior = 'auto';
    });
    window.addEventListener('pointermove', (e) => {
      if (!down) return;
      const dx = e.clientX - sx;
      if (Math.abs(dx) > 4) moved = true;
      track.scrollLeft = sl - dx;
    });
    window.addEventListener('pointerup', () => {
      if (!down) return;
      down = false; track.style.scrollSnapType = ''; track.style.scrollBehavior = '';
    });

    // Tocar / Enter abre la biografía (en pantallas táctiles no hay hover)
    $$('.pola', track).forEach((p) => {
      const toggle = () => {
        const open = !p.classList.contains('is-open');
        $$('.pola.is-open', track).forEach((o) => { o.classList.remove('is-open'); o.setAttribute('aria-expanded', 'false'); });
        p.classList.toggle('is-open', open);
        p.setAttribute('aria-expanded', String(open));
      };
      p.addEventListener('click', () => { if (!moved) toggle(); });
      p.addEventListener('keydown', (e) => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); toggle(); } });
    });
  });

  /* Franjas automáticas (derecha → izquierda, en bucle). Se detienen al interactuar. */
  $$('[data-auto] .hs-track').forEach((track) => {
    const items = [...track.children];
    if (items.length < 2) return;
    items.forEach((el) => {
      const c = el.cloneNode(true);
      c.setAttribute('aria-hidden', 'true');
      $$('input, button, a', c).forEach((x) => x.setAttribute('tabindex', '-1'));
      track.appendChild(c);
    });
    if (reduce) return;
    let paused = false, visible = false, last = 0, acc = 0;
    const speed = 0.04; // px por milisegundo
    const pause = () => { paused = true; };
    const resume = () => { paused = false; last = 0; };
    track.addEventListener('pointerenter', pause);
    track.addEventListener('pointerleave', resume);
    track.addEventListener('focusin', pause);
    track.addEventListener('focusout', resume);
    track.addEventListener('touchstart', () => { pause(); clearTimeout(track._t); }, { passive: true });
    track.addEventListener('touchend', () => { track._t = setTimeout(resume, 2500); }, { passive: true });
    new IntersectionObserver(([en]) => { visible = en.isIntersecting; last = 0; }).observe(track);
    const tick = (t) => {
      if (visible && !paused && !document.hidden) {
        if (last) {
          acc += (t - last) * speed;
          const step = Math.floor(acc);
          if (step >= 1) { track.scrollLeft += step; acc -= step; }
          const half = track.scrollWidth / 2;
          if (track.scrollLeft >= half) track.scrollLeft -= half;
        }
        last = t;
      }
      requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
  });

  /* Antes / después */
  $$('.ba input[type="range"]').forEach((r) => {
    const set = () => r.closest('.ba').style.setProperty('--pos', r.value + '%');
    r.addEventListener('input', set); set();
  });

  /* Filtros (procedimientos y resultados) */
  const chips = $$('.chip[data-filter]');
  chips.forEach((c) => c.addEventListener('click', () => {
    chips.forEach((o) => o.setAttribute('aria-pressed', String(o === c)));
    const f = c.dataset.filter;
    $$('.pcard[data-cat], .ba-item[data-cat]').forEach((card) => {
      card.hidden = f !== 'todos' && card.dataset.cat !== f;
      if (!card.hidden) card.classList.add('is-in');
    });
  }));

  /* Velo de contenido médico sensible */
  $$('.veil').forEach((v) => v.addEventListener('click', () => {
    v.closest('.ba').classList.remove('ba--sens');
  }));

  /* Carruseles horizontales genéricos */
  $$('[data-scroller]').forEach((sc) => {
    const track = $('.hs-track', sc);
    const prev = $('[data-prev]', sc), next = $('[data-next]', sc);
    if (!track || !prev || !next) return;
    const step = () => (track.firstElementChild?.offsetWidth || 280) + 20;
    const update = () => {
      prev.disabled = track.scrollLeft < 8;
      next.disabled = track.scrollLeft + track.clientWidth > track.scrollWidth - 8;
    };
    prev.addEventListener('click', () => track.scrollBy({ left: -step(), behavior: 'smooth' }));
    next.addEventListener('click', () => track.scrollBy({ left: step(), behavior: 'smooth' }));
    track.addEventListener('scroll', update, { passive: true });
    window.addEventListener('resize', update);
    update();
  });

  /* Reels: cargan el video solo si existe y se reproducen al verse */
  const reelIO = new IntersectionObserver((entries) => {
    entries.forEach((en) => {
      const v = $('video', en.target);
      if (!v) return;
      if (en.isIntersecting) {
        if (!v.dataset.tried && v.dataset.src) {
          v.dataset.tried = '1';
          v.addEventListener('loadeddata', () => {
            en.target.classList.add('has-video');
            if (!reduce) v.play().catch(() => {});
          }, { once: true });
          v.src = v.dataset.src;
        }
        if (!reduce && en.target.classList.contains('has-video')) v.play().catch(() => {});
      } else if (!v.paused) {
        v.pause();
      }
    });
  }, { threshold: 0.4 });
  $$('.reel').forEach((r) => {
    reelIO.observe(r);
    // Con video cargado, tocar activa/desactiva el sonido en vez de ir a Instagram
    r.addEventListener('click', (e) => {
      const v = $('video', r);
      if (!r.classList.contains('has-video') || !v) return;
      e.preventDefault();
      const on = v.muted;
      $$('.reel video').forEach((o) => { o.muted = true; o.closest('.reel').classList.remove('is-sound'); });
      v.muted = !on;
      r.classList.toggle('is-sound', on);
      v.play().catch(() => {});
    });
  });

  /* Video emergente (solo se descarga cuando la persona lo pide) */
  const modal = $('.vmodal');
  if (modal) {
    const mv = $('video', modal);
    const close = () => { mv.pause(); modal.close(); };
    $$('[data-video]').forEach((b) => b.addEventListener('click', () => {
      if (mv.getAttribute('src') !== b.dataset.video) mv.src = b.dataset.video;
      modal.showModal();
      mv.play().catch(() => {});
    }));
    $('.vmodal__close', modal).addEventListener('click', close);
    modal.addEventListener('click', (e) => { if (e.target === modal) close(); });
    modal.addEventListener('close', () => mv.pause());
  }

  /* Línea de tiempo que se "llena" con el scroll */
  const tl = $('.timeline');
  if (tl) {
    const fill = $('.timeline__fill', tl);
    const upd = () => {
      const r = tl.getBoundingClientRect();
      const p = Math.min(Math.max((window.innerHeight * 0.6 - r.top) / r.height, 0), 1);
      fill.style.setProperty('--fill', (p * 100).toFixed(1) + '%');
    };
    window.addEventListener('scroll', upd, { passive: true }); upd();
  }

  /* Formularios → WhatsApp (sin servidor) */
  $$('form[data-wa]').forEach((form) => {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      let ok = true;
      $$('[required]', form).forEach((inp) => {
        const bad = !inp.value.trim();
        inp.closest('.field').classList.toggle('is-bad', bad);
        inp.setAttribute('aria-invalid', String(bad));
        if (bad && ok) { inp.focus(); ok = false; }
      });
      if (!ok) return;
      const lines = [form.dataset.wa];
      $$('input, select, textarea', form).forEach((inp) => {
        if (!inp.value.trim()) return;
        const label = $(`label[for="${inp.id}"]`, form)?.textContent.replace('*', '').trim() || inp.name;
        lines.push(`• ${label}: ${inp.value.trim()}`);
      });
      window.open(`https://wa.me/${WA_NUMBER}?text=${encodeURIComponent(lines.join('\n'))}`, '_blank', 'noopener');
    });
    $$('[required]', form).forEach((inp) => inp.addEventListener('input', () => inp.closest('.field').classList.remove('is-bad')));
  });

  /* Año del footer */
  $$('[data-year]').forEach((el) => { el.textContent = new Date().getFullYear(); });

  const PH_ICON = '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="6" width="18" height="14" rx="2"/><circle cx="12" cy="13" r="3.5"/><path d="M8 6l1.5-2h5L16 6"/></svg>';
})();
