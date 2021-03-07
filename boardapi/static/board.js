var BaseURL = ''
window.onload=function getLoginUser(){
    var getRequest = new XMLHttpRequest()
    getRequest.open('GET',BaseURL + '/username')
    getRequest.send()
    getRequest.onreadystatechange = function() {
        if(getRequest.readyState == 4){
            if(getRequest.status == 200){
                var x= getRequest.response;
                var y= eval("("+x+")");
                document.getElementById("username").innerHTML=y["username"];
            }
            else{
                console.log(getRequest.responseText)
            }
        }
    }
}
function getAll(){
    var getRequest = new XMLHttpRequest()
    getRequest.open('GET',BaseURL + '/boards/all')
    getRequest.send()
    getRequest.onreadystatechange = function() {
        if(getRequest.readyState == 4){
            if(getRequest.status == 200){
                var x = getRequest.response;
                var comments = eval("("+x+")");
                document.getElementsByTagName('ul')[0].innerHTML = ""
                document.getElementById("alert").innerHTML=""
                var ul = "";
                for (var i=0 ; i < x.length ; i++ ){
                    var id = ls[i]["id"];
                    var nickname = ls[i]["nickname"];
                    var text = ls[i]["text"];
                    var date = ls[i]["date"];
                    var last = ls[i]["last"];
                    var username =ls[i]["username"];
                    ul += '<li class="item">';
                    ul += '     <div class="info">';
                    if (username==document.getElementById("username").value){
                    ul += '         <div class="id">'+id+'</div>';
                    }
                    else{
                    ul += '         <div class="id" style="display:none">'+id+'</div>';
                    }
                    ul += '         <div class="nickname">'+nickname+'</div>';
                    ul += '         <div class="date">'+date+'</div>';
                    ul += '         <fieldset class="text">'+text+'</fieldset>';
                    ul += '         <div class="last">'+last+'</div>';
                    ul += '     </div>'
                    ul += '</li>'
                }
                document.getElementById("UL").innerHTML= ul ;    
            }
        }
    }
}
getAll()
function postComment(){
    var postRequest = new XMLHttpRequest()
    postRequest.open("POST",BaseURL+'/board/add')
    var postData = {
        username:document.getElementById("username").value,
        text:document.getElementById("commentArea").value
    }
    postRequest.setRequestHeader("Content-type","application/json")
    postRequest.send(JSON.stringify(postData))
    postRequest.onreadystatechange=function(){
        if(postRequest.readyState == 4){
            if(postRequest.status == 200){
                var x= postRequest.response;
                var y= eval("("+x+")");
                console.log(y["message"])
                document.getElementById("alert").innerHTML=""
                document.getElementById("commentArea").innerHTML=""
                getAll()
            }
            else{
                document.getElementById("alert").innerHTML=postRequest.responseText
            }
        }
    }
}
getAll()
function edit_text(){
    var putRequest = new XMLHttpRequest()
    putRequest.open('PUT',BaseURL + '/board/modification')
    var putData = {
        id:document.getElementById("id").value,
        text: document.getElementById("edit").value
    }
    putRequest.setRequestHeader("Content-type","application/json")
    putRequest.send(JSON.stringify(putData))
    putRequest.onreadystatechange = function(){
        if (putData.readyState == 4){
            if (putData.status == 200){
                var x = putRequest.response;
                var y = eval("("+x+")");
                console.log(y["message"])
                document.getElementById("alert").innerHTML=""
                document.getElementById("id").innerHTML=''
                document.getElementById("edit").innerHTML=''
                getAll()
            }
            else{
                document.getElementById("alert").innerHTML=putRequest.responseText
            }
        }
    }
}
getAll()
function erase() {
    var postRequest = new XMLHttpRequest()
    postRequest.open('POST',BaseURL + '/board/deletion')
    var postData = {
        id:document.getElementById("id").value
    }
    postRequest.setRequestHeader("Content-type","application/json")
    postRequest.send(JSON.stringify(postData))
    postRequest.onreadystatechange = function(){
        if (postData.readyState == 4){
            if (postData.status == 200){
                var x = postRequest.response;
                var y = eval("("+x+")");
                console.log(y["message"])
                document.getElementById("alert").innerHTML=""
                getAll()
            }
            else{
                document.getElementById("alert").innerHTML=postRequest.responseText
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
                console.log(postRequest.responseText)
                document.getElementById("alert").innerHTML=""
                window.location.href="/"
            } else { 
                document.getElementById("alert").innerHTML=postRequest.responseText
        }
      }
   }
}