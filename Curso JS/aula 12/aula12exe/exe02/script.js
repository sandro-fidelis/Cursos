
function carregar(){
    var msg = window.document.getElementById('msg')
    var img = window.document.getElementById('imagem')
    var msg2 = window.document.getElementById('msg2')
    var data = new Date()
   // var hora = data.getHours()
   var hora = 20
    msg.innerHTML = `Agora são ${hora} horas.`
    if(hora >= 0 && hora <12){
        //BOM DIA!
        img.src = 'fotomanha.png'
        msg2.innerHTML += `<p>Bom dia!</p>`
        document.body.style.background = '#ff990e'
    }   else if (hora >=12 && hora < 18){
        //BOA TARDE!
        img.src = 'fototarde.png'
        msg2.innerHTML =`<p>Boa Tarde!</p>`
        document.body.style.background = '#fddc14'
    }else{
        //BOA NOITE
        img.src = 'fotonoite.png'
        msg2.innerHTML = `<p>Boa Noite!</p>`
        document.body.style.background = '#475057'
    }
}