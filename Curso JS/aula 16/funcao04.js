// fatorial de um número
// 5! = 5 x 4 x 3 x 2 x 1 = 120
function fatorial(n){
    var fat = 1
    for(var c = n; c > 1; c--){
        fat *= c
    }
    return fat
} 

console.log(fatorial(5))
