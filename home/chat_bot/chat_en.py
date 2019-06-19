# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.decorators import csrf

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

import time
from gtts import gTTS
import os

class Chat:
    def __init__(self):
        cb = ChatBot('mybot')
        trainer = ChatterBotCorpusTrainer(cb)
        trainer.train("chatterbot.corpus.english")

    def chat(self, request):
        ctx ={}
        if request.POST:
            rep = str(cb.get_response(request.POST['q']))
            tts = gTTS(text = rep, lang = 'en')
            time_now = time.asctime(time.localtime(time.time()))
            filename = 'Response on ' + time_now + '.mp3'
            tts.save(filename)
            os.system("mpg321 " + filename)
            ctx['rlt'] = 'Response on ' + time_now + ' : ' + request.POST['q']
        return render(request, "chat.html", ctx)

# 接收POST请求数据
# def search_post(request):
#     ctx ={}
#     if request.POST:
#         ctx['rlt'] = request.POST['q']
#     return HttpResponse("Go Advance")
