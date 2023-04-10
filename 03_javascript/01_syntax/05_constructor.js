// Object
var houseKeeper1 = {
    yearsOfExperience: 12,
    name: "Jane",
    place: "Amsterdam",
};
console.log(houseKeeper1.name);

// Constructor function 
function BellBoy(name, age, hasWorkPermit, languages) {
    this.name = name;
    this.age = age;
    this.hasWorkPermit = hasWorkPermit;
    this.languages = languages;
};

var bellBoy1 = new BellBoy("Timmy", 23, true, ["French", "English", "Spanish"]);
console.log(bellBoy1.name);

// Methods

function Receptionist(name, age) {
    this.name = name;
    this.age = age;
    this.moveSuitcase = function () {
        console.log(`${name}: May I take your suitcase ?`);
    };
};

var receptionist1 = new Receptionist("Niharika", 23);
receptionist1.moveSuitcase();

