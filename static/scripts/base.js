var left_panel;

document.addEventListener("DOMContentLoaded", function() {
    left_panel = document.getElementById('left-panel');
});

function hidePanel() {
    if (left_panel) {
        left_panel.style.visibility = 'hidden';
    }
}

function showPanel() {
    if (left_panel) {
        left_panel.style.visibility = 'visible';
    }
}
