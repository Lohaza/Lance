function submit(event) {
    event.preventDefault();
    let fileInput=document.getElementById("file");
    let manual_name_data=document.getElementById("manual_name_data").value;
    const file = fileInput.files[0];

    if (!file) {
        alert("No file selected.");
        return;
    }

    const formData = new FormData();
    formData.append("file", file, file.name);
    formData.append("manual_name_data", manual_name_data);


    fetch("http://127.0.0.1:5000/Lance/upload_manual_method", {
        method: "POST",
        body: formData,
    })
    .then (response=> {
        if (response.ok){
            console.log("The Manual data has been sent:",);
        }else{
            console.log("Error withe the request:", response);
        }

    })
    .catch(error => {
        console.error("Network error:", error)
    });


    
}