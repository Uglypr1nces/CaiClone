let character_div;

document.addEventListener("DOMContentLoaded", function () {
  character_div = document.getElementsByClassName("card mb-3");
});

document.addEventListener("click", function () {
  if (event.target.closest(".card.mb-3")) {
    character_name =
      character_div[0].getElementsByClassName("card-title")[0].innerText;
    character_description =
      character_div[0].getElementsByClassName("card-text")[0].innerText;

    if (character_name != "") {
      localStorage.setItem("character_name", character_name);
      localStorage.setItem("character_description", character_description);
      window.location.href = "/home/chat";
    } else {
      console.log("No character selected.");
    }
  }
});
