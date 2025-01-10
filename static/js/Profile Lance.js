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
    // Create a FileReader to read the image file
    const reader = new FileReader();
    reader.onload = function(e) {
        const img = new Image();
        img.onload = function() {
            // Set the new size of the image
            const maxWidth = 200;  // Desired max width (in pixels)
            const maxHeight = 200; // Desired max height (in pixels)

            let width = img.width;
            let height = img.height;

            // Resize the image while maintaining aspect ratio
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

            // Create a canvas to draw the resized image
            const canvas = document.createElement("canvas");
            const ctx = canvas.getContext("2d");
            canvas.width = width;
            canvas.height = height;
            ctx.drawImage(img, 0, 0, width, height);

            // Convert the canvas to a Blob (JPEG/PNG)
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
                    window.location.reload();  // Reload the page to show updated image
                } else {
                    alert(data.error);
                }
            })
            .catch(error => {
                console.error("Error:", error);
                alert("Error uploading image.");
            });
        }, 'image/jpeg', 0.9);  // Compress the image to JPEG format with 90% quality
    };
    img.src = e.target.result;  // Load the image data from the FileReader
    };

    // Read the file as a Data URL (base64 string)
    reader.readAsDataURL(file);
    }

