var BaseURL = ''
function postUser(){
    var postRequest = new XMLHttpRequest()
    postRequest.open('POST',BaseURL+'/session')
    var postData ={
        username: document.getElementById("username").value,
        password: document.getElementById("password").value
    }
    postRequest.setRequestHeader("Content-type","application/json")
    postRequest.send(JSON.stringify(postData))
    postRequest.onreadychange = function(){
        if (postRequest.readyState == 4){
            if (postRequest.status ==200) {
                var x= postRequest.responseText;
                var y= eval("("+x+")");
                console.log(y["message"]);
                document.getElementById("alert").innerHTML="";
                window.location.href="board";
            } else {
                var x= postRequest.responseText;
                var y= eval("("+x+")");
                console.log(y["message"]);
                document.getElementById("alert").innerHTML=y["message"];
            }
        }
    }
}
function postNewUser(){
    var postRequest = new XMLHttpRequest()
    postRequest.open("POST",BaseURL + '/register')
    var postData = {
        username: document.getElementById("username").value ,
        password: document.getElementById("password").value
    }
    postRequest.setRequestHeader("Content-type","application/json")
    postRequest.send(JSON.stringify(postData))
    postRequest.onreadystatechange = function(){
        if (postRequest.readyState ==4) {
            if (postRequest.status == 200) {
                var x= postRequest.responseText;
                var y= eval("("+x+")");
                console.log(y["message"])
                document.getElementById("alert").innerHTML=""
                window.location.href="/session"
            } else {
                var x= postRequest.responseText;
                var y= eval("("+x+")");
                console.log(y["message"]);
                document.getElementById("alert").innerHTML=y["message"];
            }
        }
    }
}