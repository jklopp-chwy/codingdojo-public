var testArr = [6,3,5,1,2,4];
var x = 0;
var sum = 0;
lengthArr = testArr.length;
while(x < lengthArr){
    sum = (testArr[x]+sum)
    console.log(testArr[x] +" " + sum);    
    x=x+1;
}

var testArr = [6,3,5,1,2,4];
count = testArr.length;
var x = 0;
var position = 0;
var math = 0;
while(x < count){
    math = testArr[position] * x;
    console.log(math);
    position = position + 1;
    x = x + 1;
}