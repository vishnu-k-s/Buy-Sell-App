window.onload = initAll;

var loginAccount;

function initAll(){
    loginAccount = document.getElementById('login');
    loginAccount.onclick = login;
}

//Login
function login(){
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;
      
    //alert(email);
    //alert(password);

    var url = '/loginajax/?email='+email+'&password='+password;
    //alert(url);

    var req = new XMLHttpRequest();
    req.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        alert(req.responseText);        
        if(req.responseText == 'Email/Password is invalid'){
            //do nothing
        }
        else{
            window.location.pathname = '/';
        }
    }
    };
 
    req.open("GET", url, true); 
    req.send();        
}