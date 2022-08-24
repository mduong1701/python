//write a function that takes in two SORTED arrays
//your function should weave these two arrays together
//into one single sorted array
//ex. [1,3,5,9] and [2,3,3,4,6,7,8,10] -> [1,2,3,3,3,4,5,6,7,8,9,10]
function combineArrays(arr1,arr2){
    var ans = [];
    var i = 0, j = 0;
    while (i < arr1.length && j < arr2.length){
        if (arr1[i] == arr2[j]){
            ans.push(arr1[i]);
            ans.push(arr2[j]);
            i++;
            j++;
        }
        else if (arr1[i] > arr2[j]){
            ans.push(arr2[j]);
            j++;
        }
        else {
            ans.push(arr1[i]);
            i++;
        }
    }
    if (i >= arr1.length){
        while (j < arr2.length){
            ans.push(arr2[j]);
            j++;
        }  
    }
    if (j >= arr2.length){
        while (i < arr1.length){
            ans.push(arr1[i]);
            i++;
        }  
    }


    return ans;
}

console.log(combineArrays([1,3,5,9],[2,3,3,4,6,7,8,10]));