const text = "DddDdiiiIiiIIvVVvvvyYyyYyaAaAaAA"
let final = ""

let group = []

current = text[0]

for (let i=1; i<text.length; i++)
{
    if (text[i].toLowerCase() == current[current.length-1].toLowerCase()) {
        current += text[i]
    }
    else{
        group.push(current)
        current = text[i]
    }
}
group.push(current)

for (let i=0; i<group.length; i++)
{
    final += group[i][i]
}

console.log(final)      //DiVya