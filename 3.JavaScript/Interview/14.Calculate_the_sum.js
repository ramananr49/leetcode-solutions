const text = "Ja120va10Scr5ipt9"

let sum = 0

let numbers = text.match(/\d+/g)

for (let number of numbers)
{
    sum += parseInt(number)
}

console.log(sum)        //144