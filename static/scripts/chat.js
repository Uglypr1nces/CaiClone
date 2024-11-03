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
    let description = document.createElement("div");
    description.classList.add("message", "bot-message"); 
    description.innerText = character_description;
    document.getElementById("chat-box").appendChild(description);
  }
});

function sendUserInput() {
  let user_input = document.getElementById("input-box").value;

  $.ajax({
    type: "POST",
    url: "userMessage/",
    data: {
      character_name: character_name,
      character_description: character_description,
      user_message: user_input,
    },
    success: function (data) {
      console.log(data);
      let chatBox = document.getElementById("chat-box");
      let newMessage = document.createElement("div");
      let receivedMessage = document.createElement("div");
      newMessage.classList.add("message", "user-message");
      newMessage.innerText = user_input;
      receivedMessage.classList.add("message", "bot-message");
      receivedMessage.innerText = data;
      chatBox.appendChild(newMessage);
      chatBox.appendChild(receivedMessage);
      document.getElementById("chat-box").value = "";
    },
    error: function () {
      alert("Failed to send Message.");
    },
  });
}
