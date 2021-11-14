import json
from django.conf import settings
from django.shortcuts import *
from django.views import View
from django.http.response import JsonResponse
import concurrent.futures
from project_linebot.tokenizer_predictions import *
# Create your views here.
class Index(View):
    template_name = "Index.html"

    def get(self, request):
        return render(request,
                      self.template_name)

    def post(self, request):
        input_text = request.POST.dict()

        if input_text is not None:
            if input_text["input"] != "":
                print(input_text)
                return_value = ""
                gru_prediction = ""
                lstm_prediction = ""
                bilstm_prediction = ""
                prediction = ""
                with concurrent.futures.ThreadPoolExecutor() as executor:
                    future = executor.submit(token_padding, input_text["input"])
                    return_value = future.result()
                for index, result in enumerate(return_value):
                    if index == 0:
                        gru_prediction = str(result)
                    elif index == 1:
                        lstm_prediction = str(result)
                    else:
                        bilstm_prediction = str(result)
                return JsonResponse({'input_text': input_text["input"], 'gru_prediction': gru_prediction, 'lstm_prediction': lstm_prediction, 'bilstm_prediction': bilstm_prediction})

        return JsonResponse({'input_text':  'error'})