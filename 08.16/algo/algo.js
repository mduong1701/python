function combine(arr1, arr2){
    if (arr1.length == 0){
        return arr2
    }
    if (arr2.length == 0){
        return arr1
    }
    var newArr = []
    if (arr1.length == arr2.length){
        for (var i = 0; i < arr1.length; i++){
            newArr += arr1[i] + arr2[i];
        }
    }
    else if (arr1.length > arr2.length){
        for (var j = 0; j < arr2.length; j++){
            newArr += arr1[j] + arr2[j];
        }
        for (var k = arr2.length ; k < arr1.length; k++){
            newArr += arr1[k];
        }
    }
    else {
        for (var a = 0; a < arr1.length; a++){
            newArr += arr1[a] + arr2[a];
        }
        for (var b = arr1.length ; b < arr2.length; b++){
            newArr += arr2[b];
        }
    }
    return newArr;
}

console.log(combine([], []))
console.log(combine([1,2,3], []))
console.log(combine([1,2,3], ['a','b','c']))
console.log(combine(['a','b','c','d'], [1,2,3,4,5]))
console.log(combine([1,2,3,4,5], ['a','b','c']))