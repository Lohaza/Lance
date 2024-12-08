function enter(){
    let name=document.getElementById("username_in").value;
    let pass=document.getElementById("pass_in").value;
    let con_pass=document.getElementById("confirm_pass_in").value;
    let email=document.getElementById("email_in").value;


    if (validation(name,pass,con_pass,email)){
    fetch("http://127.0.0.1:5000/Lance/Create_your_account",{
        method:"POST",
        body: JSON.stringify({
            name:name,
            password:pass,
            email:email,
        }),
        headers: {
            'Content-type': 'application/json; charset=UTF-8'
        }
    })
    .then (response=> {
        if (response.ok){
            window.location.href="/user";
        }else{
            console.log("Error withe the request:", response);
        }

    })
    .catch(error => {
        console.error("Network error:", error)
    });

    reset();
}
}

function reset(){
    document.getElementById("username_in").value="";
    document.getElementById("pass_in").value="";
    document.getElementById("confirm_pass_in").value="";
    document.getElementById("email_in").value="";
}


function validation(name,pass,con_pass,email){
    if (name === "" || pass === "" || con_pass === "" || email === "") {
        window.alert("All fields must be filled out!");
        return false;
    }

    if (pass !== con_pass) {
        window.alert("Passwords do not match!");
        return false;
    }

    const emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
    if (!emailPattern.test(email)) {
        window.alert("Please enter a valid email address!");
        return false;
    }

    return true;
}