window.onload = initAll;

var createAccount;
var loginAccount;

function initAll(){
    alert('hi');
    loginAccount = document.getElementById('login');
    loginAccount.onclick = login;

    createAccount = document.getElementById('create');
    createAccount.onclick = saveAccount;  

    
    
}

//Registration
function saveAccount(){
    var username = document.getElementById('username').value;
    var name = document.getElementById('name').value;
    var email = document.getElementById('email').value;
    var phone = document.getElementById('phone').value;
    var password = document.getElementById('password').value;
    
    //alert(username);
    //alert(name);
    //alert(email);
    //alert(phone);
    //alert(password);

    var url = '/createAccount/?username='+username+'&name='+name+'&email='+email+'&phone='+phone+'&password='+password;
    //alert(url);

    var req = new XMLHttpRequest();
    req.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        alert(req.responseText);
    }
    };
 
    req.open("GET", url, true); 
    req.send();        
}

//Login
function login(){
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;
      
    alert(email);
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