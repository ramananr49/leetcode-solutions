/*
What is a Factorial?
In mathematics, the factorial of a non-negative integer n is the product of all 
positive integers less than or equal to n. It is denoted by n!.
*/

// Using While Loop

function Factorial(num) {
    sum = 1
    while (num>0){
        sum *= num
        num -= 1
    }
    return sum
}

console.log(Factorial(4))       //24
console.log(Factorial(5))       //120
console.log(Factorial(8))       //40320


// Using Recursive 
console.log("*************************************")
function fact(num)
{
    if (num === 0 || num === 1) {
        return 1
    }
    else {
        return num * fact(num-1)
    }
}

console.log(fact(4))       //24
console.log(fact(5))       //120
console.log(fact(8))       //40320