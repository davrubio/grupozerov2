console.log('CARRO 2 IS WORKING')

const clickButton = document.querySelectorAll('.button')
const tbody = document.querySelector('.tbody')
let carrito = []

console.log('clickButton ', clickButton)


clickButton.forEach(btn => {
    btn.addEventListener('click', addToCarritoItem)
})

function addToCarritoItem(e) {
    const button = e.target
    const item = button.closest('.test2')
    console.log(item)
    const itemId = item.querySelector('.id').textContent;
    const itemArtista = item.querySelector('.artista').textContent;
    const itemTitle = item.querySelector('.title').textContent;
    const itemPrice = item.querySelector('.precio').textContent;
    const itemImg = item.querySelector('.img').src;
    const newCarrito = {
        id_cuadro: itemId,
        titulo: itemTitle,
        artista: itemArtista,
        precio: itemPrice,
        url: itemImg,
        cantidad: 1
    }
    addItemCarrito(newCarrito)

    console.log('newCarrito ', newCarrito)
}

function addItemCarrito(newCarrito) {
    const inputElemento = tbody.getElementsByClassName('input__elemento')
    for (let i = 0; i < carrito.length; i++) {
        if (carrito[i].titulo.trim() === newCarrito.titulo.trim()) {
            carrito[i].cantidad++;
            const inputValue = inputElemento[i]
            inputValue.value++;
            carritoTotal()
            return null
        }
    }
    carrito.push(newCarrito)
    renderCarrito()
}

function renderCarrito() {
    tbody.innerHTML = ''
    carrito.map(item => {
        const div = document.createElement('div')
        div.classList.add('ItemCarrito')
        div.classList.add('d-flex')
        div.classList.add('align-items-center')
        div.classList.add('mb-5')
        const content =
            `
            <div class="flex-shrink-0">
                                                <img src=${item.url} class="img-fluid" style="width: 150px;"
                                                    alt="Generic placeholder image">
                                            </div>
                                            <div class="flex-grow-1 ms-3">
                                                <a href="#!" class="float-end text-black"><i
                                                        class="fas fa-times"></i></a>
                                                <h5 class="title text-primary">${item.titulo}</h5>
                                                <h6 style="color: #9e9e9e;">${item.artista}</h6>
                                                <div class="d-flex align-items-center">
                                                    <p class="fw-bold mb-0 me-5 pe-3">$${item.precio}</p>
                                                    <div class="def-number-input number-input safari_only">
                                                        <button
                                                            onclick="this.parentNode.querySelector('input[type=number]').stepDown()"
                                                            class="minus"></button>
                                                        <input class="quantity input__elemento fw-bold text-black"
                                                            min="0" name="quantity" value=${item.cantidad}
                                                            type="number">
                                                        <button
                                                            onclick="this.parentNode.querySelector('input[type=number]').stepUp()"
                                                            class="plus"></button>
                                                        <span class="delete btn btn-danger">X</span>
                                                    </div>
                                                </div>
                                            </div>

        `
        div.innerHTML = content
        tbody.append(div)

        div.querySelector(".delete").addEventListener('click', removeItemCarrito)
        div.querySelector(".input__elemento").addEventListener('change', sumar)
    })
    carritoTotal()
    console.log('carrito ', carrito)
}

function carritoTotal() {
    let total = 0;
    const itemCartTotal = document.querySelector('.itemCartTotal')
    carrito.forEach((item) => {
        const precio = Number(item.precio)
        total = total + precio * item.cantidad
    })

    itemCartTotal.innerHTML =
        `
           $${total}
        `

}

function removeItemCarrito(e) {
    const buttonDelete = e.target;
    const tr = buttonDelete.closest(".ItemCarrito")
    const titulo = tr.querySelector('.title').textContent;
    for (let i = 0; i < carrito.length; i++) {
        if (carrito[i].titulo.trim() === titulo.trim()) {
            carrito.splice(i, 1)
            console.log('AHHHHHHHHHH')
        }
    }
    tr.remove()
    carritoTotal()
}

function sumar(e) {
    const sumaInput = e.target
    const tr = sumaInput.closest(".ItemCarrito")
    const title = tr.querySelector('.title').textContent;
    carrito.forEach(item => {
        if (item.titulo.trim() === title) {
            sumaInput.value < 1 ? (sumaInput.value = 1) : sumaInput.value;
            item.cantidad = sumaInput.value;
            carritoTotal()
        }
    })
    console.log(carrito);
}

$("#montoConv").inputmask({
    mask: "$[999.999.999]"
});