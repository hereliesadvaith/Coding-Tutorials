// Array
var guestList = ["Achu", "Nichu", "Hari", "Lechu"];
console.log(guestList);
console.log(guestList[0]);
// check item
console.log(guestList.includes("Nihu"));
guestList.push("Nihu"); // guestList.pop for delete
console.log(guestList);

// while loop

var output1 = [];
var number = 1;
function fizBuzz() {
    if (number % 3 === 0) {
        if (number % 5 === 0) {
            output1.push("FizBuzz");
        } else {
            output1.push("Fiz");
        };
    } else if (number % 5 === 0) {
        output1.push("Buzz");
    } else {
        output1.push(number);
    };
    number++;
};

while (number <= 100) {
    fizBuzz();
};

console.log(output1);

// for loop

var output2 = [];
function fizBuzzz(number) {
    if (number % 3 === 0) {
        if (number % 5 === 0) {
            output2.push("FizBuzz");
        } else {
            output2.push("Fiz");
        };
    } else if (number % 5 === 0) {
        output2.push("Buzz");
    } else {
        output2.push(number);
    };
};

for (var i = 1; i < 101; i++) {
    fizBuzzz(i);
};

console.log(output2);