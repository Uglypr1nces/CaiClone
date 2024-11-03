var left_panel;
var main_content;
var show_button;

document.addEventListener("DOMContentLoaded", function () {
  left_panel = document.getElementById("left-panel");
  main_content = document.getElementById("main-content");
  show_button = document.getElementById("show-panel-button");
});

function hidePanel() {
  if (left_panel && main_content) {
    left_panel.style.width = "0";
    left_panel.style.padding = "0";
    left_panel.style.overflow = "hidden";
    left_panel.style.opacity = "0";
    main_content.style.flexGrow = "1";
    show_button.style.visibility = "visible";
  }
}

function showPanel() {
  if (left_panel && main_content) {
    left_panel.style.width = "20%";
    left_panel.style.padding = "";
    main_content.style.flexGrow = "1";
    left_panel.style.overflow = "visible";
    left_panel.style.opacity = "1";
    show_button.style.visibility = "hidden";
  }
}

function createCharacter() {
  console.log("redirecting to character creation");
  window.location.href = "{% url 'create_page' %}";
}

