function spaceCount(str){
    var count = 0;
    for (var i = 0; i < str.length; i++){
        if (str[i] == " "){
            count++;
        }
    }
    return count;
}

// console.log(spaceCount(""));
// console.log(spaceCount(" "));
// console.log(spaceCount(" hi "));
// console.log(spaceCount(" hi everyone "));
// console.log(spaceCount(" a b c d"));

function reverseString(phrase){
    var result = "";
    for (var i = phrase.length - 1; i >= 0; i--){
        result += phrase[i];
    }
    return result;
}

// console.log(reverseString("Hello World!"));
// console.log(reverseString("a b c"));

function reverseWords(str) {
    var strArray = str.split(" ");
    var finalResult = "";
    for (var i = 0; i < strArray.length; i++){
        finalResult += reverseString(strArray[i]);
        if (i != strArray.length - 1){
            finalResult += " ";
        }
    }
    return finalResult;
}

// var str1 = "hello";
// var expected1 = "olleh";
// console.log(reverseWords(str1));

// var str2 = "hello world";
// var expected2 = "olleh dlrow";
// console.log(reverseWords(str2));

// var str3 = "abc def ghi";
// var expected3 = "cba fed ihg";
// console.log(reverseWords(str3));


//write a function that, given a string of words(with spaces),
//returns a new string with words in reverse sequence.
//"This is a test" -> "test a is This"
// const reverseWordOrder = (str) => {
// }
function reverseWordOrder(str){
    var strArray = str.trim().split(/\s+/);
    var result = "";
    var left = 0;
    var right = strArray.length - 1;
    while (left < right){
        var temp = strArray[left];
        strArray[left] = strArray[right];
        strArray[right] = temp;
        left++;
        right--;
    }
    for (var i = 0; i < strArray.length; i++){
        result += strArray[i];
        if (i != strArray.length - 1){
            result += " ";
        }
    }
    return result;
}

console.log(reverseWordOrder("Did I shine my shoes       today?        "));
console.log(reverseWordOrder("'Son, I am able,' she said 'Though you scare me' 'Watch,' said I 'beloved,' I said, 'Watch me scare you though,' Said she, 'Able am I son.'"))
console.log(reverseWordOrder("This is freaking insane because I live in Cincinnati but I want to live in Mississippi with my family!"));
