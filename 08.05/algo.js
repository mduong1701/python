// function square_array(arr){
//     for (var i = 0; i < arr.length; i++){
//         arr[i] = arr[i] ** 2;
//     }
//     return arr;
// };

// console.log(square_array([1,2,3,4,5]))
// console.log(square_array([]))
// console.log(square_array([9]))

// function strMultiply(str, num){
//     var newStr = "";
//     for (var i = 0; i < num; i++){
//         newStr += str;
//     }
//     return newStr;
// }

// console.log(strMultiply("hey", 5))
// console.log(strMultiply(" ", 5))
// console.log(strMultiply("hey", 0))

// function coinChange(cents){
//     var coins = {
//         "quarters": 0,
//         "dimes": 0,
//         "nickels": 0,
//         "pennies": 0
//     };
    
//     coins["quarters"] = Math.floor(cents/25);
//     cents %= 25;
//     coins["dimes"] = Math.floor(cents/10);
//     cents %= 10;
//     coins["nickels"] = Math.floor(cents/5);
//     cents %= 5;
//     coins["pennies"] = cents;
//     return coins;
// };

// console.log(coinChange(72));
// console.log(coinChange(99));
// console.log(coinChange(100));
// console.log(coinChange(1));
// console.log(coinChange(6));

function dollarAndCoinChange(cents){
    var change = {
        "tens": 0,
        "fives": 0,
        "ones": 0,
        "quarters": 0,
        "dimes": 0,
        "nickels": 0,
        "pennies": 0
    };
    change["tens"] = Math.floor(cents/1000)
    cents %= 1000
    change["fives"] = Math.floor(cents/500)
    cents %= 500
    change["ones"] = Math.floor(cents/100)
    cents %= 100
    change["quarters"] = Math.floor(cents/25);
    cents %= 25;
    change["dimes"] = Math.floor(cents/10);
    cents %= 10;
    change["nickels"] = Math.floor(cents/5);
    cents %= 5;
    change["pennies"] = cents;
    return change;
};

console.log(dollarAndCoinChange(9999));
console.log(dollarAndCoinChange(999));
console.log(dollarAndCoinChange(99));
console.log(dollarAndCoinChange(9));
console.log(dollarAndCoinChange(0));