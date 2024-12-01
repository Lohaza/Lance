function enter(){
    let pass=document.getElementById("pass_in").value;
    let con_pass=document.getElementById("confirm_pass_in").value;
    let match=false
    pass_check(pass,con_pass)
    Submit(pass,con_pass)
    reset()
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


