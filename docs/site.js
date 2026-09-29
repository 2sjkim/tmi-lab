const toggle = document.querySelector('.menu-toggle');
const nav = document.querySelector('.nav');

if (document.querySelector('.publication-tabs') || /(?:^|\/)patents\.html$/.test(location.pathname)) {
  const topButton = document.createElement('button');
  topButton.type = 'button';
  topButton.className = 'back-to-top';
  topButton.setAttribute('aria-label', 'Back to top');
  topButton.title = 'Back to top';
  topButton.innerHTML = '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m6 10 6-6 6 6M12 4v16"/></svg><span>TOP</span>';
  topButton.addEventListener('click', () => {
    document.querySelector('.brand')?.focus({preventScroll: true});
    window.scrollTo({top: 0, behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'instant' : 'smooth'});
  });
  document.body.append(topButton);
}
toggle?.addEventListener('click', () => {
  const open = toggle.getAttribute('aria-expanded') !== 'true';
  toggle.setAttribute('aria-expanded', String(open));
  toggle.setAttribute('aria-label', open ? 'Close navigation' : 'Open navigation');
  nav.classList.toggle('open', open);
});

// Progressive enhancement: file:// and failed requests retain the static content.
const recentNews = document.querySelector('[data-recent-news]');
const journalPublications = document.querySelector('[data-journal-publications]');
if ((recentNews || journalPublications) && location.protocol !== 'file:') {
  fetch('content.json', {cache: 'no-store'})
    .then(response => {
      if (!response.ok) throw new Error('Journal data unavailable');
      return response.json();
    })
    .then(data => {
      if (!Array.isArray(data.journal) || !data.journal.every(paper =>
        paper && ['title', 'authors', 'venue', 'year'].every(key => typeof paper[key] === 'string'))) {
        throw new Error('Invalid journal data');
      }
      if (recentNews) recentNews.innerHTML = TMIPublications.recent(data.journal);
      if (journalPublications) journalPublications.innerHTML = TMIPublications.journal(data.journal);
      if (location.hash.startsWith('#year-')) {
        document.getElementById(location.hash.slice(1))?.scrollIntoView();
      }
    })
    .catch(() => { /* Keep the complete pre-rendered publication list. */ });
}
document.addEventListener('keydown', event => {
  if (event.key === 'Escape' && nav?.classList.contains('open')) {
    nav.classList.remove('open');
    toggle.setAttribute('aria-expanded', 'false');
    toggle.setAttribute('aria-label', 'Open navigation');
    toggle.focus();
  }
});
