const cardAnimalsRequiringAttentionBtn = document.getElementById("cardAnimalsRequiringAttention");
const animalsRequiringAttentionList = document.getElementById("animalsRequiringAttentionList")
let clicked = false



cardAnimalsRequiringAttentionBtn.addEventListener("click", function (){
    if(animalsRequiringAttentionList.style.display === "none"){
        animalsRequiringAttentionList.style.display = "block"
    } else {
        animalsRequiringAttentionList.style.display = "none"
    }

    


})

