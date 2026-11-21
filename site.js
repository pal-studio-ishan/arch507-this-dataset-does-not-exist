// Lightbox for image grids (scoped to the grid you clicked in), comparison tabs, and copy buttons for prompts.
(function () {
  var all = Array.prototype.slice.call(document.querySelectorAll('.g-item'));
  var items = all;
  if (all.length) {
    var box = document.createElement('div');
    box.className = 'lightbox';
    box.innerHTML = '<img alt=""><button class="lb-btn lb-prev" aria-label="Previous">←</button><button class="lb-btn lb-next" aria-label="Next">→</button><div class="lb-count"></div>';
    document.body.appendChild(box);
    var img = box.querySelector('img'), count = box.querySelector('.lb-count'), i = 0;
    function show(n) {
      i = (n + items.length) % items.length;
      img.src = items[i].getAttribute('href');
      count.textContent = (i + 1) + ' / ' + items.length;
      box.classList.add('open');
    }
    all.forEach(function (a) {
      a.addEventListener('click', function (e) {
        e.preventDefault();
        var group = a.closest('.lb-group');
        items = group ? Array.prototype.slice.call(group.querySelectorAll('.g-item')) : all;
        show(items.indexOf(a));
      });
    });
    box.querySelector('.lb-prev').addEventListener('click', function (e) { e.stopPropagation(); show(i - 1); });
    box.querySelector('.lb-next').addEventListener('click', function (e) { e.stopPropagation(); show(i + 1); });
    box.addEventListener('click', function () { box.classList.remove('open'); });
    document.addEventListener('keydown', function (e) {
      if (!box.classList.contains('open')) return;
      if (e.key === 'Escape') box.classList.remove('open');
      if (e.key === 'ArrowLeft') show(i - 1);
      if (e.key === 'ArrowRight') show(i + 1);
    });
  }
  document.querySelectorAll('.cmp-tab').forEach(function (t) {
    t.addEventListener('click', function () {
      document.querySelectorAll('.cmp-tab').forEach(function (o) { o.setAttribute('aria-selected', o === t ? 'true' : 'false'); });
      document.querySelectorAll('.cmp-set').forEach(function (s) { s.hidden = s.getAttribute('data-set') !== t.getAttribute('data-set'); });
    });
  });
  document.querySelectorAll('.copy').forEach(function (b) {
    b.addEventListener('click', function () {
      var t = b.parentNode.querySelector('p').textContent;
      try {
        navigator.clipboard.writeText(t).then(function () { b.textContent = 'Copied'; setTimeout(function () { b.textContent = 'Copy'; }, 1500); });
      } catch (e) { /* clipboard not available */ }
    });
  });
})();
