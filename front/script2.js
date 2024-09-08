document.getElementById('menu-icon').addEventListener('click', function() {
    this.classList.toggle('open');
    document.querySelector('nav ul').classList.toggle('active');
});