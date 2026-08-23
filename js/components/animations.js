/**
 * animations.js — Emil Kowalski-inspired animation system
 * Handles: page-load entrance, parallax, magnetic hover, clip-path reveals
 */

const EASE_OUT = 'cubic-bezier(0.23, 1, 0.32, 1)';
const PREFERS_REDUCED = window.matchMedia('(prefers-reduced-motion: reduce)');
const HAS_FINE_POINTER = window.matchMedia('(hover: hover) and (pointer: fine)');

/**
 * Page-load stagger animation for hero elements
 * Uses Web Animations API for interruptibility
 */
export function initPageLoadEntrance() {
  if (PREFERS_REDUCED.matches) return;

  const heroContent = document.querySelector('.hero-content');
  if (!heroContent) return;

  // The hero elements already have CSS animation (hero-entrance keyframes).
  // Enhance with a subtle backdrop parallax on load.
  const heroSlide = document.querySelector('.hero-slide.active .hero-slide__image');
  if (heroSlide) {
    heroSlide.animate([
      { transform: 'scale(1.12)', opacity: 0.8 },
      { transform: 'scale(1.08)', opacity: 1 }
    ], {
      duration: 1200,
      easing: EASE_OUT,
      fill: 'forwards'
    });
  }
}

/**
 * Lightweight scroll-driven parallax
 * Only uses transform: translateY (GPU compositing)
 */
export function initParallax() {
  if (PREFERS_REDUCED.matches) return;

  const heroImage = document.querySelector('.hero-slide__image');
  if (!heroImage) return;

  let ticking = false;

  function onScroll() {
    if (ticking) return;
    ticking = true;

    requestAnimationFrame(() => {
      const scrollY = window.scrollY;
      const heroHeight = window.innerHeight;

      // Only parallax while hero is visible
      if (scrollY < heroHeight) {
        const offset = scrollY * 0.15;
        heroImage.style.transform = `scale(1.08) translateY(${offset}px)`;
      }

      ticking = false;
    });
  }

  window.addEventListener('scroll', onScroll, { passive: true });
}

/**
 * Magnetic hover effect for CTA buttons
 * Follows cursor within button bounds for a playful feel
 * Marketing site = decorative is OK per the skills
 */
export function initMagneticHover() {
  if (PREFERS_REDUCED.matches || !HAS_FINE_POINTER.matches) return;

  const magnets = document.querySelectorAll('.btn--primary, .hero-search__btn');
  if (!magnets.length) return;

  magnets.forEach(el => {
    const strength = 0.2; // How much the button moves (0 = none, 1 = full cursor tracking)

    el.addEventListener('mousemove', (e) => {
      const rect = el.getBoundingClientRect();
      const x = e.clientX - rect.left - rect.width / 2;
      const y = e.clientY - rect.top - rect.height / 2;
      el.style.transform = `translate(${x * strength}px, ${y * strength}px)`;
    });

    el.addEventListener('mouseleave', () => {
      el.style.transition = 'transform 0.4s cubic-bezier(0.23, 1, 0.32, 1)';
      el.style.transform = 'translate(0, 0)';
      // Clean up inline transition after it completes
      setTimeout(() => {
        el.style.transition = '';
      }, 400);
    });
  });
}

/**
 * Active-state press feedback
 * Scale down on press, spring back on release
 */
export function initPressFeedback() {
  if (PREFERS_REDUCED.matches) return;

  const pressables = document.querySelectorAll('.btn, .hero-pill, .trending-tab');
  pressables.forEach(el => {
    el.addEventListener('pointerdown', () => {
      el.style.transform = 'scale(0.97)';
    });

    el.addEventListener('pointerup', () => {
      el.style.transform = '';
    });

    el.addEventListener('pointerleave', () => {
      el.style.transform = '';
    });
  });
}

/**
 * Smooth image reveal with clip-path
 * Wipes images into view from bottom on scroll
 */
export function initImageReveals() {
  if (PREFERS_REDUCED.matches) return;

  const images = document.querySelectorAll('.bento-item__image, .honeymoon-card__image');
  if (!images.length) return;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.clipPath = 'inset(0 0 0 0)';
        observer.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.15,
    rootMargin: '0px 0px -80px 0px'
  });

  images.forEach(el => {
    el.style.clipPath = 'inset(0 0 100% 0)';
    el.style.transition = 'clip-path 0.6s cubic-bezier(0.23, 1, 0.32, 1)';
    observer.observe(el);
  });
}

/**
 * Smooth number counter with spring easing
 * Uses requestAnimationFrame for smooth 60fps
 */
export function initSmoothCounters() {
  const counters = document.querySelectorAll('.trust-item__number');
  if (!counters.length) return;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        animateNumber(entry.target);
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.5 });

  counters.forEach(el => observer.observe(el));
}

function animateNumber(el) {
  const text = el.textContent;
  const match = text.match(/(\d[\d,]*)(\+?)/);
  if (!match) return;

  const target = parseInt(match[1].replace(/,/g, ''));
  const suffix = match[2] || '';
  const rest = text.replace(match[0], '{{NUM}}');
  const duration = 1400;
  const start = performance.now();

  function update(now) {
    const elapsed = now - start;
    const progress = Math.min(elapsed / duration, 1);

    // Ease-out quartic for a snappy feel that decelerates smoothly
    const eased = 1 - Math.pow(1 - progress, 4);
    const current = Math.round(target * eased);

    el.textContent = rest.replace('{{NUM}}', current.toLocaleString('en-IN') + suffix);

    if (progress < 1) {
      requestAnimationFrame(update);
    }
  }

  requestAnimationFrame(update);
}

/**
 * Section heading entrance animation
 * Subtle scale + fade for section titles
 */
export function initSectionHeadingEntrance() {
  if (PREFERS_REDUCED.matches) return;

  const headings = document.querySelectorAll('.section-label, .section-title, .section-subtitle');
  if (!headings.length) return;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.opacity = '1';
        entry.target.style.transform = 'translateY(0)';
        observer.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.2,
    rootMargin: '0px 0px -60px 0px'
  });

  headings.forEach((el, i) => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(12px)';
    el.style.transition = `opacity 0.4s ${EASE_OUT} ${i * 0.08}s, transform 0.4s ${EASE_OUT} ${i * 0.08}s`;
    observer.observe(el);
  });
}

/**
 * Initialize all animation modules
 */
export function initAnimations() {
  initPageLoadEntrance();
  initParallax();
  initMagneticHover();
  initPressFeedback();
  initImageReveals();
  initSectionHeadingEntrance();
}
