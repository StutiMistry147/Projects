
const themeToggle = document.getElementById('theme-toggle');
const body = document.body;

themeToggle.addEventListener('click', () => {
    body.classList.toggle('dark-mode');
});

const backToTop = document.getElementById('back-to-top');
window.addEventListener('scroll', () => {
    if (window.scrollY > 300) {
        backToTop.style.display = 'block';
    } else {
        backToTop.style.display = 'none';
    }
});

backToTop.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
});

const tagline = document.querySelector('.tagline');
const phrases = [
    "Python, C++, Web Development & Cybersecurity Enthusiast",
    "Building Cute & Interactive Apps",
    "Learning and Sharing Projects Daily"
];

let currentPhrase = 0;
let currentChar = 0;

function typeEffect() {
    if (currentChar < phrases[currentPhrase].length) {
        tagline.textContent += phrases[currentPhrase][currentChar];
        currentChar++;
        setTimeout(typeEffect, 50);
    } else {
        setTimeout(eraseEffect, 2000);
    }
}

function eraseEffect() {
    if (currentChar > 0) {
        tagline.textContent = phrases[currentPhrase].substring(0, currentChar - 1);
        currentChar--;
        setTimeout(eraseEffect, 25);
    } else {
        currentPhrase = (currentPhrase + 1) % phrases.length;
        setTimeout(typeEffect, 500);
    }
}

document.addEventListener('DOMContentLoaded', typeEffect);

const cards = document.querySelectorAll('.project-card');

const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('show');
        }
    });
}, { threshold: 0.2 });

cards.forEach(card => {
    observer.observe(card);
});
