let character_div;

document.addEventListener("DOMContentLoaded", function () {
  character_div = document.getElementsByClassName("card mb-3");
  console.log("loaded home");
  localStorage.clear();
});

document.addEventListener("click", function (event) {
  const clickedCard = event.target.closest(".card.mb-3");
  if (clickedCard) {
    const character_name =
      clickedCard.getElementsByClassName("card-title")[0].innerText;
    const character_description =
      clickedCard.getElementsByClassName("card-text")[0].innerText;
    const character_id = 
      clickedCard.getElementsByClassName("card-id")[0].innerText;

    if (character_name != "") {
      localStorage.setItem("character_name", character_name);
      localStorage.setItem("character_description", character_description);
      localStorage.setItem("character_id", character_id)
      window.location.href = "/home/chat";
    } else {
      console.log("No character selected.");
    }
  }
});
