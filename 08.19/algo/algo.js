function findNotDuplicate(arr){
    var count = {};
    for (var i = 0; i < arr.length; i++){
        if (!(arr[i] in count)){
            count[arr[i]] = 1;
        }
        else {
            count[arr[i]]++;
        }
    }
    for (var j in count){
        if (count[j] == 1){
            return j;
        }
    }
    return null
}

arr1 = [3,5,4,3,4,6,5];
arr2 = [3,5,5];
arr3 = [3,3,5];
arr4 = [5];
arr5 = [];

console.log(findNotDuplicate(arr1));
console.log(findNotDuplicate(arr2));
console.log(findNotDuplicate(arr3));
console.log(findNotDuplicate(arr4));
console.log(findNotDuplicate(arr5));