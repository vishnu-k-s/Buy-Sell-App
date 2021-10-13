window.onload = initAll;

var createAccount;

function initAll(){
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
    
    if((username.length)<4){
        document.getElementById('error_message').style.display='block';
        document.getElementById('error_message').innerHTML = "Minimum 4 characters required for username";
        return false;
    }
    if((password.length)<4){
        document.getElementById('error_message').style.display='block';
        document.getElementById('error_message').innerHTML = "Minimum 4 characters required for password";
        return false;
    }

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
