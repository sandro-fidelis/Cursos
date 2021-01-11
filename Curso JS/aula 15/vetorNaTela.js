var valores  = [3, 2 ,5 ,9 ,8, 7]

console.log(valores)// mostra os valores das variáveis
/*
for (var pos=0; pos < valores.length; pos ++){
    console.log(`A posição ${pos} tem o valor ${valores[pos]}`)
    // mostra as posições e valores de cada variável
}*/

for(var pos in valores){
    console.log(`Aposição ${pos} tem o valor ${valores[pos]}`)
//forma simplificada de mostrar as posções e valores da cada variável
}