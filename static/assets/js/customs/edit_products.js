const modalBtns = [...document.getElementsByClassName("edit_products")]
const modalEditProductHeader = document.getElementById("product-modal-header")
const input_one = document.getElementById("product-name")
const input_two = document.getElementById("product-quantity")
const input_three = document.getElementById("product-id")
modalBtns.forEach(Btn => Btn.addEventListener("click", () => {
    pk = Btn.getAttribute("data-pk")
    product_name = Btn.getAttribute("data-name")
    quantity = Btn.getAttribute("data-quantity")

    
    input_one.value = product_name
    input_two.value = quantity
    input_three.value = pk
    
    modalEditProductHeader.innerHTML = `
        تغییر ${product_name}
    `



}))