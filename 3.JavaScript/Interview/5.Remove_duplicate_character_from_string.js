/*
Write a Program to remove the duplicate character from String of text or word
*/

const text = "Automation"
output = "Automin"

const final = [...new Set(text.toLocaleLowerCase())].join("")
console.log(final)

let seen = ""

for (let c of text.toLocaleLowerCase())
{
    if (!seen.includes(c))
    {
        seen += c
    }

}
console.log(seen)