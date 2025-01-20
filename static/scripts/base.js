var left_panel;
var main_content;
var show_button;
var greeting_title;
var user_login_button;
var characters;


let user_name = localStorage.getItem("user_name") || "";
let user_mail = localStorage.getItem("user_mail") || "";
let user_password = localStorage.getItem("user_password") || "";

var path;

document.addEventListener("DOMContentLoaded", function () {
  left_panel = document.getElementById("left-panel");
  main_content = document.getElementById("main-content");
  show_button = document.getElementById("show-panel-button");
  greeting_title = document.getElementById("greeting-title");
  user_login_button = document.getElementById("left-panel-login-button");
  characters = document.getElementsByClassName("left-panel-middle");
  path = window.location.pathname;

  if (path == "/home/") {
    if (user_name != ""){
      greeting_title.innerHTML = "Welcome " + user_name;
    }else{
      greeting_title.innerHTML = "Not logged in";
    }
  }

  getCharacters();
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

function changeUserCreds(x,y,z){
  try {
    localStorage.setItem("user_name", x);
    localStorage.setItem("user_mail", y);
    localStorage.setItem("user_password", z);

    return true;
  } catch (error) {
    console.log("Failed to change user credentials.");
    return false;
  }
}


function setCharacters(data) {
  const charactersContainer = document.getElementById("characters");

  if (!charactersContainer) {
    console.error("Element with id 'characters' not found.");
    return;
  }
  while (charactersContainer.firstChild) {
    charactersContainer.removeChild(charactersContainer.firstChild);
  }

  for (let i = 0; i < data.length; i++) {
    let character = document.createElement("div");
    character.className = "character";
    character.innerText = data[i][0]; // Assumes `data[i][0]` contains the name or text
    charactersContainer.appendChild(character);
  }
}

function getCharacters(){
  console.log("Getting characters...");
  $.ajax({
    type: "POST",
    url: "/home/get_characters/",
    success: function (data) {
      setCharacters(data.characters);
      console.log("Characters: ", data.characters);
    },
    error: function () {
      return "Error";
    },
  });
}