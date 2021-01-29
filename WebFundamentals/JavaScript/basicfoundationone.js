//1

function array() {
    var output = [];
    for(var i=1; i<256; i++){
        output.push(i);
    }
    return output; 
}
console.log("number 1 is=" + array(0))

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
console.log("number 2 is =" + evennumbers(0));

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
console.log("number 3 is =" + oddnumbers(0));

//4
