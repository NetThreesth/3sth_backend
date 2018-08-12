# -*- coding: UTF-8 -*-

from wordMgr import wordMgr
from enum import Enum
import random

class eWordType(Enum):
    eNoun = 0
    eVerb = 1
    eSubject = 2
    eQuestion = 3

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
        rule2.sRule.append(eWordType.eSubject)
        rule2.sRule.append(eWordType.eVerb)
        rule2.sRule.append(eWordType.eQuestion)

        rule3 = sentenceRule()
        rule3.sRule.append(eWordType.eNoun)
        rule3.sRule.append(eWordType.eVerb)
        rule3.sRule.append(eWordType.eQuestion)

        self._sentenceMgr.append(rule1)
        self._sentenceMgr.append(rule2)
        self._sentenceMgr.append(rule3)

    def __getSubject(self):
        val = random.randint(0, 3)
        if val == 0:
            return u"你"
        elif val == 1:
            return u"我"
        else:
            return u"他"

    def getSentence(self, value, intensity):
        ruleIdx = random.randint(0,  int(self.map(intensity, 0, 255, 0, 2)))
        rule = self._sentenceMgr[ruleIdx].sRule
        sentence = ""
        for type in rule:
            if type == eWordType.eNoun:
                num = self._wMgr.getNounNum()
                index = random.randint(0, int(num * self.map(value, 0, 255, 1, 5)/5.0))
                text = self._wMgr.getNoun(0, index)
                sentence += text

            elif type == eWordType.eVerb:
                num = self._wMgr.getVerbNum()
                val = self.map(value, 0, 255, 1, 5)/5.0
             
                index = random.randint(0, int(num * val))
                text = self._wMgr.getVerb(0, index)
                sentence += text

            elif type == eWordType.eSubject:
                sentence += self.__getSubject()
            elif type == eWordType.eQuestion:
                sentence += u"了嗎？"
        return sentence;


    def map(self, value, leftMin, leftMax, rightMin, rightMax):
        leftSpan = leftMax - leftMin
        rightSpan = rightMax - rightMin
        valueScaled = float(value - leftMin) / float(leftSpan)
        return rightMin + (valueScaled * rightSpan)
    
    def updateWord(self, segmentMsg):
        
        if(len(segmentMsg) == 0):
            return
        words = segmentMsg.split(',')
        for word in words:
            text = word[:word.find('[')]
            type = word[word.find('[') + 1:word.find(']')]
            if(type == 'n'):
                self._wMgr.addNoun(text)
            elif(type == 'v'):
                self._wMgr.addVerb(text)

    def __init__(self, rid):
        self._wMgr = wordMgr()
        self._wMgr.setup(rid)

        self._sentenceMgr = []
        self.__initSentenceMgr()

        