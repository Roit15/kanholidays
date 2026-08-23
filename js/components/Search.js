import { PACKAGES } from '../data.js';

export function initSearch() {
  const searchToggle = document.getElementById('searchToggle');
  const searchOverlay = document.getElementById('searchOverlay');
  const searchClose = document.getElementById('searchClose');
  const searchInput = document.getElementById('searchInput');
  const heroSearchInput = document.getElementById('heroSearchInput');

  if (searchToggle && searchOverlay) {
    searchToggle.addEventListener('click', () => {
      searchOverlay.classList.add('active');
      setTimeout(() => searchInput?.focus(), 300);
    });
  }

  if (searchClose && searchOverlay) {
    searchClose.addEventListener('click', () => {
      searchOverlay.classList.remove('active');
    });
  }

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && searchOverlay?.classList.contains('active')) {
      searchOverlay.classList.remove('active');
    }
  });

  if (heroSearchInput) {
    heroSearchInput.addEventListener('focus', () => {
      if (searchOverlay) {
        searchOverlay.classList.add('active');
        setTimeout(() => searchInput?.focus(), 300);
      }
    });
  }

  function executeSearch(query) {
    if (!query) return;
    const q = query.toLowerCase().trim();
    const match = PACKAGES.find(p => p.dest.toLowerCase().includes(q) || p.name.toLowerCase().includes(q));
    
    if (match) {
      const slug = match.dest.toLowerCase().replace(/[^a-z0-9]+/g, '-');
      window.location.href = `/destinations/${slug}`;
    } else {
      window.location.href = `/destinations`;
    }
  }

  if (searchInput) {
    searchInput.addEventListener('keypress', (e) => {
      if (e.key === 'Enter') {
        executeSearch(searchInput.value);
      }
    });
  }
}
