/*
#Write a program to reverse the string
*/

let text = "JavaScript"

//Mehtod 1 - using Split(), reverse(), join() method

let rev_text = text.split("").reverse().join("")
console.log(rev_text)

//Method 2 - using the for loop

let rev_text1 = ""

for (let i = text.length -1; i>=0; i--)
{
    rev_text1 += text[i]
}
console.log(rev_text1)

// Mehtod 3 - Using split() and reduce() method

let rev_text2 = text.split("").reduce((acc,c)=>c+acc, "")
console.log(rev_text2)

//reverse the each word in the string

let text1 = "I am Learning JavaScript"

let text_arr = text1.split(" ")
console.log(text_arr)
let rev_arr = []

for (let word of text_arr)
{
    rev_arr.push(word.split("").reverse().join(""))
}
console.log(rev_arr)
console.log(rev_arr.join(" "))

// Using Map 

function reverseEachWord(sen)
{
    return sen.split(" ").map(word => word.split("").reverse().join("")).join(" ")
}

console.log(reverseEachWord(text1))