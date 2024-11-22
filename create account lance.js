function enter(){
    let pass=document.getElementById("pass_in").value;
    console.log(pass);
    let con_pass=document.getElementById("confirm_pass_in").value;
    console.log(con_pass);
    pass_check(con_pass,pass)
    reset()
}


function reset(){
    document.getElementById("confirm_pass_in").value="";
    document.getElementById("pass_in").value="";
}
    

function pass_check(con_pass,pass){
if (pass==con_pass){
    console.log("passwords match")
}

}