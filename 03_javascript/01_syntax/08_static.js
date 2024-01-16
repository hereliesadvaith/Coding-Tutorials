// Static Method

class Person {
    constructor(name) {
        this.name = name
    }
    static greet() {
        console.log("Hello")
    }
}

var person1 = new Person("Advaith")
// person1.greet() it will show error. To call static method
Person.greet() // Hello

// To call static method with object

class Developer extends Person {
    static greet(x) {
        super.greet(x)
    }
}

var developer1 = new Developer("Advaith")
Developer.greet(developer1) // Hello
