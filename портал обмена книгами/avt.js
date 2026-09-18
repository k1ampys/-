document.getElementById('AvtForm').addEventListener('submit',function(event){
    const login_pattern = /^[A-Za-z]+$/;

    const login = document.getElementById('login').value.trim();
    const password = document.getElementById('password').value.trim();

    if(login.length>6){
        if(!login_pattern.test(login)){
            alert('В логине могут использоваться только латинские буквы');
            event.preventDefault();
            return;
        }
    }
    else{
        alert('В логине должно быть более 6 символов');
        event.preventDefault();
        return;
    }

    if(password.length < 6){
        alert('В пароле должно быть более 6 символов');
        event.preventDefault();
        return;
    }

})