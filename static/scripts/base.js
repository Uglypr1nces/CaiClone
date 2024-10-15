var left_panel;

document.addEventListener("DOMContentLoaded", function () {
  left_panel = document.getElementById("left-panel");
});

function hidePanel() {
  if (left_panel) {
    left_panel.style.visibility = "hidden";
  }
}

function showPanel() {
  if (left_panel) {
    left_panel.style.visibility = "visible";
  }
}

function selectCharacter() {}

function loadCharacter() {}

function createCharacter() {}
$.ajax({
  type: "GET",
  url: "/create_page",
  success: function (data) {
    alert("successfull");
  },
  failure: function () {
    alert("failure");
  },
});

function sendCommand(command) {
  var xhr = new XMLHttpRequest();
  xhr.open("POST", "{% url " + command + "", true);
  xhr.setRequestHeader("X-CSRFToken", "{{ csrf_token }}");
  xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
  xhr.send("command=" + command);
}
