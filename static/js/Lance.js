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

function search_page(){
    fetch("http://127.0.0.1:5000/Lance", {
        method: "GET",
        headers: {
            "Content-Type": "application/json"
        }
    })
    .then(response => {
        if (response.ok) {
            window.location.href = "/Lance/search";
        } else {
            alert("Error search page unable to load.");
        }
    })
    .catch(error => {
        console.error("Error:", error);
    });
}
