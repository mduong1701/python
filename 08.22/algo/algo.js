// function maxArr(arr){
//     ans = [];
//     if (arr.length == 0){
//         return []
//     }
//     maxNum = arr[0]
//     for (var i = 1; i < arr.length; i++){
//         if (maxNum < arr[i]){
//             maxNum = arr[i]
//         }
//     }
//     for (var j = 0; j < arr.length; j++){
//         if (maxNum == arr[j]){
//             ans.push(j);
//         }
//     }
//     return ans;
// }

// console.log(maxArr([]));
// console.log(maxArr([1]));
// console.log(maxArr([1,5]));
// console.log(maxArr([5,2,5]));
// console.log(maxArr([8,3,8,4,8]));

// function freArr(arr){
//     if (arr.length == 0 || arr.length == 1){ 
//         return arr
//     }
//     numDict = {}
//     for (i in arr){
//         if (i in numDict){
//             numDict[i] += 1;
//         }
//         else {
//             numDict[i] = 1;
//         }
//     }

// }