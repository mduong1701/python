//write a function to take in an array of strings
//each string in the array should be doubled up
//return the array
//ex. ["hi","m","hello","x"] -> ["hihi","mm","hellohello","xx"]
// function double(arr){
//     for (var i = 0; i < arr.length; i++){
//         arr[i] += arr[i];
//     }
//     return arr;
// }

// list = ["hi","m","hello","x"];
// console.log(double(list))
// ---------------------------------------------------------------------
/* 
Given an array of strings
return the number of times each string occurs (a frequency / hash table)
*/
function makeFrequencyTable(arr){
    var wordCount = {};
    for (var i = 0; i < arr.length; i++){
        if (!(arr[i] in wordCount)){
            wordCount[arr[i]] = 1;
        }
        else{
            wordCount[arr[i]]++;
        }
    }
    return wordCount;
}

const arr1 = ["a", "a", "a"];
// const expected1 = {
//   a: 3,
// };
console.log(makeFrequencyTable(arr1));

// ---------------------------------------------------------------------

// const arr2 = ["a", "b", "a", "c", "B", "c", "c", "d"];
// const expected2 = {
//   a: 2,
//   b: 1,
//   c: 3,
//   B: 1,
//   d: 1,
// };
// console.log(makeFrequencyTable(arr2));

// const arr3 = [];
// const expected3 = {};
// console.log(makeFrequencyTable(arr3));

// const arr4 = ["r","r","a","q","h","a","h","a","h","a","1"," ","r"];
// const expected4 = {
//     "r":3,
//     "a":4,
//     "q":1,
//     "h":3,
//     "1":1,
//     " ":1
// };
// console.log(makeFrequencyTable(arr4));

// /* 
// Given a non-empty array of odd length containing ints where every int but one
// has a matching pair (another int that is the same)
// return the only int that has no matching pair.
// */
function oddOccurrencesInArray(nums){
    var numCount = makeFrequencyTable(nums);
    console.log(numCount);
    var result = [];
    for (var key in numCount){
        if (numCount[key] % 2 == 1){
            result.push(key);
        }
    }
    return result;
}

// const nums1 = [1,2];
// const expected_b1 = 1;
// console.log(oddOccurrencesInArray(nums1));

// const nums2 = [5, 4, 5];
// const expected_b2 = 4;
// console.log(oddOccurrencesInArray(nums2));

// const nums3 = [5, 4, 3, 4, 3, 4, 5];
// const expected_b3 = 4; // there is a pair of 4s but one 4 has no pair.
// console.log(oddOccurrencesInArray(nums3))

// const nums4 = [5, 2, 6, 2, 3, 1, 6, 3, 2, 5, 2, 2];
// const expected_b4 = 1;
// console.log(oddOccurrencesInArray(nums4));