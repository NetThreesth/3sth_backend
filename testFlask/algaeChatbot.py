#!/usr/bin/python
# -*- coding: UTF-8 -*-
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import random
class algaeChatbot:
    def __init__(self, rid):
        charbotId = "chatbot" + str(rid)
        charbotDB = "chatbotDB/" + charbotId + "_DB.db"

        self.chatbot = ChatBot(charbotId,
            storage_adapter="chatterbot.storage.SQLStorageAdapter",
            database=charbotDB)
        self.chatbot.set_trainer(ChatterBotCorpusTrainer)
        
        #self.chatbot.train(
        #    "./training_corpus/0624_corpus.yml",
        #    "./training_corpus/0808_corpus.yml"
        #    )
        
    def getResponse(self, msg=""):
        if self.checkSpecial(msg):
            return '3sth.net以當代三體共構之文化脈絡為討論主軸，以藻類(自然)、使用者(人類)與人工智慧(科技)為符碼，探討三者交互作用如何交織出文化織體，以及此間的運作方式'
        elif self.checkEnglish(msg):
            if(random.randint(0, 10)> 5):
                return '不好意思，我外語能力不太好耶！'
            else:
                return '可不可以說中文呀？'            
        else:
            return self.chatbot.get_response(msg).text

    def checkSpecial(self, msg):
        return (msg == '3sth.net');

    def checkEnglish(self, msg):
        count = 0
        for var in msg:
            if (var >= 'A' and var <= 'Z') or (var >= 'a' and var <= 'z'):
                count += 1
        
        return (len(msg) * 0.5 < count);