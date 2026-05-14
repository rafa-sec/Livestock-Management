const editBtn = document.querySelectorAll(".editBtn")
const editConfirmBtn = document.querySelector(".editConfirmBtn");

const deleteButtons = document.querySelectorAll(".deleteConfirmBtn");


editConfirmBtn.addEventListener("click", function(){
    const confirmed = confirm("Do you really want to edit it?");

    if (!confirmed) {
        event.preventDefault();
    }
})


editBtn.forEach(button => {

    button.addEventListener("click", function (){
        const row = button.closest("tr");

        const form = row.querySelector(".editForm");
        if(form.style.display === "none" || form.style.display === ""){

                form.style.display = "block"

        }else{

            form.style.display = "none"

        }

    })

})


deleteButtons.forEach(button => {

    button.addEventListener("click", function (event) {

        const confirmed = confirm("Do you really want to delete this animal?");

        if (!confirmed) {
            event.preventDefault();
        }

    });

});
