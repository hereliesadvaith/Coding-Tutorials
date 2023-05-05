var randomNumber1 = Math.floor(Math.random() * 6) + 1;
var randomDiceImage = "dice" + randomNumber1 + ".png";
var randomDiceImageSource = "images/" + randomDiceImage;
// changing the img source
document.querySelectorAll("img")[0].setAttribute("src", randomDiceImageSource);

var randomNumber2 = Math.floor(Math.random() * 6) + 1;
randomDiceImage = "dice" + randomNumber2 + ".png";
randomDiceImageSource = "images/" + randomDiceImage;
document.querySelectorAll("img")[1].setAttribute("src", randomDiceImageSource);

if (randomNumber1 > randomNumber2) {
  document.querySelector("h1").innerHTML = "Player 1 Wins";
} else if (randomNumber1 === randomNumber2) {
  document.querySelector("h1").innerHTML = "Draw";
} else {
  document.querySelector("h1").innerHTML = "Player 2 Wins";
};


