/*
Write a program to find the second largest number in a list.
*/

const a_list = [12, 35, 1, 10, 34, 1];
console.log(a_list)
let unique_list = [...new Set(a_list)];
console.log(unique_list)
let sorted_unique_list = unique_list.sort((a,b) => b-a)
console.log(sorted_unique_list)
console.log(sorted_unique_list[1])

/*
Write a program to find the second largest number in a list.
*/

const arr = [ 12, 35, 1, 10, 34, 1 ]
let largest = -Infinity
let seconglargest = -Infinity

for (let num of arr)
{
    if (num > largest)
    {
        seconglargest = largest
        largest = num
    }
    else if (num > seconglargest && num < largest)
    {
        seconglargest = num
    }
}

console.log(`The Second Largest Number from array is ${seconglargest}`)