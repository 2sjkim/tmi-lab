/* Shared journal renderer: Home and Journal read the same ordered data. */
(function (root) {
  'use strict';
  const escape = value => String(value ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const clip = '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="m21.4 11.6-9.2 9.2a6 6 0 0 1-8.5-8.5l10-10a4 4 0 0 1 5.7 5.7l-10 10a2 2 0 0 1-2.8-2.8l9.2-9.2"/></svg>';
  function safeUrl(url) {
    try { const parsed = new URL(url); return ['https:', 'http:'].includes(parsed.protocol) ? parsed.href : ''; }
    catch { return ''; }
  }
  function ordered(records) {
    // Within the same year, preserve the journal's editorial order (newest first).
    return records.map((paper, index) => ({paper, index})).sort((a, b) => {
      const year = value => /^\d{4}$/.test(String(value)) ? Number(value) : 0;
      return year(b.paper.year) - year(a.paper.year) || a.index - b.index;
    }).map(({paper}) => paper);
  }
  function publication(paper) {
    let venue = escape(paper.venue);
    for (const label of ["Editor's Choice", 'Oral Presentation']) {
      venue = venue.replaceAll(escape(label), '<span class="publication-distinction">' + escape(label) + '</span>');
    }
    const url = safeUrl(paper.url);
    const link = url ? ' <a class="publication-link" href="' + escape(url) + '" target="_blank" rel="noopener noreferrer" aria-label="Open paper: ' + escape(paper.title) + '">' + clip + '<span>Link</span></a>' : '';
    const otherLinks = (paper.links || []).map(link => {
      const url = safeUrl(link.url);
      return url ? '<a href="' + escape(url) + '">' + escape(link.text) + '</a>' : '';
    }).filter(Boolean).join(' ');
    return '<article class="publication"><h3>' + escape(paper.title) + link + '</h3><p>' + escape(paper.authors) + '</p><p class="venue">' + venue + '</p>' + (otherLinks ? '<p class="paper-links">' + otherLinks + '</p>' : '') + '</article>';
  }
  function recent(records) { return ordered(records).slice(0, 3).map(publication).join(''); }
  function journal(records) {
    const papers = ordered(records);
    const years = [...new Set(papers.map(p => p.year))];
    const id = year => 'year-' + String(year).replace(/[^a-zA-Z0-9_-]/g, '-');
    return '<nav class="year-nav" aria-label="Publication years">' + years.map(year => '<a href="#' + id(year) + '">' + escape(year) + '</a>').join('') + '</nav><div>' + years.map(year => '<section class="year-group" id="' + id(year) + '"><h2>' + escape(year) + '</h2>' + papers.filter(p => p.year === year).map(publication).join('') + '</section>').join('') + '</div>';
  }
  const api = {ordered, publication, recent, journal};
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  else root.TMIPublications = api;
})(typeof window !== 'undefined' ? window : globalThis);
