import json
import jieba
import numpy as np
import tensorflow.keras as keras
from keras.models import load_model
import os

cur_path = os.getcwd()
print(cur_path)
with open(cur_path + "/project_linebot/tokenizer.json",encoding="utf-8") as jsonFile:
    tokenizer = json.load(jsonFile)
    jsonFile.close()

model_GRU_ONLY = load_model(cur_path + '/project_linebot/models/model_GRU_ONLY.h5')
model_Bi_LSTM = load_model(cur_path + '/project_linebot/models/model_Bi_LSTM.h5')
model_LSTM_ONLY = load_model(cur_path + '/project_linebot/models/model_LSTM_ONLY.h5')

def token_padding(inputs):
    inputs = jieba.cut(str(inputs))
    text_tmp = []
    for word in inputs:
        if word == '!' or word == '《' or word == '》' or word == '\xa0' or word == ' ' or word == '\n' or word == '/n' or word == '(' or word == ')' or word == '『' or word == '』' or word == '...' or word == '（' or word == '）' or word == '：' or word == '?' or word == '？' or word == '！' or word == '\u3000' or word == '】' or word == '【' or word == '」' or word == '「' or word == '，' or word == '、' or word == '╱' or word == '。' or word == '；' or word == '·' or word == '..' or word == '．' or word == '.' or word == ',' or word == '～' or word == '“' or word == '”' or word == '/' or word == '㈠' or word == '㈡' or word == '／':  
            word = ''
        else:
            text_tmp.append(word)
    trantotoken = []
    for input in text_tmp:
        if input in tokenizer:
            trantotoken.append(tokenizer[input])
        else:
            trantotoken.append(0)
    return predictions([trantotoken])

def predictions(trantotoken):
    print(trantotoken)
    prediction_GRU = np.argmax(model_GRU_ONLY.predict(trantotoken),axis=1)[0]
    prediction_BiLSTM = np.argmax(model_Bi_LSTM.predict(trantotoken),axis=1)[0]
    prediction_LSTM = np.argmax(model_LSTM_ONLY.predict(trantotoken),axis=1)[0]
    print(prediction_GRU, prediction_BiLSTM, prediction_LSTM)
    return prediction_GRU, prediction_LSTM, prediction_BiLSTM