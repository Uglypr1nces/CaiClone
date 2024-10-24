let character_name;
let character_description;
let chat;

document.addEventListener("DOMContentLoaded", function () {
  character_name = localStorage.getItem("character_name");
  if (character_name == "" || character_description == "") {
    alert("No character selected.");
    window.location.href = "/home";
  } else {
    document.getElementById("character-name").innerText = character_name;
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
      let chatBox = document.getElementById("chat-box");
      let newMessage = document.createElement("div");
      let receivedMessage = document.createElement("div");
      newMessage.classList.add("user-message");
      newMessage.innerText = user_input;
      receivedMessage.classList.add("user-message");
      receivedMessage.innerText = data.response;
      chatBox.appendChild(newMessage);
      chatBox.appendChild(receivedMessage);
      document.getElementById("user-input").value = "";
    },
    error: function () {
      alert("Failed to send Message.");
    },
  });
}
