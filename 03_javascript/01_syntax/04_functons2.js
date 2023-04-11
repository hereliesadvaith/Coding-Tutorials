var numbers = [3, 56, 1, 48, 5];

//Map -Create a new array by doing something with each item in an array.
function double(num) {
    return num * 2;
};
var result = numbers.map(double);
console.log(result)

//Filter - Create a new array by keeping the items that return true.
result = numbers.filter(function (num) {
    return num > 10;
});
console.log(result)

//Reduce - Accumulate a value by doing something to each item in an array.
result = numbers.reduce(function (accumulator, currentNumber) {
    return accumulator - currentNumber;
});
console.log(result)

//Find - find the first item that matches from an array.
result = numbers.find(function (num) {
    return num > 10;
});
console.log(result)

//FindIndex - find the index of the first item that matches.
result = numbers.findIndex(function (num) {
    return num < 3;
});
console.log(result)

//substring
const paragraph = "Hey if we are both unmarried when we are 40 i will marry you";
result = paragraph.substring(0, 11);
console.log(result)

//Arrow functions
result = numbers.map(num => (num * 2));

result = numbers.filter(num => (num > 10));

result = numbers.reduce((accumulator, currentNumber) => (accumulator + currentNumber));