var BaseURL = ''
window.onload=function getLoginUser(){
    var getRequest = new XMLHttpRequest()
    getRequest.open('GET',BaseURL + '/username')
    getRequest.send()
    getRequest.onreadystatechange = function() {
        if(getRequest.readyState == 4){
            if(getRequest.status == 200){
                var x= getRequest.responseText;
                var y= eval("("+x+")");
                document.getElementById("username").innerHTML=y["username"];
            }
            else{
                console.log(getRequest.responseText)
            }
        }
    }
}
function getInfo(){
    var getRequest = new XMLHttpRequest()
    getRequest.open('GET',BaseURL + "/userinfo")
    getRequest.send()
    getRequest.onreadystatechange = function(){
        if(getRequest.readyState ==4 ) {
            if(getRequest.status == 200 ) {
                var x = getRequest.responseText;
                var y = eval("("+x+")");
                var username = y["username"];
                var nickname = y["nickname"];
                var age = y["age"];
                var gender = y["date"];
                document.getElementById("alert").innerHTML=""
                document.getElementById("username0").innerHTML=username;
                document.getElementById("nickname").innerHTML=nickname;
                document.getElementById("age").innerHTML=age;
                document.getElementById("gender").innerHTML=gender;
            }
            else{
                var x = getRequest.responseText;
                var y = eval("("+x+")");
                console.log(y["message"]);
                document.getElementById("alert").innerHTML=y["message"];
            }
        }
    }
}
getInfo()
function change(){
    var postRequest = new XMLHttpRequest()
    postRequest.open('POST',BaseURL + '/userinfo/modification')
    // postRequest.send()
    var obj = document.getElementById("gender1");
    var index =obj.selectedIndex;
    var postData = {
        nickname: document.getElementById("nickname1").value,
        age: document.getElementById("age1").value,
        gender: obj.options[index].value,
        password: document.getElementById("password1").value
    }
    postRequest.setRequestHeader("Content-type","application/json")
    postRequest.send(JSON.stringify(postData))
    postRequest.onreadystatechange = function(){
        if (postRequest.readyState ==4){
            if(postRequest.status == 200){
                var x = postRequest.responseText;
                var y = eval("("+x+")");
                console.log(y["message"]);
                document.getElementById("alert").innerHTML="";
                document.getElementById("username0").innerHTML="";
                document.getElementById("nickname").innerHTML="";
                document.getElementById("age").innerHTML="";
                document.getElementById("gender").innerHTML="";
                cancel()
                getInfo()
            }
            else{
                var x = postRequest.responseText;
                var y = eval("("+x+")");
                console.log(y["message"]);
                document.getElementById("alert").innerHTML=y["message"];
            }
        }
    }
}
function logout(){
    var postRequest = new XMLHttpRequest()
    postRequest.open("POST", BaseURL + '/userinfo/logout') 
    var postData = {
         username: document.getElementById("username").value
    }
    postRequest.setRequestHeader("Content-type", "application/json")
    postRequest.send(JSON.stringify(postData))
    postRequest.onreadystatechange = function() {
        if (postRequest.readyState == 4) {
            if (postRequest.status == 200) { 
                var x = postRequest.responseText;
                var y = eval("("+x+")");
                console.log(y["message"]);
                document.getElementById("alert").innerHTML="";
                window.location.href="session";
            } else { 
                var x = postRequest.responseText;
                var y = eval("("+x+")");
                console.log(y["message"]);
            }
      }
   }
}
function edit(){
    var a=document.getElementById("box");
    a.setAttribute("style","display:block");
    var b=document.getElementById("change-box");
    b.setAttribute("style","display:none");
}
function cancel(){
    var a=document.getElementById("box");
    a.setAttribute("style","display:none");
    var b=document.getElementById("change-box");
    b.setAttribute("style","display:block");
}