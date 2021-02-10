//1

function array() {
    var output = [];
    for(var i=1; i<256; i++){
        output.push(i);
    }
    return output; 
}
//console.log("number 1 is=" + array(0))

//2
function evennumbers() {
    var sum = 0
    var count = 0
    while(count<=1000){
        if(count % 2 == 0){
            sum = sum + count
        }
        count ++
    }   
    return sum
}
//console.log("number 2 is =" + evennumbers(0));

//3
function oddnumbers(){
    var sum = 0
    var count = 0
    while(count<=5000){
        if(count % 2 == 1){
            sum = sum + count
        }
        count ++
    }
    return sum
}
//console.log("number 3 is =" + oddnumbers(0));

//4

//Create Function that takes in an array
//Create var  called Sum
//use for loop to iterate
// Everytime we iterate we want to add value to 
// return Sum

function sum(arr){
    var sum = 0;
    for(var i = 0; i < arr.length; i++ ){
        sum += arr[i]; //sum += is the same thing as sum = sum + x
    }
    return sum;
}
var array = [1,3,5];
//console.log(sum(array));

//Find max - Given an array with multiple values, write a function that returns the maximum number in the array. (e.g. for [-3,3,5,7] max is 7)
//Create a function that takes in an array
//create a var called max
//create a loop to iterate through the array
//create a conditional that checks the var against the next element in the array
//return max

function getMax(arr){
    var max = arr[0];
    for(var i = 1; i <arr.length; i++){
        if (max < arr[i]){
            max = arr[i]
        }
    }
    return max;
}
var maxarray = [-5, 3,124, -100]
//console.log(getMax(maxarray));

//Find average - Given an array with multiple values, write a function that returns the average of the values in the array. (e.g. for [1,3,5,7,20] average is 7.2)
//create a function that takes in an array
//create a var called average
//create a loop to iterate through the array
//divide sum of array by length of array

function getAvg(arr){
    var total = 0;
    for (var i = 0; i <arr.length; i++){
        total += arr[i]
    }
    var avg = total / arr.length;
    return avg;
}
var arrayavg = [1,2];
//console.log(getAvg(arrayavg));

//Array odd - Write a function that would return an array of all the odd numbers between 1 to 50. (ex. [1,3,5, .... , 47,49]). Hint: Use 'push' method.
//create a function that takes in an array
//create a var called oddArray
//create a loop to iterate through the array
//create a conditional to push a number out of the array if it is odd
function getOdd(arr){
    //var odd = arr;
    for (var i = 0; i <arr.length; i++){
        var odd = arr[i]
        if (odd % 2 == 0){
            arr.push[i]
        }
    }
    return odd;
}
var oddArray = [0,1,2,3,4];
//console.log(getOdd(oddArray));

//Greater than Y - Given value of Y, write a function that takes an array and returns the number of values that are greater than Y. For example if arr = [1, 3, 5, 7] and Y = 3, your function will return 2. (There are two values in the array greater than 3, which are 5, 7).
//create a function that takes in array
//create a var called Y
//create a loop to iterate through the array
//create a conditional to compare Y to the current element in the array
//if y is > than the element, +1 to a count
function getGreater(arr){
    var y = 5
    var count = 0
    for (var i = 0; i<arr.length; i++){
        if (arr[i] > y){
           count += 1;
        }
    }
    return count;
}
var compareArray = [1,3,6,8,9];
//console.log(getGreater(compareArray));

//Squares - Given an array with multiple values, write a function that replaces each value in the array with the value squared by itself. (e.g. [1,5,10,-2] will become [1,25,100,4])
//create a function that takes in array
//create a placeholder array
//create a loop to iterate through the array
//multiply each element in the position by itself
//place that value in the placeholder array

function squares(arr){
    var placeHolder = [];
    var square = 0
    for (i = 0; i<arr.length; i++){
         square = arr[i] * arr[i];
         placeHolder.push(square);
    }
    return placeHolder;
}
var squareArray = [1,2,3];
//console.log(squares(squareArray));

//Negatives - Given an array with multiple values, write a function that replaces any negative numbers within the array with the value of 0. When the program is done the array should contain no negative values. (e.g. [1,5,10,-2] will become [1,5,10,0])
//create function that takes in array
//create a loop to iterate through the array
//create a conditional to compare if the current element is less than 0
//if less than zero, replace it with zero

function negatives(arr){
    for (i = 0; i<arr.length; i++){
        if (arr[i] < 0){
            arr[i] = 0
        }
    }
    return arr;
}
var negativeArray = [-1, -2, 2, 4];
//console.log(negatives(negativeArray));

//Max/Min/Avg - Given an array with multiple values, write a function that returns a new array that only contains the maximum, minimum, and average values of the original array. (e.g. [1,5,10,-2] will return [10,-2,3.5])
//create a function that takes in a array
//create a max, min, avg var
//create a conditional that gives max
//create a conditial that gves min
//create a conditional that gives avg

function minMaxAvg(arr){
    var min = 0;
    var max = 0;
    var avg = 0;
    var total = 0;
    var arrayTotals = [];
    for (i = 0; i<arr.length; i++){
        if (arr[i] > max){
            max = arr[i];
        }
    }
    for (i = 0; i<arr.length; i++){
        if (arr[i] < min){
            min = arr[i];
        }
    }
    for (i = 0; i<arr.length; i++){
        total += arr[i]
    }
    var avg = total / arr.length;
    arrayTotals.push(max,min, avg);//,min,avg);
    return arrayTotals;
}
var bigArray = [0,2,3,1];
console.log(minMaxAvg(bigArray));