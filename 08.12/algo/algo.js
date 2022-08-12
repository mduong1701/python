function trim(str){
    var newStr ="";
    for (var i = 0; i < str.length; i++){
        if ((str[i] == " ") && (str[i-1] != " ") && (str[i+1] != " ") && ((i - 1) >= 0) && ((i + 1) < str.length)){
            newStr += str[i];
        }
        if (str[i] != " "){
            newStr += str[i];
        }
    }
    return newStr;
}

var str5 = "     hello world      ";
console.log(trim(str5));
console.log(trim("   aaa bbb ccc   "));
console.log(trim("aaa bbb ccc   "));
console.log(trim("   aaa bbb ccc"));

// ======================================================

function isAnagram(s1, s2){
    if (s1.length != s2.length){
        return false
    }
    var d1 = {}
    var d2 = {}
    for (var i = 0; i < s1.length; i++){
        if (!(s1[i] in d1)){
            d1[s1[i]] = 1;
        }
        else {
            d1[s1[i]] += 1;
        }
    }

    for (var j = 0; j < s2.length; j++){
        if (!(s2[j] in d2)){
            d2[s2[j]] = 1;
        }
        else {
            d2[s2[j]] += 1;
        }
    }
    for (var i = 0; i < s1.length; i++){
        if (!(s1[i] in d2)){
            return false
        }
        if (d1[s1[i]] != d2[s1[i]]){
            return false
        }
    }
    return true
}

console.log(isAnagram("yes", "eys"));
console.log(isAnagram("aaabbbb", "bbbbaaa"));
console.log(isAnagram("aaabbbb", "aabbbbb"));
