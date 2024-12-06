function enter(){
    let name=document.getElementById("username_in").value;
    let pass=document.getElementById("pass_in").value;
    let con_pass=document.getElementById("confirm_pass_in").value;
    let email=document.getElementById("email_in").value;

    let match = pass_check(pass,con_pass);

    if (match===true){
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
        console.log(response)

    })
    reset()
}
}

function reset(){
    document.getElementById("username_in").value="";
    document.getElementById("pass_in").value="";
    document.getElementById("confirm_pass_in").value="";
    document.getElementById("email_in").value="";
}


function pass_check(pass,con_pass){
    if (pass===con_pass){
        return true;
     } else{
        window.alert("passwords do not match")
        return false;
     }
}



