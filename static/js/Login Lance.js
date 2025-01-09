function enter(){
    let name=document.getElementById("username_in").value;
    let pass=document.getElementById("pass_in").value;


    
    fetch("http://127.0.0.1:5000/Lance/login",{
        method:"POST",
        body: JSON.stringify({
            name:name,
            password:pass,
        }),
        headers: {
            'Content-type': 'application/json; charset=UTF-8'
        }
    })
    .then (response=> {
        if (response.ok){
            window.location.href="/Lance";
        }else{
            response.json().then(data => {
                console.log("Error:", data.error);
                alert(data.error || "An error occurred while logging in.");
        });
    }

    })
    .catch(error => {
        console.error("Network error:", error)
    });

    reset();
}

function logout() {
    fetch("http://127.0.0.1:5000/logout", {
        method: "GET",
        headers: {
            "Content-Type": "application/json"
        }
    })
    .then(response => {
        if (response.ok) {
            window.location.href = "/Lance";
        } else {
            alert("Error logging out.");
        }
    })
    .catch(error => {
        console.error("Error:", error);
    });
}

function reset(){
    document.getElementById("username_in").value="";
    document.getElementById("pass_in").value="";
}
