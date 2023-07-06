

function test(){
    let titulo = document.getElementById('titulo')
}
function test22(pokeTitulo, pokeArtista,pokeDescripcion,pokePrecio,pokeAnno_creacion,pokeImagen){
    // let test = document.querySelector("input[id=labelFoto]");
    let titulo = document.getElementById('titulo')
    let artista = document.getElementById('artista')
    let descripcion = document.getElementById('descripcion')
    let precio = document.getElementById('precio')
    let anno_creacion = document.getElementById('anno_creacion')
    let imagen = document.getElementById('imagen')
    console.log(imagen)

    titulo.value = pokeTitulo.value
    artista.value = pokeArtista.value
    descripcion.value = pokeDescripcion.value
    precio.value = pokePrecio.value * 100
    // anno_creacion.value = pokeAnno_creacion.value
    anno_creacion.value = datetime.datetime.now()  
    imagen.value = pokeImagen.value

    console.log(titulo)
}

