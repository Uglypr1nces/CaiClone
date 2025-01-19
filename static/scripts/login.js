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
    
    console.log(email.value);
    console.log(password.value);
  
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
            
            user_name = localStorage.getItem("user_name");
            if (user_name === null){
              $.ajax({
                type: "POST",
                url: "get_user_name/",
                data: {
                  email: email.value,
                },
                success: function (data) {
                  localStorage.setItem("user_name", data.user_name);
                  if(changeUserCreds(data.user_name, email.value, password.value)){
                    window.location.href = "/home/";
                  }
                  else{
                    alert("Failed to change user Credentials.");
                  }
                },
                error: function () {
                  alert("Failed to verify user.");
                },
              });
              changeUserCreds(user_name, email.value, password.value);
              window.location.href = "/home/";
            }
            else{
              changeUserCreds(user_name, email.value, password.value);
              window.location.href = "/home/";
            }
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