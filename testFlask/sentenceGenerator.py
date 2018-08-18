# -*- coding: UTF-8 -*-

from wordMgr import wordMgr
from enum import Enum
import random

class eWordType(Enum):
    eNoun = 0
    eVerb = 1
    eSubject = 2
    eAdjust = 3
    eQuestion = 4

class sentenceRule:
    def __init__(self):
        self.sRule = []

class sentenceGenerator:
    

    def __initSentenceMgr(self):
        rule1 = sentenceRule()
        rule1.sRule.append(eWordType.eSubject)
        rule1.sRule.append(eWordType.eVerb)
        rule1.sRule.append(eWordType.eNoun)

        rule2 = sentenceRule()
        rule2.sRule.append(eWordType.eAdjust)
        rule2.sRule.append(eWordType.eNoun)
        rule2.sRule.append(eWordType.eVerb)
        rule2.sRule.append(eWordType.eSubject)

        rule3 = sentenceRule()
        rule3.sRule.append(eWordType.eSubject)
        rule3.sRule.append(eWordType.eAdjust)
        rule3.sRule.append(eWordType.eNoun)

        rule4 = sentenceRule()
        rule4.sRule.append(eWordType.eSubject)
        rule4.sRule.append(eWordType.eVerb)
        rule4.sRule.append(eWordType.eQuestion)

        rule5 = sentenceRule()
        rule5.sRule.append(eWordType.eNoun)
        rule5.sRule.append(eWordType.eVerb)
        rule5.sRule.append(eWordType.eQuestion)

        self._sentenceMgr.append(rule1)
        self._sentenceMgr.append(rule2)
        self._sentenceMgr.append(rule3)
        self._sentenceMgr.append(rule4)
        self._sentenceMgr.append(rule5)


    def getSentence(self, value, intensity):
        ruleIdx = random.randint(0,  int(self.map(intensity, 0, 1023, 0, 4)))
        
        rule = self._sentenceMgr[ruleIdx].sRule
        sentence = ""
        for type in rule:
            if type == eWordType.eNoun:
                num = self._wMgr.getNounNum()
                index = random.randint(0, int(num * self.map(value, 0, 255, 1, 5)/5.0))
                text = self._wMgr.getNoun(0, index)
                self.addToOneDaySet(text)
                sentence += text

            elif type == eWordType.eVerb:
                num = self._wMgr.getVerbNum()
                val = self.map(value, 0, 255, 1, 5)/5.0             
                index = random.randint(0, int(num * val))
                text = self._wMgr.getVerb(0, index)
                self.addToOneDaySet(text)
                sentence += text
            elif type == eWordType.eAdjust:
                num = self._wMgr.getAdjNum()
                val = self.map(value, 0, 255, 1, 5)/5.0
                index = random.randint(0, int(num * val))
                text = self._wMgr.getAdj(0, index)
                self.addToOneDaySet(text)
                sentence += text            
            elif type == eWordType.eSubject:
                num = self._wMgr.getSubjectNum()
                sentence += self._wMgr.getSubject(0, num)

            elif type == eWordType.eQuestion:
                sentence += u"嗎？"
        return sentence;

    def save(self):
        self._wMgr.saveToFile()

    def map(self, value, leftMin, leftMax, rightMin, rightMax):
        leftSpan = leftMax - leftMin
        rightSpan = rightMax - rightMin
        valueScaled = float(value - leftMin) / float(leftSpan)
        val = rightMin + (valueScaled * rightSpan)
        val = max(min(val, rightMax), rightMin)
        return val
    
    def updateWord(self, segment):
        isUpdate = False
        for word in segment:
            text = word['word']
            type = word['flag']
            if(type == 'n'):
                isUpdate |= self._wMgr.addNoun(text)
            elif(type == 'v'):
                isUpdate |= self._wMgr.addVerb(text)
            elif(type == 'r'):
                isUpdate |= self._wMgr.addSubject(text)
            elif(type == 'a'):
                isUpdate |= self._wMgr.addAdj(text)

        self._needUpdate |= isUpdate

    def addToOneDaySet(self, text):
        if text not in self._oneDaySet:
            self._oneDaySet.append(text)

    def isInOneDaySet(self, text):
        if text in self._oneDaySet:
            return True
        else:
            return False

    def checkTimer(self, delta):
        self._timer -= delta
        self._oneDayTimer -= delta

        if self._timer <= 0:
            self._timer = 60 * 60
            if self._needUpdate:
                self._needUpdate = False
                self.save()
        if self._oneDayTimer <= 0:
            self._oneDayTimer = 60 * 60 * 24
            self._oneDaySet.clear()

    def __init__(self, rid):
        self._needUpdate = False
        self._timer = 60 * 60 #1 hour
        self._wMgr = wordMgr()
        self._wMgr.setup(rid)

        self._oneDayTimer = 60 * 60 * 24
        self._oneDaySet = []

        self._sentenceMgr = []
        self.__initSentenceMgr()

        