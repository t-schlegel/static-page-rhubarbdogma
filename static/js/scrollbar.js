// Initially hide the scrollbar
hideScrollbar();

let scrollbarTimeout;
const body = document.body;

function showScrollbar() {
  body.classList.remove('hide-scrollbar');
  clearTimeout(scrollbarTimeout);
}

function hideScrollbar() {
  scrollbarTimeout = setTimeout(() => {
    body.classList.add('hide-scrollbar');
  }, 1500); // Hide after 1.5 seconds of inactivity
}

window.addEventListener('scroll', () => {
  showScrollbar();
  hideScrollbar();
});

// Initially hide the scrollbar
hideScrollbar();
