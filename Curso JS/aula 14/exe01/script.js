function contar(){
    var inicio = window.document.getElementById('txtinicio')
    var fim = window.document.getElementById('txtfim')
    var passo = window.document.getElementById('txtpasso')
    var cont = window.document.getElementById('cont')
    if (inicio.value.length == 0 || fim.value.length == 0 || passo.value.length == 0 ){
           window.alert('ERRO! não pode começar a contagem sem números')  
    }else{
        cont.innerHTML ='Contando: <br>'
        inicio = Number(inicio.value)
        fim = Number(fim.value)
        passo = Number(passo.value)
        if (passo <= 0){
            window.alert('ERRO! O passo não pode ser ZERO ou Menor que ZERO - Considerando passo 1 ' )
            passo = 1
        }
        if (inicio > fim){//CONTAGEM REGRESSIVA
            for (c = inicio; c >= fim; c -= passo)
            cont.innerHTML += ` ${c}\u{1F61C}`
            
        }else{
            (inicio < fim)//CONTAGEM CRESCENTE
           /* for (c = inicio; c <= fim; c += passo){
                cont.innerHTML += `${c}`*/
            var c= inicio
            while(c<= fim){
                    cont.innerHTML += ` ${c}\u{1F61C}`
                c += passo
               
            }
    
        }  
        cont.innerHTML += ` \u{1F3C1}`
    }

}