var n = Math.random();
console.log(n);
console.log(Math.floor(n));
// we can scale it up
n = Math.floor(n * 6);
// now we get numbers 0 to 5, add 1 to get numbers 1 to 6
n++
console.log(n);

// control statements
if (n === 6) {
    console.log("highscore");
} else {
    console.log("could be better");
};
/*
=== is equal to
!== not equal to
>= greater than equal to
<= less than equal to
== same as 3 equal sign but doesn't give a shit about datatype
&& And
|| Or
! Not
*/
if (n > 2) {
    console.log("Greater than ONE")
} else if (n < 2) {
    console.log("Less than 3")
} else {
    console.log("Equals to 2")
};