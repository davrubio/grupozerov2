

let totalAmount = document.querySelectorAll(".totalAmount");
let amountByItem = document.querySelectorAll("input[name=totalTxtPrice]");
let totalItem = document.querySelectorAll(".totalQuantity");
let itemCountByEachProd = document.querySelectorAll("input[name=item]")
console.log(totalAmount)
console.log(amountByItem)
console.log(totalItem)
console.log(itemCountByEachProd)

document.querySelectorAll(".bi-cart-plus-fill").forEach(item => {
    item.addEventListener("click", function () {
        console.log('item 1ro', item)
        addItemToCart(item);
    })
    // console.log(item)
})

function addItemToCart(item) {
    console.log('acá empieza item ', item)
    let valor = document.getElementById('txtPriceId').value
    console.log('valor ',valor)
    // let closetTr = item.closest("td").parentNode;
    // let closestPrice = closetTr.cells[2].querySelector("input[name=txtPrice]");
    // let closestTotalPrice = closetTr.cells[2].querySelector("input[totalTxtPrice]");
    let total = document.getElementById('totalTxtPrice').value
    console.log('totalTxtPrice ', totalTxtPrice)
    let itemCount = item.closest("td").querySelector("input[name=item]").value;
    console.log('itemCount ', parseFloat(itemCount))
    itemCount = parseFloat(itemCount) + 1;
    console.log('itemCount + 1', parseFloat(itemCount))
    closestTotalPrice = parseFloat(valor) * parseFloat(itemCount)
    // closestTotalPrice = parseFloat(closestPrice) * parseFloat(itemCount.value)
    console.log('* ', closestTotalPrice)
    // console.log('closestPrice ', closestPrice)
    total = closestTotalPrice
    amountByItem.forEach(item => {
        // tempTotalAmount = tempTotalAmount + (closestTotalPrice)
        // console.log('tempTotalAmount ', tempTotalAmount)
        // console.log('item.value ', item.value)
    })
    totalAmount.forEach(item => {
        // item.innerHTML = tempTotalAmount
        // console.log('item ', item)
        // console.log('item.innerHTML ', item.innerHTML)
    })

}