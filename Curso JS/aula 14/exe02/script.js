function calcular(){
    var num = window.document.getElementById('txtnum')// seleciona o valor de "txtnum" 
    var tab = window.document.getElementById('seltab')// seleciona o valor da seleção "seltab"
    if (num.value.length == 0){//testa se a variável está vazia, antes de iniciar o programa
        window.alert("ERRO! Impossível calcular sem valor")
    }else{ 
    num = Number(num.value)// converte o que foi digitado para número
    tab.innerHTML = ""// Limpa a tabuada
    c = 1// inicio do contador
    while (c <= 10){
        var item = document.createElement('option') // criação de um novo elemento
        item.text = `${num} X ${c} = ${num*c}`// escrever na tela o calculo
        item.value = `tab${c}`// valor de "option" não tem muita influencia no javascript
        tab.appendChild(item)// "tab" adiciona oe elementos de "item" 
        c++ // incremento da condição "while"
      }
    } 
}