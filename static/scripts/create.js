var character_name;
var character_description;

document.addEventListener("DOMContentLoaded", function () {});

function createCharacter() {
  if (
    document.getElementById("character-name").value === "" ||
    document.getElementById("character-description").value === ""
  ) {
    alert("Please fill out all fields.");
    return;
  } else {
    character_name = document.getElementById("character-name").value;
    character_description = document.getElementById(
      "character-description"
    ).value;

    console.log(character_name);
    console.log(character_description);

    $.ajax({
      type: "POST",
      url: "/create_character",
      data: {
        name: character_name,
        description: character_description,
      },
      success: function (data) {
        alert("Character created successfully!");
        window.location.href = "/home";
      },
      error: function () {
        alert("Failed to create character.");
      },
    });
  }
}
