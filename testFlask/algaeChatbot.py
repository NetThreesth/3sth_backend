
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

class algaeChatbot:
    def __init__(self, rid):
        charbotId = "chatbot" + str(rid)
        charbotDB = "chatbotDB/" + charbotId + "_DB.db"

        self.chatbot = ChatBot("testBot",
            storage_adapter="chatterbot.storage.SQLStorageAdapter",
            database=charbotDB)
        self.chatbot.set_trainer(ChatterBotCorpusTrainer)
        
    def getResponse(self, msg=""):
        return self.chatbot.get_response(msg)