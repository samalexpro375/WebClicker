const clickButton = document.getElementById('click-button');
const money_el = document.getElementById('money');
let mn = 0;
let a = 1;

function updateClickCount() {
    clickCountElement.textContent = mn;
}
clickButton.addEventListener('click', function() {
    mn += a
    updateClickCount()
});

updateClickCount();
