document.getElementById('AdminForm').addEventListener('submit',function(event){
    event.preventDefault();
    const login = document.getElementById('login').value.trim();
    const password = document.getElementById('password').value.trim();

    if(login!='admin'){
        alert('Неверный логин');
        return;
    }

    if(password!='bookworm'){
        alert('Неверный пароль');
        return;
    }
    if(login === 'admin'){
        if(password === 'bookworm'){
            document.getElementById('AdminForm').style.display = 'none';
            document.getElementById('AdminForm').style.backgroundColor = ' ';
            document.getElementById('WatchCard').style.display = 'block';

            return;
        }
    }
    

})

document.getElementById('formCard1').addEventListener('submit',function(event){
    event.preventDefault();
    document.getElementById('Publish1').style.display = 'none';
    document.getElementById('Publish1').style.backgroundColor = ' ';
    document.getElementById('otcaz1').style.display = 'block';
})
document.getElementById('formCard2').addEventListener('submit',function(event){
    event.preventDefault();
    document.getElementById('Publish2').style.display = 'none';
    document.getElementById('Publish2').style.backgroundColor = ' ';
    document.getElementById('otcaz2').style.display = 'block';
})
document.getElementById('formCard3').addEventListener('submit',function(event){
    event.preventDefault();
    document.getElementById('Publish3').style.display = 'none';
    document.getElementById('Publish3').style.backgroundColor = ' ';
    document.getElementById('otcaz3').style.display = 'block';
})