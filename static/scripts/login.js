var email;
var password;
var logged_in;

function validate() {
  if(
    document.getElementById("email").value === "" ||
    document.getElementById("password").value === ""
  ){
    alert("Email or Password cant be blank")
  }
  else{
    email = document.getElementById("email");
    password = document.getElementById("password");
    $.ajax({
        type: "POST",
        url: "verification/",
        data: {
          email: email.value,
          password: password.value,
        },
        success: function (data) {
          if (data != "User verified successfully"){
            alert("User not found with that password and email combination")
            document.getElementById("email").value = "";
            document.getElementById("password").value = "";
          }
          else{
            $.ajax({
              type: "POST",
              url: "get_user_name/",
              data: {
                email: email.value,
              },
              success: function (data) {
                console.log(data);
                localStorage.setItem("user_name", data);
                if (changeUserCreds(data, email.value, password.value)) {
                  window.location.href = "/home/";
                } else {
                  alert("Failed to change user Credentials.");
                }
              },
              error: function () {
                alert("Failed to verify user.");
              },
            });
          }
        },
        error: function () {
          alert("Failed to verify user.");
        },
      }); 
  }
}


function signUp() {
  window.location.href = "/home/signup"
}

document.addEventListener('keyup', (event) => {
  if (event.key == 'Enter') {
    validate();
  }
  else if(event.key == 'Escape'){
    window.location.href = "/home";
  }
});