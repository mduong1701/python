// function getUser(){
//     var count = document.querySelector(".display");
//     count.innerText = "Hi Man, how are you?";
// };

// async function getCoderData() {
//     // The await keyword lets js know that it needs to wait until it gets a response back to continue.
//     var response = await fetch("https://api.github.com/users/adion81");
//     // We then need to convert the data into JSON format.
//     var coderData = await response.json();
//     return coderData;
// }
// console.log(getCoderData());

async function getUser(){
    var count = document.querySelector(".display");

    var response = await fetch("https://api.github.com/users/adion81");
    var coderData = await response.json();
    console.log(coderData);
    count.src = coderData.avatar_url;
}