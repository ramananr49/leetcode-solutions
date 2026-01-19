/*
Reverse the Number
*/

let num = 12345

function reverse_num (num)
{
    let temp = 0
    while(num>0)
    {
        let digit = num%10
        temp = (temp * 10) + digit
        num = Math.floor(num/10)
    }
    return temp
}
console.log(reverse_num(num))