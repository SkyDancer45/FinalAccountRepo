document.addEventListener('DOMContentLoaded', () => {

    // Parallax effect on scroll for the hero section
    const hero = document.querySelector('.hero');
    window.addEventListener('scroll', () => {
      let offset = window.pageYOffset;
      hero.style.backgroundPositionY = offset * 0.7 + 'px';
    });
  
    // Glowing effect for the CTA button on hover
    const ctaButton = document.querySelector('.cta-button');
    ctaButton.addEventListener('mouseenter', () => {
      ctaButton.style.boxShadow = '0 0 20px 10px rgba(0, 188, 212, 0.8)';
      ctaButton.style.transform = 'scale(1.1)';
    });
  
    ctaButton.addEventListener('mouseleave', () => {
      ctaButton.style.boxShadow = '0 10px 20px rgba(0, 188, 212, 0.5)';
      ctaButton.style.transform = 'scale(1.0)';
    });
  
    // 3D Card flip on hover for feature cards
    const featureCards = document.querySelectorAll('.feature-card');
    featureCards.forEach(card => {
      card.addEventListener('mouseenter', () => {
        card.style.transform = 'rotateY(180deg)';
        card.style.transition = 'transform 0.8s';
      });
  
      card.addEventListener('mouseleave', () => {
        card.style.transform = 'rotateY(0deg)';
      });
    });
  
    // Smooth scrolling for navigation links
    const navLinks = document.querySelectorAll('nav ul li a');
    navLinks.forEach(link => {
      link.addEventListener('click', (e) => {
        e.preventDefault();
        const targetId = e.currentTarget.getAttribute('href').substring(1);
        const targetSection = document.getElementById(targetId);
        targetSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
      });
    });
  
    // Mobile menu toggle
    const menuIcon = document.querySelector('.menu-icon');
    const navMenu = document.querySelector('nav ul');
    menuIcon.addEventListener('click', () => {
      menuIcon.classList.toggle('open');
      navMenu.classList.toggle('active');
    });
  
  });