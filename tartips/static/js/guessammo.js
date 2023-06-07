const bs = []
for (let i = 0; i < respuestas.length; i++) {
    bs.push(document.getElementById(respuestas[i]))
}
const presult = document.getElementById('result')

function guessed() {
    presult.innerText = `Perfect Dude, it is ${guess}`
}
function failed(i) {
    presult.innerText = `No no dude, it was ${guess}`
    var img = document.getElementById('default')
    console.log(url[i])
    img.setAttribute('src',url[i])
    img.style.display = 'block'
}
for (let i = 0; i < bs.length; i++) {
    if (respuestas[i] == guess) {
        bs[i].addEventListener('click', guessed)
    } else {
        bs[i].addEventListener('click', function(){
            failed(i)
        })
    }
}
