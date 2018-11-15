import time, random
import requests
from threading import Thread
from dbMgr import dbMgr

class deepAIMgr():
    def probUp(self, rId):
        if (rId >= 0 and rId < len(self._probList)):
            self._probList[rId] = 0.6;

    def __init__(self):
        self._probList = [0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6]
        self._countList = [10, 10, 10, 10, 10, 10, 10, 10, 10]


    def countDeep(self, roomId):
        self._countList[roomId] -= 1
        if(self._countList[roomId] == 0):
            url = "https://3sth.net/apis/uploadDeepAlMessage"
            db = dbMgr()
            val = random.random()
            if val < self._probList[roomId]:
                result = self.getDeepMsg(db, roomId)
                d = {"rid":roomId, "message":result}
                requests.post(url, json=d) 
            del db
            self._countList[roomId] = 10

    def getDeepMsg(self, db, roomId):
        max = db.getDeepAiMessageMax(roomId)
        min = db.getDeepAiMessageMin(roomId)

        result = ''.join(random.sample(max + min, len(max) + len(min)))
        return result
        
