function mostCommon(str){
    // "elementary"
    if (str.length == 0){
        return [];
    }
    var strObject = {};
    // for loop to create an object of characters
    for (var i = 0; i < str.length; i++){
        if (str[i] in strObject){
            strObject[str[i]] += 1;
        }
        else {
            strObject[str[i]] = 1;
        }
    }
    // { e : 3, l : 1, m : 1, n : 1, t : 1, a : 1, r : 1, y : 1}
    // Find the max value
    var letterFrequency = Object.values(strObject); 
    // [3,1,1,1,1,1,1,1]
    var max = letterFrequency[0];
    for (var j = 1; j < letterFrequency.length; j++){
        if (max < letterFrequency[j]){
            max = letterFrequency[j];
        }
    }
    // max = 3
    var ans = [];
    var letterArr = Object.entries(strObject);
    // [ [e,3], [l,1], [m,1], [n,1], [t,1], [a,1], [r,1], [y,1] ]
    for ([key, value] of letterArr){
        if (value == max){
            ans.push(key);
    // ['e']
        }
    }
    return ans;
}

console.log(mostCommon("elementary"));
console.log(mostCommon("sensate"));
console.log(mostCommon("aaabbcccddeee"));
console.log(mostCommon(""));
console.log(mostCommon("abc"));
console.log(mostCommon("abbbc"));