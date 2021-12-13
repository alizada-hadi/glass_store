const deleteBtns = [...document.getElementsByClassName("delete_products_button")]
const modalDeleteHeader = document.getElementById("product-delete-modal-header")
const input_first = document.getElementById("product-pk")


deleteBtns.forEach(Btn => Btn.addEventListener("click", () => {
    pk = Btn.getAttribute("data-pk")
    pro_name = Btn.getAttribute("data-name")
    input_first.value = pk

    modalDeleteHeader.innerHTML = `
        حذف محصول "${pro_name}" ؟
    `

}))