/*
#Write a program to check if two strings are anagrams.
*/

let s1 = "listen"
let s2 = "silent"

let s3 = "rail"
let s4 = "liar"

let s5 = "hello"
let s6 = "world"

function is_Anagram(s1, s2)
{
    s1 = s1.split("").sort().join("")
    s2 = s2.split("").sort().join("")
    return s1 === s2
}

console.log(`The word "${s1}" and "${s2}" are anagram : ${is_Anagram(s1,s2)}`)
console.log(`The word "${s3}" and "${s4}" are anagram : ${is_Anagram(s3,s4)}`)
console.log(`The word "${s5}" and "${s6}" are anagram : ${is_Anagram(s5,s6)}`)