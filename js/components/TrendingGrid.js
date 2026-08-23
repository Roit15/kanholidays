import { PACKAGES } from '../data.js';

function escapeHTML(str) {
  if (typeof str !== 'string') return str;
  return str.replace(/[&<>'"]/g, 
    tag => ({
      '&': '&amp;',
      '<': '&lt;',
      '>': '&gt;',
      "'": '&#39;',
      '"': '&quot;'
    }[tag] || tag)
  );
}

export function initTrendingPackages() {
  const grid = document.getElementById('trendingGrid');
  const tabs = document.querySelectorAll('.trending-tab');
  if (!grid) return;

  function renderPackages(filter = 'all') {
    let filtered = PACKAGES;
    if (filter === 'international') filtered = PACKAGES.filter(p => p.category === 'international');
    else if (filter === 'india') filtered = PACKAGES.filter(p => p.category === 'india');
    else if (filter === 'honeymoon') filtered = PACKAGES.filter(p => p.tags.includes('honeymoon'));
    else if (filter === 'adventure') filtered = PACKAGES.filter(p => p.tags.includes('adventure'));

    // Show max 9
    filtered = filtered.slice(0, 9);

    grid.innerHTML = filtered.map(pkg => {
      const escapedDest = escapeHTML(pkg.dest);
      const escapedName = escapeHTML(pkg.name);
      const escapedHighlights = escapeHTML(pkg.highlights.join(' · '));
      const slug = pkg.dest.toLowerCase().replace(/[^a-z0-9]+/g,'-');
      const escapedImage = encodeURI(pkg.image);

      return `
      <a href="/destinations/${slug}.html" class="card">
        <div class="card__image">
          <img src="${escapedImage}" alt="${escapedName}" loading="lazy">
          <span class="card__badge">${escapedDest}</span>
          <button class="card__wishlist" onclick="event.preventDefault();event.stopPropagation();this.classList.toggle('active')" aria-label="Add to wishlist">
            <i class="fas fa-heart" aria-hidden="true"></i>
          </button>
        </div>
        <div class="card__body">
          <div class="card__rating">
            <span class="stars">${'★'.repeat(Math.floor(pkg.rating))}${pkg.rating % 1 ? '½' : ''}</span>
            <span>${pkg.rating} (${pkg.reviews} reviews)</span>
          </div>
          <h3 class="card__title">${escapedName}</h3>
          <p class="card__subtitle">${escapedHighlights}</p>
          <div class="card__chips">
            <span class="chip"><i class="fas fa-clock" aria-hidden="true"></i> ${escapeHTML(pkg.duration)}</span>
            ${pkg.flights ? '<span class="chip"><i class="fas fa-plane" aria-hidden="true"></i> Flights Inc.</span>' : ''}
            <span class="chip"><i class="fas fa-hotel" aria-hidden="true"></i> Hotel</span>
          </div>
          <div class="card__footer">
            <div class="card__price">
              <span class="card__price-original">₹${pkg.originalPrice.toLocaleString('en-IN')}</span>
              <span class="card__price-current">₹${pkg.price.toLocaleString('en-IN')}</span>
              <span class="card__price-label">per person</span>
            </div>
            <span class="btn btn--sm btn--primary">View Details</span>
          </div>
        </div>
      </a>
      `;
    }).join('');
  }

  renderPackages('all');

  tabs.forEach(tab => {
    tab.addEventListener('click', () => {
      tabs.forEach(t => t.classList.remove('active'));
      tab.classList.add('active');
      renderPackages(tab.dataset.filter);
    });
  });
}
