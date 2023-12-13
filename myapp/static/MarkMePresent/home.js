function validateForm() {
    console.log("login");
    var username = document.getElementById("email").value;
    var password = document.getElementById("name").value;
    var data = {
        email: username,
        password: password,
    };
    // console.log(data);

    setRequestHeader();

    $.ajax({
        dataType: 'json',
        type: 'POST',
        url: "/MarkMePresent/data/",
        data: data,
        success: function (data) {
            // console.log("Success:", data);
            if(data==404){
                alert("User not found");
            }else{
            alert("Successfully Marked Present");
        window.location.href="/";}
            // window.location.href = "../";
        },
        error: function (jqXHR, textStatus, errorThrown) {
            alert("error");

        }
    });

    return false;
  }