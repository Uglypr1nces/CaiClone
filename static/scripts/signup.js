var email;
var password;
var username;
var logged_in;

function createUser() {
  if(
    document.getElementById("username").value === "" ||
    document.getElementById("email").value === "" ||
    document.getElementById("password").value === ""
  ){
    alert("Email or Password cant be blank")
  }
  else{
    username = document.getElementById("username");
    email = document.getElementById("email");
    password = document.getElementById("password");
  
    $.ajax({
        type: "POST",
        url: "create_user/",
        data: {
          username: username.value,
          email: email.value,
          password: password.value,
        },
        success: function (data) {
          if (data != "User created successfully"){
            alert("Couldnt create user, please try again")
            document.getElementById("username").value = "";
            document.getElementById("email").value = "";
            document.getElementById("password").value = "";
          }
          else{
            changeUserCreds(username, email, password);
            window.location.href = "/home";
          }
        },
        error: function () {
          alert("Failed to verify user.");
        },
      }); 
  }
}


document.addEventListener('keyup', (event) => {
  if (event.key == 'Enter') {
    createUser();
  }
  else if(event.key == 'Escape'){
    window.location.href = "/home";
  }
});