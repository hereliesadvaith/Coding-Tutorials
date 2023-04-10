function greeter() {
    console.log("Hi there,");
    console.log("Hope you are doing fine");
};
greeter();

function spGreeter(name) {
    console.log("Hey " + name);
};
spGreeter("Advaith");

// Life in weeks
function lifeInWeeks(age) {
    var yearsRemaining = 72 - age;
    return ((yearsRemaining * 52) + " weeks remaining in your life");
};
console.log(lifeInWeeks(24));

// BMI
function bmiCalc(w, h) {
    return Math.round(w / Math.pow(h, 2));
};
console.log(bmiCalc(65, 1.76));

/* Leap year 
Every year that is evenly divisible by 4
Except every year that is evenly divisible by 100
Unless the year is also evenly divisible by 400
*/
function isLeapYear(year) {
    if ((year % 4) === 0) {
        if ((year % 100) === 0) {
            if ((year % 400) === 0) {
                return true;
            } else {
                return false;
            };
        } else {
            return true;
        };
    } else {
        return false;
    };
};
console.log(isLeapYear(2003));

// fibonacciGenerator

function fibonacciGenerator(n) {
    var output = [];
    if (n === 1) {
        output.push(0);
    } else if (n === 2) {
        output.push(0);
        output.push(1);
    } else {
        a = n - 2;
        output.push(0);
        output.push(1);
        for (i = 1; i <= a; i++) {
            output[i + 1] = output[i] + output[i - 1];
        }
    };
    console.log(output);
};
fibonacciGenerator(10);