import { HERO_SLIDES } from '../data.js';

const EASE_OUT = 'cubic-bezier(0.23, 1, 0.32, 1)';

export function initHeroSlider() {
  const slides = document.querySelectorAll('.hero-slide');
  const titleEl = document.getElementById('heroTitle');
  const subtitleEl = document.getElementById('heroSubtitle');
  const progressBar = document.getElementById('heroProgressBar');
  if (!slides.length) return;

  let current = 0;
  const duration = 4000; // 4s per slide — slightly longer for breathing room

  function animateProgress() {
    if (!progressBar) return;
    progressBar.style.transition = 'none';
    progressBar.style.width = '0%';
    requestAnimationFrame(() => {
      requestAnimationFrame(() => {
        progressBar.style.transition = `width ${duration}ms linear`;
        progressBar.style.width = '100%';
      });
    });
  }

  function goToSlide(index) {
    slides[current].classList.remove('active');
    current = index % slides.length;
    slides[current].classList.add('active');

    if (titleEl && HERO_SLIDES[current]) {
      // Exit: fade out + subtle upward drift
      titleEl.style.transition = `opacity 0.25s ${EASE_OUT}, transform 0.25s ${EASE_OUT}`;
      subtitleEl.style.transition = `opacity 0.25s ${EASE_OUT}, transform 0.25s ${EASE_OUT}`;
      titleEl.style.opacity = '0';
      titleEl.style.transform = 'translateY(-8px)';
      subtitleEl.style.opacity = '0';
      subtitleEl.style.transform = 'translateY(-8px)';

      setTimeout(() => {
        // Set new text while invisible
        titleEl.textContent = HERO_SLIDES[current].title;
        subtitleEl.textContent = HERO_SLIDES[current].subtitle;

        // Reset position for entrance
        titleEl.style.transition = 'none';
        subtitleEl.style.transition = 'none';
        titleEl.style.transform = 'translateY(12px)';
        subtitleEl.style.transform = 'translateY(12px)';

        // Enter: fade in + upward drift with stagger
        requestAnimationFrame(() => {
          requestAnimationFrame(() => {
            titleEl.style.transition = `opacity 0.5s ${EASE_OUT}, transform 0.5s ${EASE_OUT}`;
            subtitleEl.style.transition = `opacity 0.5s ${EASE_OUT} 0.1s, transform 0.5s ${EASE_OUT} 0.1s`;
            titleEl.style.opacity = '1';
            titleEl.style.transform = 'translateY(0)';
            subtitleEl.style.opacity = '1';
            subtitleEl.style.transform = 'translateY(0)';
          });
        });
      }, 280);
    }
    animateProgress();
  }

  animateProgress();
  setInterval(() => goToSlide(current + 1), duration);
}

export function initTypingEffect() {
  const subtitleEl = document.getElementById('heroSubtitle');
  if (!subtitleEl) return;
  const cursor = document.createElement('span');
  cursor.className = 'typing-cursor';
  subtitleEl.appendChild(cursor);
}
