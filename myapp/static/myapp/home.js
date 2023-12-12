function updateName(arg){
    console.log(arg);
        setRequestHeader();
    
        $.ajax({
            dataType: 'json',
            type: 'POST',
            url: "/UpdateGroupName/",
            data: {
                id: arg.id,
                value: arg.value,
            },
            success: function (data) {
                console.log(data);
                
            },
            error: function (jqXHR, textStatus, errorThrown) {
                alert("Error: " + errorThrown);
            }
        });
}

function update(arg,value){
    // console.log(value,arg.parentElement.children[1].value);
    id=arg.parentElement.parentElement.children[0].id;
    setRequestHeader();
    $.ajax({
        dataType: 'json',
        type: 'POST',
        url: "/UpdateScore/",
        data: {
            id: id,
            type: value,
            value: arg.parentElement.children[1].value,
        },
        success: function (data) {
            console.log(arg.parentElement.children[1].value+arg.parentElement.parentElement.children[2].innerHTML);
            if(value=="add"){
            // arg.parentElement.children[1].value;
            arg.parentElement.parentElement.children[2].innerHTML=String(Number(arg.parentElement.parentElement.children[2].innerHTML)+Number(arg.parentElement.children[1].value));
            }else{
                arg.parentElement.parentElement.children[2].innerHTML=String(Number(arg.parentElement.parentElement.children[2].innerHTML)-Number(arg.parentElement.children[1].value));
            }
            
        },
        error: function (jqXHR, textStatus, errorThrown) {
            alert("Error: " + errorThrown);
        }
    });
}