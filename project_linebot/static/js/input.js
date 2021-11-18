$('#input_button').click(function (event) {
    event.preventDefault();
    input_text = $('#input_text').val();
    clearInput();
    if (input_text === "") {
        alert("請輸入訊息");
    } else {
        process_input(event, input_text);
        $('#loading').addClass("active");
    }
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
            var result_a = document.querySelectorAll('.result a');
            result_a.forEach(element => {
                element.classList.remove("active");
            })
            if (data["input_text"] != "error") {
                $('#showing_result').addClass("active");
                $('#showing_background').addClass("active");
                setTimeout(function () {
                    $('#result_content').addClass("active");
                    $('#show_input').text(data["input_text"]);
                    if (data["gru_prediction"] == "0") {
                        $('#show_gru').text("正確");
                    } else {
                        $('#show_gru').text("錯誤");
                    }
                    if (data["lstm_prediction"] == "0") {
                        $('#show_lstm').text("正確");
                    } else {
                        $('#show_lstm').text("錯誤");
                    }
                    if (data["bilstm_prediction"] == "0") {
                        $('#show_bilstm').text("正確");
                    } else {
                        $('#show_bilstm').text("錯誤");
                    }
                    var i = 0;
                    while (i < result_a.length) {
                        const item = data["google_scraper_content"][i];
                        if (item === undefined && i == 0) {
                            $('#ref').text("暫時無參考資料");
                            i = 5;
                        } else
                        if (item === undefined) {
                            i = 5;
                        } else {
                            console.log(i, item);
                            result_a[i].textContent = item[0];
                            result_a[i].classList.add("active");
                            result_a[i].attributes.href.value = item[1];
                        }
                        i++;
                    }
                }, 1000);
            } else {
                console.log("error")
            }
        },
        error: function (xhr, errmsg, err) {
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
}

function clearInput() {
    document.querySelector("#input_text").value = "";
}

function closeResult() {
    $('#showing_result').removeClass("active");
    $('#showing_background').removeClass("active");
    $('#result_content').removeClass("active");
    $('#ref').text("參考資料：");
}
