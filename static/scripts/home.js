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

    console.log(character_name);
    console.log(character_description);

    $.ajax({
      type: "POST",
      url: "chat/",
      data: {
        name: character_name,
        description: character_description,
      },
      success: function (data) {
        console.log(data);
      },
      error: function () {
        alert("Failed to chat with character.");
      },
    });
  }
});
