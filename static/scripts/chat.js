let character_name;
let character_description;
let chat;
document.addEventListener("DOMContentLoaded", function () {
  character_name = localStorage.getItem("character_name");
  character_description = localStorage.getItem("character_description");

  if (character_name == "" || character_description == "") {
    alert("No character selected.");
    window.location.href = "/home";
  } else {
    document.getElementById("character-name").innerText = character_name;
    document.getElementById("character-description").innerText =
      character_description;
  }
});

function sendUserInput() {
  let user_input = document.getElementById("user-input").value;

  $.ajax({
    type: "POST",
    url: "userMessage/",
    data: {
      user_message: user_input,
    },
    success: function (data) {
      alert("Message sent successfully!");
    },
    error: function () {
      alert("Failed to send Message.");
    },
  });
}
