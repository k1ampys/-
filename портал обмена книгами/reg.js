document.getElementById('RegistrationForm').addEventListener('submit',function(event){
    const login_pattern = /^[A-Za-z]+$/;
    const fio_pattern = /^[А-ЯЁ][а-яё]+ [А-ЯЁ][а-яё]+ [А-ЯЁ][а-яё]+$/;
    const phone_pattern = /^(\+7|8)\d(9)$/;

    const login = document.getElementById('login').value.trim();
    const password = document.getElementById('password').value.trim();
    const fio = document.getElementById('fio').value.trim();
    const phone = document.getElementById('phone').value.trim();

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

    if(!fio_pattern.test(fio)){
        alert('Неверно введено ФИО');
        event.preventDefault();
        return;
    }
    if(!phone_pattern.test(phone)){
        alert('Неверно введён телефон');
        event.preventDefault();
        return;
    }
})

