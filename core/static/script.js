document.addEventListener('DOMContentLoaded', function () {
    const carousel = document.querySelector('#heroCarousel');
    if (carousel) {
      new bootstrap.Carousel(carousel, {
        interval: 5000,
        ride: 'carousel',
        pause: false,
        wrap: true
      });
    }

    const headers = document.querySelectorAll('.accordion-header');

    headers.forEach(header => {
      header.addEventListener('click', () => {
        const content = header.nextElementSibling;
        const isOpen = content.classList.contains('open');

        document.querySelectorAll('.accordion-content').forEach(el => el.classList.remove('open'));

        if (!isOpen) {
          content.classList.add('open');
        }
      });
    });
  });
document.addEventListener('DOMContentLoaded', function () {
  const headers = document.querySelectorAll('.accordion-header');

  headers.forEach(header => {
    header.addEventListener('click', function () {
      const content = this.nextElementSibling;

      // Toggle visibility
      content.classList.toggle('show');
    });
  });
});
