function balanceIndex(arr){
    var index = -1;
    if (arr.length == 0){
        return index;
    }

    if (arr.length == 1){
        return index = 0;
    }

    if (arr.length == 2){
        return index;
    }

    for (var i = 1; i < arr.length; i++){
        var leftSum = 0, rightSum = 0;
        for (var j = i - 1; j >= 0; j--){
            leftSum += arr[j];
        }
        for (var k = i + 1; k < arr.length; k++){
            rightSum += arr[k];
        }
        if (leftSum == rightSum){
            index = i;
        }
    }
    return index;
}
    
console.log(balanceIndex([]));
console.log(balanceIndex([2]));
console.log(balanceIndex([1,2]));
console.log(balanceIndex([1,2,1]));
console.log(balanceIndex([1,2,1,7,4]));
console.log(balanceIndex([1,2,1,7,4,11]));