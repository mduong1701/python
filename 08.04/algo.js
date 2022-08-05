// write a function that will print the integers 100 - 1000
// function printInt(x, y){
//     for (var i = x; i <= y; i++){
//         console.log(i);
//     }
// }
// printInt(100, 1000)

// Write a function that will add up the sum of the integers 0 -200
// function sumUp(x, y){
//     var sum = 0;
//     for (var i = x; i <= y; i++){
//         sum += i;
//     }
//     return sum;
// }
// console.log(sumUp(0, 200));

// Encode
// function encode(str){
//     var result = "";
//     for (var i = 0; i < str.length; i++){
//         start = str[i];
//         var count = 1;
//         while (str[i] == str[i+1]){
//             count++;
//             i++;
//         }
//         result = result + str[i] + count;
//     }
//     return result;
// }

// console.log(encode("aaabbcccc"))
// console.log(encode("ddddeeeeeffgggg"))
// // console.log(encode("aaaaabbbbbbbc"))
// // console.log(encode("bb"))

// Decode

function decode(str) {
    var result = "";
    var i = 0;
    while (i < str.length) {
        current_letter = str[i];
        var count = str[i + 1];
        if ((i + 2) < str.length) {
            if (str[i + 2].toLowerCase() === str[i + 2].toUpperCase()) {
                count += str[i + 2];
                i += 3;
            }
            else {
                i += 2;
            }
        }
        else {
            i += 2;
        }
        for (var j = 0; j < parseInt(count); j++) {
            result += current_letter;
        }
    }
    return result;
}
console.log(decode("a1b15c5d12"));
console.log(decode("a12b5c15d2"));
console.log(decode("a5b1c5d3"));
console.log(decode("a12b10c13d4e15"));