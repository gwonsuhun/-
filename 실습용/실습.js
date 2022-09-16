function printHello() {
    console.log("hello");
}
printHello();

function log(message) {
    console.log(message);
}
log("hello@");
log("안녕하세요")


function changeName(obj) {
    obj.name = "coder";
}

const ellie = {name : "ellie"};
changeName(ellie);
console.log(ellie);

function showMessage(name, message = "입력하지않았습니다"){
    console.log(name,message);
}

showMessage("hi");

function printAll(...args) {
    for (let i = 0; i < args.length; i++) {
        console.log(args[i]);
    }
}

printAll('dream',"coding","ellie");

function randomQuiz (answer, printYes, printNo) {
    if (answer === "love ya") {
        printYes();
    }else {
        printNo();
    }
}

const printYes = function() {
    console.log("Yes");
};

const printNo = function print() {
    console.log("no");
};

randomQuiz("love ya", printYes,printNo);
randomQuiz("-____-",printYes,printNo);

class person {
    constructor(name,age) {
        this.name = name;
        this.age = age;
    }
    speak() {
        console.log(`${this.name} : hello!`);
    }
}

const ellie_1 = new person('ellie',20);
console.log(ellie_1.name);
console.log(ellie_1.age);
ellie_1.speak();