var username = "{{ username }}"; 
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

    let fileInput=document.getElementById("file");
    const file = fileInput.files[0];

    if (!file) {
        alert("No file selected.");
        return;
    }
    const reader = new FileReader();
    reader.onload = function(e) {
        const img = new Image();
        img.onload = function() {
            const maxWidth = 100;  
            const maxHeight = 100; 

            let width = img.width;
            let height = img.height;

            if (width > height) {
                if (width > maxWidth) {
                    height = Math.round((maxWidth / width) * height);
                    width = maxWidth;
                }
            } else {
                if (height > maxHeight) {
                    width = Math.round((maxHeight / height) * width);
                    height = maxHeight;
                }
            }

            
            const canvas = document.createElement("canvas");
            const ctx = canvas.getContext("2d");
            canvas.width = width;
            canvas.height = height;
            ctx.drawImage(img, 0, 0, width, height);

            canvas.toBlob(function(blob) {

                const formData = new FormData();
                formData.append("file", blob, file.name); 




            fetch("http://127.0.0.1:5000/Lance/upload_profile_image", {
                method: "POST",
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.message) {
                    window.relodad()
                } else {
                    alert(data.error);
                }
            })
            .catch(error => {
                console.error("Error:", error);
                alert("Error uploading image.");
            });
        }, 'image/jpeg', 0.9); 
    };
    img.src = e.target.result;  
    };

    reader.readAsDataURL(file);
    }

