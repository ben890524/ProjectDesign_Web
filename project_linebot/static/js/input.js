$('#input_button').click(function(event){
    event.preventDefault();
    input_text = $('#input_text').val();
    clearInput();
    process_input(event, input_text);
    $('#loading').addClass("active");
})
function process_input(event, input_text) {
    $.ajax({
        url: "index",
        type: "POST",
        data: {
            input: input_text,
            csrfmiddlewaretoken: $('[name="csrfmiddlewaretoken"]').val()
        },
        success: function (data) {
            $('#loading').removeClass("active");
            console.log(data);
            if(data["input_text"] != "error"){
                $('#showing_result').addClass("active");
                $('#showing_background').addClass("active");
                setTimeout(function(){ 
                    $('#result_content').addClass("active");
                    $('#show_input').text(data["input_text"]);
                    if(data["gru_prediction"] == "0"){
                        $('#show_gru').text("正確");
                    }else{
                        $('#show_gru').text("錯誤");
                    }
                    if(data["lstm_prediction"] == "0"){
                        $('#show_lstm').text("正確");
                    }else{
                        $('#show_lstm').text("錯誤");
                    }
                    if(data["bilstm_prediction"] == "0"){
                        $('#show_bilstm').text("正確");
                    }else{
                        $('#show_bilstm').text("錯誤");
                    }   
                }, 1000); 
            }else{
                console.log("error")
            }
        },
        error: function (xhr, errmsg, err) {
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
}

function clearInput(){
    document.querySelector("#input_text").value = "";
}

function closeResult(){
    $('#showing_result').removeClass("active");
    $('#showing_background').removeClass("active");
    $('#result_content').removeClass("active");          
}