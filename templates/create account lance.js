function enter(){
    let pass=document.getElementById("pass_in").value;
    let con_pass=document.getElementById("confirm_pass_in").value;
    let match=false
    pass_check(pass,con_pass)
    reset()
    Submit(pass,con_pass)
}


function reset(){
    document.getElementById("confirm_pass_in").value="";
    document.getElementById("pass_in").value="";
}


function pass_check(pass,con_pass,){
    if (pass==con_pass){
        console.log("passwords match")
    }
}

function Submit(pass,con_pass){

    let data ={
        "password_id":pass,
        "confirm_password_id":con_pass
    };


    fetch("/submit",{
        method:"POST",
        headers:{
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(Response=> Response.json())
    .then(data=>{
        console.log(data);
        window.alert(data.message)
    })
    .catch(console.error("Error:",error));

}

