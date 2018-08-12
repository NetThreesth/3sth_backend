import time, random
import requests
from threading import Thread
from dbMgr import dbMgr

class deepAIThread(Thread):
    def probUp(self, rId):
        if (rId >= 0 and rId < len(self._probList)):
            self._probList[rId] = 0.6;

    def __init__(self):
        self._probList = [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3]
        Thread.__init__(self)

    def run(self):
        url = "http://35.229.249.165/apis/uploadDeepAlMessage"
        while(True):
            db = dbMgr()
            time.sleep(10 * 60)
            for rId in range(0, 9):
                val = random.random()
                if val < self._probList[rId]:
                    result = self.getDeepMsg(db, rId)
                    d = {"rid":rId, "message":result}
                    requests.post(url, json=d) 
            del db             
            
    def getDeepMsg(self, db, roomId):
        max = db.getDeepAiMessageMax(roomId)
        min = db.getDeepAiMessageMin(roomId)

        result = ''.join(random.sample(max + min, len(max) + len(min)))
        return result
        
