class Person {
    constructor(name) {
        this.name = name
    }
    greet() {
        console.log("Hey " + this.name)
    }
}

var person1 = new Person("Lilly")
person1.greet() // Hey Lilly

class Developer extends Person {
    constructor(name, role) {
        super(name)
        this.role = role
    }
    greet() {
        console.log("Hi " + this.role + " " + this.name)
    }
}

var developer1 = new Developer("Advaith", "Python Developer")
developer1.greet() // Hi Python Developer Advaith
