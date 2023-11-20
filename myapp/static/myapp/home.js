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