let character_name;
let character_description;
let waiting_animation;

document.addEventListener("DOMContentLoaded", function () {
  character_name = localStorage.getItem("character_name");
  character_description = localStorage.getItem("character_description");
  waiting_animation = document.getElementById("loading_animation");
  
  // Check if character details are missing or null
  if (!character_name || !character_description) {
    alert("No character selected.");
    window.location.href = "/home";
    return;
  }

  waiting_animation.style.visibility = "hidden";
  document.getElementById("character-name").innerText = character_name;

  // Display character description
  let description = document.createElement("div");
  description.classList.add("message", "bot-message");
  description.innerText = character_description;
  document.getElementById("chat-box").appendChild(description);
});

function sendUserInput() {
  let user_input = document.getElementById("input-box").value.trim();

  if (!user_input) {
    alert("Please enter a message.");
    return;
  }

  waiting_animation.style.visibility = "visible";

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
      let userMessage = document.createElement("div");
      let botMessage = document.createElement("div");

      userMessage.classList.add("message", "user-message");
      userMessage.innerText = user_input;

      botMessage.classList.add("message", "bot-message");
      botMessage.innerText = data;

      chatBox.appendChild(userMessage);
      chatBox.appendChild(botMessage);

      document.getElementById("input-box").value = ""; // Clear input box
      waiting_animation.style.visibility = "hidden"; // Hide loading animation
    },
    error: function (xhr, status, error) {
      console.error("Error:", error);
      alert("Failed to send message. Please try again.");
      waiting_animation.style.visibility = "hidden"; // Hide loading animation
    },
  });
}

document.addEventListener('keyup', (event) => {
  if (event.key == 'Enter') {
    sendUserInput();
  }
  else if(event.key == 'Escape'){
    window.location.href = "/home";
  }
});