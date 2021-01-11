
    var num = window.document.getElementById('txtnum')// seleciona o valor digitado e coloca na variável "num"
    var lista = window.document.getElementById('lista')// seleciona o valor digitado e coloca na variável "lista"
    var res = window.document.getElementById('res') 
    var valores = []// vetor

/*function isNumero(n){
    if(Number(n) >=1 && Number(n) <= 100){
    return true
    }else{
        return false
    }
}

function inLista(n,l){
    if(l.indexOf(Number(n))!= -1){
    return true
}else{
    return false
}
}
function adiciona(){
    if(isNumero(num.value) && !inLista(num.value, valores)){
        valores.push(Number(num.value))
        var item = document.createElement('option')
        item.text =`Valor ${num.value} adicionado`
        lista.appendChild(item)
        res.innerHTML = ''
    }else{
        window.alert('ERRO! Valor inválido ou já incluso na lista')
      }
      num.value = ''
      num.focus()
}
function finalizar(){
    if (valores.lenght == 0){
        window.alert('ERRO! Necessário digitar valores antes de finalizar')
    }else{
        var tot = valores.length
        var maior = valores[0]
        var menor = valores[0]
        var soma = 0
        var media = 0
        for(var pos in valores){
            soma += valores[pos]
            if(valores[pos] > maior)
            maior = valores[pos]
            if(valores[pos] < menor)
            menor = valores[pos]
        }
        media = soma / tot
        res.innerHTML = ''
        res.innerHTML += `<p>Ao todo, temos ${tot}, números cadastrados.</p>`
        res.innerHTML += `<p>O maior valor informado foi ${maior}.</p>`
        res.innerHTML += `<p>O menor valor informado foi ${menor}.</p>`
        res.innerHTML += `<p>Somando todos os valores, temos ${soma}.</p>`
        res.innerHTML += `<p>A média dos valores digitados é: ${media}.</p>`
    }
}*/



function adiciona(){
    if (num.value.length == 0){
        window.alert('ERRO! Impossível começar sem valores')
    }else if
        (num.value== 0){
        window.alert('ERRO! O valor não pode ser "0" ZERO')
        }else if
            (Number(num.value) > 100){
        window.alert("ERRO! O valor tem que ser entre 1 e 100")   
            }
            if
            (num.value != valores){
            (valores.push(Number(num.value)))
             var item = document.createElement('option')
             item.text =`Valor ${num.value} adicionado`
             lista.appendChild(item)
             num.value = ''
             num.focus()

            }else{
                window.alert('ERRO')
            }


}