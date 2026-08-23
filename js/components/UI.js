export function initHeader() {
  const header = document.getElementById('siteHeader');
  if (!header) return;

  window.addEventListener('scroll', () => {
    const scroll = window.scrollY;
    header.classList.toggle('scrolled', scroll > 50);
  }, { passive: true });
}

export function initMobileMenu() {
  const toggle = document.getElementById('mobileToggle');
  const overlay = document.getElementById('mobileOverlay');
  const menu = document.getElementById('mobileMenu');
  if (!toggle || !menu) return;

  function openMenu() {
    toggle.classList.add('active');
    menu.classList.add('active');
    if (overlay) overlay.classList.add('active');
    document.body.classList.add('no-scroll');
  }

  function closeMenu() {
    toggle.classList.remove('active');
    menu.classList.remove('active');
    if (overlay) overlay.classList.remove('active');
    document.body.classList.remove('no-scroll');
  }

  toggle.addEventListener('click', () => {
    toggle.classList.contains('active') ? closeMenu() : openMenu();
  });

  if (overlay) overlay.addEventListener('click', closeMenu);
}

export function initScrollReveal() {
  const reveals = document.querySelectorAll('.reveal, .reveal-left, .reveal-right, .reveal-scale, .reveal-clip');
  if (!reveals.length) return;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        entry.target.classList.add('active');
        observer.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.08,
    rootMargin: '0px 0px -100px 0px'
  });

  reveals.forEach(el => observer.observe(el));
}

export function initCounterAnimation() {
  const counters = document.querySelectorAll('.trust-item__number');
  if (!counters.length) return;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        animateCounter(entry.target);
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.5 });

  counters.forEach(el => observer.observe(el));
}

function animateCounter(el) {
  const text = el.textContent;
  const match = text.match(/(\d[\d,]*)(\+?)/);
  if (!match) return;

  const target = parseInt(match[1].replace(/,/g, ''));
  const suffix = match[2] || '';
  const rest = text.replace(match[0], '{{NUM}}');
  const duration = 1800;
  const start = performance.now();

  function update(now) {
    const elapsed = now - start;
    const progress = Math.min(elapsed / duration, 1);
    const eased = 1 - Math.pow(1 - progress, 3); // ease-out cubic
    const current = Math.round(target * eased);
    el.textContent = rest.replace('{{NUM}}', current.toLocaleString('en-IN') + suffix);
    if (progress < 1) requestAnimationFrame(update);
  }

  requestAnimationFrame(update);
}

export function initCallbackModal() {
  const modal = document.getElementById('callbackModal');
  if (!modal) return;

  modal.addEventListener('click', (e) => {
    if (e.target === modal) closeCallbackModal();
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && modal.classList.contains('active')) {
      closeCallbackModal();
    }
  });
}

export function openCallbackModal(pkgId, pkgName) {
  const modal = document.getElementById('callbackModal');
  const destSelect = document.getElementById('callbackDest');
  if (modal) {
    modal.classList.add('active');
    document.body.classList.add('no-scroll');
    if (destSelect && pkgName) {
      for (let opt of destSelect.options) {
        if (pkgName.toLowerCase().includes(opt.value.toLowerCase())) {
          opt.selected = true;
          break;
        }
      }
    }
  }
}

export function closeCallbackModal() {
  const modal = document.getElementById('callbackModal');
  if (modal) {
    modal.classList.remove('active');
    document.body.classList.remove('no-scroll');
  }
}

// Attach to window since it's used in inline onclick in HTML
window.openCallbackModal = openCallbackModal;
window.closeCallbackModal = closeCallbackModal;
