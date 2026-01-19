/*
Write a program to count the occurrences of each character in a string.
*/

const text = "Radar"

let count = {}

for (let c of text.toLocaleLowerCase())
{
  if (!count[c])
    {
        count[c] = 1
    }
    else{
        count[c] += 1
    }  
}

console.log(count)

for (let [k,v] of Object.entries(count))
{
    console.log(k , v)
}