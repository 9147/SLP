function checkData(){
    usernames=document.getElementById('usernames').value.replaceAll('\n',"").split(',');
    firstName=document.getElementById('firstname').value.replaceAll('\n',"").split(',');
    lastName=document.getElementById('lastname').value.replaceAll('\n',"").split(',');
    email=document.getElementById('emails').value.replaceAll('\n',"").split(',');
    password=document.getElementById('passwords').value.replaceAll('\n',"").split(',');
    len=usernames.length;
    if(len!=firstName.length || len!=lastName.length || len!=email.length || len!=password.length){
        alert('Please enter equal number of data in all fields');
        return false;
    }
    data={}
    for(i=0;i<len;i++){
        data[usernames[i]]={'firstName':firstName[i],'lastName':lastName[i],'email':email[i],'password':password[i]};
    }
    alert(data.toString());
    setRequestHeader();
    $.ajax({
        url: '/updateUsers/',
        type: 'POST',
        data: data,
        success: function (data) {
            alert('Users created successfully');
            window.location.href='/';
        }
    });
}