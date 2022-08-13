//write a function that accepts a string str
//make a new string that contains only the first half
//of str and return that string
//for odd lengths, take the floor of the halfway index
//"salutations!" -> "saluta"
//"can you really include a sentence this long" -> "can you really includ"
// function firstHalf(str){
//     var result = "";
//     var num = Math.floor(str.length/2);
//     for (var i = 0; i < num; i++){
//         result += str[i];
//     }
//     return result;
// }

// console.log(firstHalf("Hello"));
// console.log(firstHalf("Hello there"));
// console.log(firstHalf("Hi"));
// console.log(firstHalf(""));
// console.log(firstHalf("!?"));

// //Create a standalone function that accepts a string
// //and an integer, and rotates the characters in the
// //string to the right by that amount.
// //this one must be done without built in methods
// //("Did I shine my shoes today?", 9) ->
// //"es today?Did I shine my sho"
function rotateString(str, num){
    var result = "";
    for (var i = str.length - num; i < str.length; i++){
        result += str[i];
    }
    for (var j = 0; j < str.length - num; j++){
        result += str[j];
    }
    return result;
} 
function isRotation(str1, str2){
    for (var i = 0; i < str1.length; i++){
        if (rotateString(str1, i) == str2){
            return true;
        }
    }
    return false;
}

console.log(isRotation("Did I shine my shoe today?", "es today?Did I shine my sho"));
console.log(isRotation("Did I shine my shoes today?","es today?Did I shine my sho"));
