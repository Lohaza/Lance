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

function submit(event) {
    event.preventDefault();

    const formData = new FormData(this);
    
    fetch("http://127.0.0.1:5000/Lance/upload_profile_image", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.message) {
            alert(data.message);
            window.location.reload();  // Reload the page to show updated image
        } else {
            alert(data.error);
        }
    })
    .catch(error => {
        console.error("Error:", error);
        alert("Error uploading image.");
    });
};