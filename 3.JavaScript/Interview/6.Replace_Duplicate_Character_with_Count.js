/*
Write a Program to Replace the Duplicate Character with its count
*/

const text = "Automation"
output = "2u22m22i2n"

let text_obj = {}

for (ch of text.toLowerCase())
{
    if(!text_obj[ch])
    {
        text_obj[ch] = 1
    }
    else
    {
        text_obj[ch] += 1
    }
}
temp = ""
for (let ch of text.toLowerCase())
{
    if (text_obj[ch]>1)
    {
        temp += text_obj[ch]
    } else {
        temp += ch
    }
}
console.log(temp)       //2u22m22i2n