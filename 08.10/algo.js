// function spaces(str){
//     var count = 0;
//     for (var i = 0; i < str.length; i++){
//         if (str[i] == " "){
//             count++;
//         }
//     }
//     return count;
// }

// const str1 = ""
// const str2 = "a b"
// const str3 = "a b c"
// const str4 = " a b c"
// const str5 = "a b c d "

// console.log(spaces(str1));
// console.log(spaces(str2));
// console.log(spaces(str3));
// console.log(spaces(str4));
// console.log(spaces(str5));

// -----------------------------------------------------

// function countFun(str, val){
//     var count = 0;
//     for (var i = 0; i < str.length; i++){
//         if (str[i] == val){
//             count++;
//         }
//     }
//     return count;
// }
// const str1 = "b"
// const str2 = "a b"
// const str3 = "a b a c"
// const str4 = " a b a c a"
// const str5 = "a b a c a a d "

// console.log(countFun(str1, "a"));
// console.log(countFun(str2, "a"));
// console.log(countFun(str3, "a"));
// console.log(countFun(str4, "a"));
// console.log(countFun(str5, "a"));

// -----------------------------------------------------

//write a function to count the number of spaces in a string
//return that count


//write a function that takes in a string str, and a search string val
//count the number of appearences of val in str
//val will always be a string of length 1, no more, no less

//Write an algorithm that takes in a string and checks to make sure the parentheses are valid.
//all '(' should have a matching ')'
//parentheses should also be in the correct order(i.e. ')(' would not be valid)

//example: ()           -> true
//example: (([(8+13)])) -> true
//example: (()))()      -> false
//example: (            -> false
//example: ())())((()   -> false

function parensValid(input){
    var count = 0;
    for (var i = 0; i < input.length; i++){
        if (input[i] == "("){
            count++;
        }
        else if(input[i] == ")"){
            count--;
            if (count < 0){
                return false;
            }
        }
    }
    return (count == 0)
}
    // if (count != 0){
    //     return false
    // }
    // return true


console.log(parensValid("()"));
console.log(parensValid("(([(8+13)]))"));
console.log(parensValid("(()))()"));
console.log(parensValid("("));
console.log(parensValid("())())((()"));