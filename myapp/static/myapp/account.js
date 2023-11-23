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
            window.location.href='/account';
        },
        error: function (data) {
            alert('Error in resetting game');
        }
    });
}

function ActivateTeams(){
    setRequestHeader();
    $.ajax({
        url: '/activateTeams/',
        type: 'POST',
        success: function (data) {
            alert('Teams activated successfully');
            window.location.href='/account';
        },
        error: function (data) {
            alert('Error in activating teams');
        }
    });
}

function ClearTeams(){
    setRequestHeader();
    $.ajax({
        url: '/clearTeams/',
        type: 'POST',
        success: function (data) {
            alert('Teams cleared successfully');
            window.location.href='/account';
        },
        error: function (data) {
            alert('Error in clearing teams');
        }
    });
}