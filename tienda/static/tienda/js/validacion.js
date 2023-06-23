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

    let closetTr = item.closest("td").parentNode;
    let closestPrice = closetTr.cells[2].querySelector("input[name=txtPrice]").value;
    let closestTotalPrice = closetTr.cells[2].querySelector("input[totalTxtPrice]");

    let itemCount = item.closest("td").querySelector("input[name=item]");
    // console.log(itemCount.value)
    // console.log(closestPrice)

    itemCount.value = parseFloat(itemCount.value) + 1;
    closestTotalPrice = parseFloat(closestPrice) * parseFloat(itemCount.value)
    // console.log('*', closestTotalPrice)
    // console.log(closeTr)
    let tempTotalAmount = 0;
    amountByItem.forEach(item => {
        tempTotalAmount = tempTotalAmount + parseFloat(closestTotalPrice)
        console.log('tempTotalAmount ', tempTotalAmount)
        console.log('item.value ', item.value)
    })
    totalAmount.forEach(item => {
        item.innerHTML = tempTotalAmount
        console.log('item ', item)
        console.log('item.innerHTML ', item.innerHTML)
    })

}