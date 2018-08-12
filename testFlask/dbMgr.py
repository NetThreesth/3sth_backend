import pymysql

class dbMgr:
    _host = ""
    _user = ""
    _pw = ""
    _db = ""
    _isInit = False
    _conn = None

    @staticmethod
    def initConnect(host, user, pw, db):
        dbMgr._host = host
        dbMgr._user = user
        dbMgr._pw = pw
        dbMgr._db = db
        dbMgr._isInit = True

    def addMessage(self, roomId, msg, score):
        
        if dbMgr._isInit == False:
            return ""
        sql = 'INSERT INTO threesth.deepailog(message, score, chatroomId) VALUES("%s", %d, %d)'
        sql = sql % (msg, score, roomId)
        
        cursor = self._conn.cursor()
        try:
            #print("SQL:" + sql)
            cursor.execute(sql)
            self._conn.commit()
        except:
            print("[addmessage]ERROR")
            self._conn.rollback()
        cursor.close()

    def getDeepAiMessageMax(self, roomId):
        if dbMgr._isInit == False:
            return ""
        deepAiMsg = ""
        sql = "SELECT message FROM threesth.deepailog WHERE chatroomId = %d ORDER BY score DESC LIMIT 1"
        cursor = self._conn.cursor()
        try:
            cursor.execute(sql % roomId)
            self._conn.commit()
            
            result = cursor.fetchall()
            for row in result:
                deepAiMsg = row[0]
        except:
            self._conn.rollback()
            
        cursor.close()
        return deepAiMsg

    def getDeepAiMessageMin(self, roomId):
        if dbMgr._isInit == False:
            return ""
        deepAiMsg = ""
        sql = "SELECT message FROM threesth.deepailog WHERE chatroomId = %d ORDER BY score ASC LIMIT 1"
        cursor = self._conn.cursor()
        try:
            cursor.execute(sql % roomId)
            self._conn.commit()
            
            result = cursor.fetchall()
            for row in result:
                deepAiMsg = row[0]
        except:
            self._conn.rollback()
            
        cursor.close()
        return deepAiMsg

    def __init__(self):
        if dbMgr._isInit:
            self._conn = pymysql.connect(dbMgr._host, dbMgr._user, dbMgr._pw, dbMgr._db)
        

    def __del__(self):
        self._conn.close()

        
        