//Se crea una lista con los botones del html.
const bs = []
for (let i = 0; i < respuestas.length; i++) {
    bs.push(document.getElementById(respuestas[i]))
}
const presult = document.getElementById('result')
var nextButton = document.getElementById('next')

//Funcion que se utiliza cuando el usuario ya selecciono
//una opcion y se eliminen los botones
function destroyButtons(){
    for(let i=0; i < bs.length;i++){
        bs[i].style.display = 'none'
    }
    nextButton.style.display = 'block'
}


function guessed() {
    presult.innerText = `Perfect Dude, it is ${guess}`
    destroyButtons()
}

function failed(i) {
    presult.innerText = `No no dude, it was ${guess}`
    let img = document.getElementById('default')
    console.log(url[i])
    img.setAttribute('src',url[i])
    img.style.display = 'block'
    destroyButtons()
}

//Aqui se le asigna una funcion a cada boton y tipo que este caso son click
for (let i = 0; i < bs.length; i++) {
    if (respuestas[i] == guess) {
        bs[i].addEventListener('click', guessed)
    } else {
        bs[i].addEventListener('click', function(){
            failed(i)
        })
    }
}
