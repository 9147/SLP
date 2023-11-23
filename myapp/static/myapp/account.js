function openBlock(){
    document.getElementById('block').style.display='flex';
}
function closeBlock(){
    document.getElementById('block').style.display='none';
}
function validateForm(){
    // alert($('passward').val(),$('passward2').val());
    if(document.getElementById('password').value.length<4){
        alert("passwords must be atleast of 4 characters");
        return false;
    }
    else if(document.getElementById('password').value!==document.getElementById('password2').value){
        alert("passwords don't match");
        return false;
    }
    
}
function ResetGame(){
    setRequestHeader();
    $.ajax({
        url: '/resetGame/',
        type: 'POST',
        success: function (data) {
            alert('Game reset successfully');
            window.location.href='/';
        },
        error: function (data) {
            alert('Error in resetting game');
        }
    });
}