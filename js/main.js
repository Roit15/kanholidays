import { initHeroSlider, initTypingEffect } from './components/HeroSlider.js';
import { initSearch } from './components/Search.js';
import { initTrendingPackages } from './components/TrendingGrid.js';
import { 
  initHeader, 
  initMobileMenu, 
  initScrollReveal, 
  initCounterAnimation, 
  initCallbackModal 
} from './components/UI.js';
import { initAnimations } from './components/animations.js';

document.addEventListener('DOMContentLoaded', () => {
  initHeroSlider();
  initHeader();
  initMobileMenu();
  initSearch();
  initTrendingPackages();
  initScrollReveal();
  initCallbackModal();
  initCounterAnimation();
  initTypingEffect();
  initAnimations();
});
