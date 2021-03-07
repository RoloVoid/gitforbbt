function getAll(){
    var BaseURL = ''
    var getRequest = new XMLHttpRequest()
    getRequest.open('GET',BaseURL + '/boards/all')
    getRequest.send()
    getRequest.onreadystatechange = function() {
        if(getRequest.readyState == 4){
            if(getRequest.status == 200){
                let obj = JSON.parse(getRequest.responseText) ;
                // console.log(obj)
                let boards = obj.boards ;
                document.getElementsByClassName('board')[0].innerHTML = ""
                for (var i=0 ; i < boards.length ; i++ ){
                    var nickname = boards[i].nickname;
                    var date = boards[i].date;
                    var text = boards[i].text;
                    var last = boards[i].last;
                    var a = document.createElement("div");
                    var a1 = document.createElement("div");
                    a1.innerText = nickname ;
                    a1.className = "nickname";
                    a.appendChild(a1);
                    var a2 = document.createElement("div");
                    a2.innerText = date ;
                    a2.className = "date";
                    a.appendChild(a2);
                    var a3 = document.createElement("div");
                    a3.innerText = text ;
                    a3.className = "text";
                    a3.style['overflow']='auto';
                    a.appendChild(a3);
                    var a4 = document.createElement("div");
                    a4.innerText = last ;
                    a4.className = "last";
                    a.appendChild(a4);
                    document.getElementsByClassName("board")[0].appendChild(a);
                } 
            }
        }
    }
}
getAll()