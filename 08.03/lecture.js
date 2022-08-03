// function join(arr, separator) {
//     var str = ""
//     for (var i = 0; i < arr.length; i++){
//         if (i != arr.length - 1){
//             str = str + arr[i] + separator;
//         }
//         else {
//             str += arr[i];
//         }
//     }
//     return str
// }

// var arr1 = [1, 2, 3];
// var separator1 = ", ";
// var expected1 = "1, 2, 3";
// console.log(join(arr1,separator1));

// var arr2 = [1, 2, 3];
// var separator2 = "-";
// var expected2 = "1-2-3";
// console.log(join(arr2,separator2));

// var arr3 = [1, 2, 3];
// var separator3 = " - ";
// var expected3 = "1 - 2 - 3";
// console.log(join(arr3,separator3));

// var arr4 = [1];
// var separator4 = ", ";
// var expected4 = "1";
// console.log(join(arr4,separator4));

// var arr5 = [];
// var separator5 = ", ";
// var expected5 = "";
// console.log(join(arr5,separator5));
// console.log("==============================================")

function bookIndex(nums) {
    var str = "";
    var i = 0;
    var end = 0;
    while (i < nums.length){
        str += nums[i];
        end = i + 1;
        while (end < nums.length && nums[end] == nums[end - 1] + 1){
            end += 1;
            i = end;
        };
    };
    return str
};

const nums1 = [1, 13, 14, 15, 37, 38, 70];
// const output1 = bookIndex(nums1);
// const expected1 = "1, 13-15, 37-38, 70";
// console.assert(output1 === expected1, {output: output1});

console.log(bookIndex(nums1))

// const nums2 = [5, 6, 7, 8, 9];
// const output2 = bookIndex(nums2);
// // const expected2 = "5-9";
// // console.assert(output2 === expected2, {output: output2});
// console.log(bookIndex(nums2))

// const nums3 = [1, 2, 3, 7, 9, 15, 16, 17];
// // const output3 = bookIndex(nums3);
// // const expected3 = "1-3, 7, 9, 15-17";
// // console.assert(output3 === expected3, {output: output3});
// console.log(bookIndex(nums3))