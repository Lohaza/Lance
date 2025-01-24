function submit(){
    let search=document.getElementById("input_search").value;
    fetch("http://127.0.0.1:5000/Lance/search",{
        method:"POST",
        body:JSON.stringify({
            search:search
        }),
        headers: {
            'Content-type': 'application/json; charset=UTF-8'
        }
    })
    .then (response=> {
        if (response.ok){
            window.location.href="/Lance/search";
        }else{
            console.log("Error withe the request:", response);
        }

    })
    .catch(error => {
        console.error("Network error:", error)
    });
    
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