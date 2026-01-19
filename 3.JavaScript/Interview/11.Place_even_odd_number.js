/*
Write a program to place even number in even index and odd number in odd index
*/
let arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

let n = arr.length

let even_arr = []
let odd_arr = []

for (let i=0; i<arr.length; i++)
{
    if (arr[i]%2 === 0)
    {
        even_arr.push(arr[i])
    } else {
        odd_arr.push(arr[i])
    }
}
console.log(even_arr)
console.log(odd_arr)

for (let j=0; j<arr.length; j++) {
    if (j%2 == 0)
    {
        arr[j] = even_arr.shift()
    }
    else {
        arr[j] = odd_arr.shift()
    }
}
console.log(arr)