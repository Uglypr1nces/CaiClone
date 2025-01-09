let user_name = "";
let user_mail = "";
let user_password = "";

document.addEventListener("DOMContentLoaded", function(){
    //onload
});

function changeUserCreds(x,y,z){
    if (typeof(x) == String & typeof(x) == String & typeof(x) == String){
        user_name = x;
        user_mail = y;
        user_password = z;
    }
    else{
        console.log("User Credentials are NOT string.")
    }
}