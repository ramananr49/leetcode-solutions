/*
#write a program to check the given string is Palindrome
*/

const str = "madam"
const str1 = "test"
const str2 = "Radar"

function is_Palindrome(word) {
    rev_word = word.split("").reverse().join("")
    return rev_word.toLowerCase() === word.toLowerCase()
}

console.log(`The word ${str} is Palindrome word : ${is_Palindrome(str)}`)
console.log(`The word ${str1} is Palindrome word : ${is_Palindrome(str1)}`)
console.log(`The word ${str2} is Palindrome word : ${is_Palindrome(str2)}`)