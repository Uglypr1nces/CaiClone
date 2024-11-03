var email;
var password;

  function validate() {
    email = document.getElementById("email");
    password = document.getElementById("password");
    
    console.log(email.value);
    console.log(password.value);

    $.ajax({
        type: "POST",
        url: "verfication/",
        data: {
          email: email,
          password: password,
        },
        success: function (data) {
          alert("User verified successfully!");
          window.location.href = "/home";
        },
        error: function () {
          alert("Failed to create character.");
        },
      });
  }