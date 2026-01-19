const text = "R@ma12n6#dg44*";

let alphabet = 0
let number = 0
let spl_char = 0


for (ch of text)
{
    if(/[A-Za-z]/.test(ch))
    {
        alphabet++
    }
    else if (/[0-9]/.test(ch))
    {
        number++
    }
    else {
        spl_char++
    }
}

console.log(`Alphabet count is : ${alphabet}`)
console.log(`Numeric count is : ${number}`)
console.log(`Special Character count is : ${spl_char}`)