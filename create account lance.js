
function enter(){
    let pass=document.getElementById("pass_in").value;
    let con_pass=document.getElementById("confirm_pass_in").value;
    hash_pass=stringToHash(pass)
    hash_con_pass=stringToHash(con_pass)
    pass_check(hash_pass,hash_con_pass)
    console.log(hash_pass)
    console.log(hash_con_pass)
    reset()
}


function reset(){
    document.getElementById("confirm_pass_in").value="";
    document.getElementById("pass_in").value="";
}

function stringToHash(string) {
    let hash = 0;
    if (string.length == 0) return hash;
    for (i = 0; i < string.length; i++) {
        char = string.charCodeAt(i);
        hash = ((hash << 5) - hash) + char;
        hash = hash & hash;
    }
    return hash;
}

function pass_check(hash_pass,hash_con_pass){
if (hash_pass==hash_con_pass){
    console.log("passwords match")
}

}

function topython(usrdata){
    $.ajax({
        url: "fill url here",
        type: "POST",
        data: { information : "You have a very nice website, sir." , userdata : usrdata },
        dataType: "json",
        success: function(data) {
            <!-- do something here -->
            $('#somediv').html(data);
        }});
$("#someButton").bind('click', toPython(something));
}