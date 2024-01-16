// Private Method


class Person {
    constructor(fname, lname) {
        this.fname = fname
        this.lname = lname
    }
    // Private Method
    #fullName() {
        console.log(this.fname + " " + this.lname)
    }
    display() {
        this.#fullName()
    }
}

var person1 = new Person("Peter", "Griffin")
// person1.fullName() give you an error
person1.display()
