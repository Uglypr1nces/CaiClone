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
            changeUserCreds("Bobby", email, password);
            console.log("user found");
            window.location.href = "/home";
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