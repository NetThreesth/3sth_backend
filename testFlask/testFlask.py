#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json, math, random, time
from threading import Thread

from flask import Flask, request, render_template
from config import DevConfig
from algaeChatbot import algaeChatbot
from segment import segment
from sentenceGenerator import sentenceGenerator
from algae import algaeATT
from deepAI import deepAIThread
from dbMgr import dbMgr

app = Flask(__name__)
app.config.from_object(DevConfig)

@app.route('/3sth/api/v1.0/chatbots/', methods=['POST'])
def talk():
    msg = ""
    roomId = 0
    if(request.is_json):
        data = request.get_json(force=True)
        msg = data['msg']
        roomId = int(data['rid'])
    else:
        msg = request.form['msg']
        roomId = int(request.form['rid'])
    segment = seg.splitMsg(msg)
    sentenceMgr[roomId].updateWord(segment)
    algaeResponse = sentenceMgr[roomId].getSentence(255, 255)
    t2c = text2cmd(msg)
    
    db = dbMgr()
    db.addMessage(int(roomId), msg, t2c['score']) 
    del db

    deepAI.probUp(roomId)

    algaeDeviceList[roomId].addAlageData(t2c['pumpValue'], t2c['ledValue'])
    data = algaeDeviceList[roomId].getAlgaeData()

    resp = {
        "active":"chatbots",
        "roomId":str(roomId),
        "inputMsg":msg,
        "chatbotResponse":botList[roomId].getResponse(msg),
        "algaeResponse":algaeResponse,
        "chatbot2algaeResponse":botList[roomId].getResponse(algaeResponse),
        "text2cmd":t2c,
        "pump":data.pump,
        "led":data.led,  
        "density":data.density,
        "color":data.color
    }
    return json.dumps(resp, ensure_ascii=False)

@app.route('/3sth/api/v1.0/userdata/', methods=['POST'])
def userdata():
    if(request.is_json):
        data = request.get_json(force=True)
        touch = int(data['touch'])
        time = int(data['time'])
        roomId = int(data['rid'])
    else:
        touch = int(request.form['touch'])
        time = int(request.form['time'])
        roomId = int(request.form['rid'])
    pumpValue = getPumpBase(touch)
    ledValue = getLedBase(time)

    algaeDeviceList[roomId].updateBaseline(pumpValue, ledValue)
    resp = {
        "active":"userdata",
        "baseline_pump":pumpValue,
        "baseline_led":ledValue,
    }
    return json.dumps(resp, ensure_ascii=False)

@app.route('/3sth/api/v1.0/getTodayMsg/', methods=['GET'])
def getTodayMsg():
    db = dbMgr()
    msg = db.getTodayMessage()
    resp = {
        "active":"getTodayMsg",
        "msg":msg
    }
    del db
    return json.dumps(resp, ensure_ascii=False)

@app.route('/3sth/api/v1.0/uploadPattern/', methods=['POST'])
def uploadPattern():
    pattern = request.form['pattern']
    db = dbMgr()
    db.addMetaAIPattern(pattern)
    resp = {
        "active":"uploadPattern"
    }
    del db
    return json.dumps(resp, ensure_ascii=False)

@app.route('/3sth/api/v1.0/getAlgaeData/', methods=['POST'])
def getAlgaeData():
    roomId = int(request.form['rid'])
    data = algaeDeviceList[roomId].getAlgaeData()
    resp = {
        "active":"getAlgaeData",
        "pump":data.pump,
        "led":data.led,
        "density":data.density,
        "color":data.color
    }
    return json.dumps(resp, ensure_ascii=False)

@app.route('/3sth/api/v1.0/getDeepAIMsg/', methods=['POST'])
def getDeepAIMsg():
    roomId = request.form['rid']
    db = dbMgr()
    result = deepAI.getDeepMsg(db, int(roomId))
    resp = {
        "active":"getDeepAIMsg",
        "roomId":roomId,
        "deepAiMsg":result
    }
    del db
    return json.dumps(resp, ensure_ascii=False)

@app.route('/3sth/api/v1.0/chatbotTest/', methods=['POST'])
def chatbotTest():
    msg = ""
    msg = request.form['msg']
    botList[0].getResponse(msg)
    resp = {
        "active":"chatbotTest",
        "msg":botList[0].getResponse(msg)
    }
    return json.dumps(resp, ensure_ascii=False)

@app.route('/test', methods=['GET'])
def test():
    #return render_template('test.html')
    return render_template('testLocal.html')

##Method
def text2cmd(msg):
    ledV = 0
    pumpV = 0
    idx = 0
    score = 0
    haveGrass = False
    for var in msg:
        code = var.encode('utf-8')
        v = getUTF8CodeValue(code)
        haveGrass &= checkGrass(v)
        if ledV == 0:
            pumpV = ledV = v
        else:
            if(idx % 2 == 0):
                pumpV -= v
                ledV += v
            else:
                pumpV += v
                ledV -= v
        idx += 1

    base = 1
    if(haveGrass):
        base = 2

    score = min(2147483646, base * int(math.sqrt(abs(ledV * pumpV))))
    if(ledV * pumpV < 0):
        score = -score

    if ledV > 0:
        ledV %= 5
    else:
        ledV = -(abs(ledV) % 5)

    if pumpV > 0:
        pumpV %= 5
    else:
        pumpV = -(abs(pumpV) % 5)
    result = {
        "ledValue":ledV,
        "pumpValue":pumpV,
        "score":score
    }
    return result

def getUTF8CodeValue(code):
    p = len(code) - 1
    v = 0
    for codeVal in code:
        v += codeVal << (8 * p)
        p -= 1
    return v


def checkGrass(code):
    if(code >= 15239609 and code <= 15243660):
        return True
    else:
        return False

def getLedBase(time):
    ledValue = 0
    if(time <= 90):
        ledValue = (time - 1) * 2 + 20
    elif(time > 90 and time <= 120):
        ledValue = 208
    elif(time > 120 and time <= 240):
        ledValue = 218
    elif(time > 240 and time <= 360):
        ledValue = 228
    elif(time > 360 and time <= 480):
        ledValue = 238
    elif(time > 480 and time <= 600):
        ledValue = 248
    else:
        ledValue = 255

    return ledValue 

def getPumpBase(touch):
    pumpValue = touch / 50.0 + 20
    return min(255, pumpValue)

##Main Loop
def mainLoop():
    while(True):
        time.sleep(30)
        for rid in range(0, 9):
            algaeDeviceList[rid].checkTimer(30)

if __name__ == '__main__':
    
    #algae chatbot
    botList = []
    for id in range(0, 9):
        botList.append(algaeChatbot(id))

    #segment
    seg = segment()

    #database
    dbMgr.initConnect("35.236.188.139", "root", "threesththreesththreesth", "threesth")
    db = dbMgr()
    data = db.getTodayMessage()
    del db

    #deepAI
    deepAI = deepAIThread()
    deepAI.setDaemon(True)
    deepAI.start()

    #sentaence
    sentenceMgr = []
    for id in range(0, 9):
        sentenceMgr.append(sentenceGenerator(id))

    #algae
    algaeDeviceList = []
    algaeDeviceList.append(algaeATT('muCg1jZhIZY6s961aJ03rcxk', '4LpvkqOyciVeG0lqFyC6yXg4gvel80JLErW6hK70'))
    algaeDeviceList.append(algaeATT('1yIBQapqIvJmKpAEX2IJKgc5', '4O8qd506sCJMW1VeVvE41lqDtwntCIz2YZsuALS'))
    algaeDeviceList.append(algaeATT('xlvfKg52QzsAmJn7XSVqBvSF', '4PwZsM3RGJzuG0lqFzagjYK8CgDnIdpanumy2PJ1'))
    algaeDeviceList.append(algaeATT('q35bNns5XPEqJ5DbgwvsRW3Z', '4UzyyY2mPXm1i0ByXzX1LF5QyCjwD1KTl58BSr8A'))
    algaeDeviceList.append(algaeATT('XNQ90OLBUmEzHZh0Iv8rC64r', '4JovjWsPB5kfW1VeVnTQWPHUB7Si8qDwUwAAyeE'))
    algaeDeviceList.append(algaeATT('4qcN9roOwWQHHYwKEPJrlbpf', '4NKhlbNfSs5qW1VeVzQz7VQSyS45L17EnqiSFzo2'))
    algaeDeviceList.append(algaeATT('O4xQniLbfzOWRxJC2UyP4q50', '4QKgrGvpJOobW1VeVq8gmj9S5M4KJqhMwUrDKy8'))
    algaeDeviceList.append(algaeATT('QLyIkkOBVvieLmVYsBNjL2M4', '4NnFth5L5d0aW1VeVyYynXw2dJGu71ID5sQngmb'))
    algaeDeviceList.append(algaeATT('sJFbVrGQKSahaUsKW3CisEHh', '4Smr2oddHVhUW1VeVvw4J7KVnqezCGYgFiuXso6'))
    time.sleep(3)
    for id in range(0, 9):
        algaeDeviceList[id].getAlgaeData()

    #loop
    loop = Thread(target = mainLoop)
    loop.setDaemon(True)
    loop.start()

    app.run("0.0.0.0", use_reloader=False)
    #app.run(use_reloader=False);
