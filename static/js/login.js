
const loginBtn = document.getElementById("loginBtn")

loginBtn.addEventListener("click", function(){
    const password = document.getElementById("password").value
    const username = document.getElementById("username").value

    if(password === "admin" && username === "admin"){
        alert("Admin logged")
        window.location = "dashboard.html"
    }else if(password === "worker" && username === "worker"){
        alert("Worker logged")
    }
})