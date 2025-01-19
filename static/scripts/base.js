var left_panel;
var main_content;
var show_button;
var greeting_title;

let user_name = localStorage.getItem("user_name") || "";
let user_mail = localStorage.getItem("user_mail") || "";
let user_password = localStorage.getItem("user_password") || "";

var path;

document.addEventListener("DOMContentLoaded", function () {
  left_panel = document.getElementById("left-panel");
  main_content = document.getElementById("main-content");
  show_button = document.getElementById("show-panel-button");
  greeting_title = document.getElementById("greeting-title");

  path = window.location.pathname;

  if (path == "/home/") {
    if (user_name != ""){
      greeting_title.innerHTML = "Welcome " + user_name;
    }else{
      greeting_title.innerHTML = "Not logged in";
    }
  }

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
  if (typeof(x) === "string" && typeof(y) === "string" && typeof(z) === "string"){
      user_name = x;
      user_mail = y;
      user_password = z;
      
      localStorage.setItem("user_name", user_name);
      localStorage.setItem("user_mail", user_mail);
      localStorage.setItem("user_password", user_password);

      console.log("Changed User Credentials to: ");
      console.log("Username: " + user_name);
      console.log("Email: " + user_mail);
      console.log("Password:  " + user_password);
      return true;
  }
  else{
      console.log("Invalid input types: ", typeof(x), typeof(y), typeof(z));
      return false;
    }
}

