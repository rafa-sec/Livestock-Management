const editBtn = document.querySelector(".editBtn")
const editForm = document.querySelector(".editForm");
const editConfirmBtn = document.querySelector(".editConfirmBtn");

const deleteConfirmBtn = document.querySelector(".deleteConfirmBtn");

editConfirmBtn.addEventListener("click", function(){
    confirm("Do you really want to edit it?")
})

editBtn.addEventListener("click", function (){
    editForm.style.display = "block"
})

deleteConfirmBtn.addEventListener("click", function (){
    confirm("Do you really want to delete this animal?")
})