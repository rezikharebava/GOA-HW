// settings.js

const toggle = document.getElementById('modeToggle');
const label = document.getElementById('modeLabel');

// Load saved mode from localStorage
const savedMode = localStorage.getItem('mode');
if (savedMode === 'dark') {
    document.documentElement.classList.add('dark');
    toggle.checked = true;
    label.textContent = 'Dark Mode';
}

// Toggle theme
toggle.addEventListener('change', () => {
    if (toggle.checked) {
        document.documentElement.classList.add('dark');
        localStorage.setItem('mode', 'dark');
        label.textContent = 'Dark Mode';
    } else {
        document.documentElement.classList.remove('dark');
        localStorage.setItem('mode', 'light');
        label.textContent = 'Light Mode';
    }
});