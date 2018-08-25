# -*- coding: UTF-8 -*-

from wordMgr import wordMgr
from enum import Enum
import random

class eWordType(Enum):
    eNoun = 0
    eVerb = 1
    eSubject = 2
    eAdjust = 3
    eParticles = 4
    eAdverb = 5
    eQuestion = 6
    eYesOrNot = 7
    eHaveOrNot = 8
    eHave = 9
    eIf = 10
    eWillBe = 11
    eBecause = 12
    eSo = 13
    eSince = 14
    eThen = 15
    eBa = 16
    eAll = 17
    eRe = 18
    eComma = 19
    eSubjectOrNoun = 20
    


class sentenceRule:
    def __init__(self):
        self.sRule = []

class sentenceGenerator:
    

    def __initSentenceMgr(self):
        ruleSet = []
        ruleSet.append(sentenceRule())
        ruleSet[-1].sRule.append(eWordType.eVerb)
        ruleSet[-1].sRule.append(eWordType.eNoun)

        ruleSet.append(sentenceRule())
        ruleSet[-1].sRule.append(eWordType.eAdjust)
        ruleSet[-1].sRule.append(eWordType.eNoun)

        ruleSet.append(sentenceRule())
        ruleSet[-1].sRule.append(eWordType.eSubject)
        ruleSet[-1].sRule.append(eWordType.eAdjust)

        ruleSet.append(sentenceRule())
        ruleSet[-1].sRule.append(eWordType.eSubject)
        ruleSet[-1].sRule.append(eWordType.eVerb)

        ruleSet.append(sentenceRule())
        ruleSet[-1].sRule.append(eWordType.eSubjectOrNoun)
        ruleSet[-1].sRule.append(eWordType.eYesOrNot)
        ruleSet[-1].sRule.append(eWordType.eNoun)

        ruleSet.append(sentenceRule())
        ruleSet[-1].sRule.append(eWordType.eSubjectOrNoun)
        ruleSet[-1].sRule.append(eWordType.eAdverb)
        ruleSet[-1].sRule.append(eWordType.eAdjust)

        ruleSet.append(sentenceRule())
        ruleSet[-1].sRule.append(eWordType.eSubjectOrNoun)
        ruleSet[-1].sRule.append(eWordType.eYesOrNot)
        ruleSet[-1].sRule.append(eWordType.eAdjust)
        ruleSet[-1].sRule.append(eWordType.eParticles)

        ruleSet.append(sentenceRule())
        ruleSet[-1].sRule.append(eWordType.eSubjectOrNoun)
        ruleSet[-1].sRule.append(eWordType.eHaveOrNot)
        ruleSet[-1].sRule.append(eWordType.eNoun)

        ruleSet.append(sentenceRule())
        ruleSet[-1].sRule.append(eWordType.eSubjectOrNoun)
        ruleSet[-1].sRule.append(eWordType.eYesOrNot)
        ruleSet[-1].sRule.append(eWordType.eVerb)

        ruleSet.append(sentenceRule())
        ruleSet[-1].sRule.append(eWordType.eNoun)
        ruleSet[-1].sRule.append(eWordType.eHave)
        ruleSet[-1].sRule.append(eWordType.eVerb)

        ruleSet.append(sentenceRule())
        ruleSet[-1].sRule.append(eWordType.eSubjectOrNoun)
        ruleSet[-1].sRule.append(eWordType.eVerb)
        ruleSet[-1].sRule.append(eWordType.eNoun)

        ruleSet.append(sentenceRule())
        ruleSet[-1].sRule.append(eWordType.eAdjust)
        ruleSet[-1].sRule.append(eWordType.eParticles)
        ruleSet[-1].sRule.append(eWordType.eNoun)
        ruleSet[-1].sRule.append(eWordType.eVerb)
        ruleSet[-1].sRule.append(eWordType.eSubject)

        ruleSet.append(sentenceRule())
        ruleSet[-1].sRule.append(eWordType.eSubjectOrNoun)
        ruleSet[-1].sRule.append(eWordType.eYesOrNot)
        ruleSet[-1].sRule.append(eWordType.eAdjust)
        ruleSet[-1].sRule.append(eWordType.eParticles)
        ruleSet[-1].sRule.append(eWordType.eNoun)

        ruleSet.append(sentenceRule())
        ruleSet[-1].sRule.append(eWordType.eSubject)
        ruleSet[-1].sRule.append(eWordType.eParticles)
        ruleSet[-1].sRule.append(eWordType.eNoun)
        ruleSet[-1].sRule.append(eWordType.eAdverb)
        ruleSet[-1].sRule.append(eWordType.eAdjust)

        ruleSet.append(sentenceRule())
        ruleSet[-1].sRule.append(eWordType.eSubject)
        ruleSet[-1].sRule.append(eWordType.eParticles)
        ruleSet[-1].sRule.append(eWordType.eNoun)
        ruleSet[-1].sRule.append(eWordType.eYesOrNot)
        ruleSet[-1].sRule.append(eWordType.eAdjust)
        ruleSet[-1].sRule.append(eWordType.eParticles)

        ruleSet.append(sentenceRule())
        ruleSet[-1].sRule.append(eWordType.eSubjectOrNoun)
        ruleSet[-1].sRule.append(eWordType.eHaveOrNot)
        ruleSet[-1].sRule.append(eWordType.eAdjust)
        ruleSet[-1].sRule.append(eWordType.eParticles)
        ruleSet[-1].sRule.append(eWordType.eNoun)

        ruleSet.append(sentenceRule())
        ruleSet[-1].sRule.append(eWordType.eSubject)
        ruleSet[-1].sRule.append(eWordType.eParticles)
        ruleSet[-1].sRule.append(eWordType.eNoun)
        ruleSet[-1].sRule.append(eWordType.eHaveOrNot)
        ruleSet[-1].sRule.append(eWordType.eVerb)

        ruleSet.append(sentenceRule())
        ruleSet[-1].sRule.append(eWordType.eNoun)
        ruleSet[-1].sRule.append(eWordType.eParticles)
        ruleSet[-1].sRule.append(eWordType.eNoun)
        ruleSet[-1].sRule.append(eWordType.eVerb)
        ruleSet[-1].sRule.append(eWordType.eAdjust)
        ruleSet[-1].sRule.append(eWordType.eParticles)
        ruleSet[-1].sRule.append(eWordType.eNoun)

        ruleSet.append(sentenceRule())
        ruleSet[-1].sRule.append(eWordType.eSubjectOrNoun)
        ruleSet[-1].sRule.append(eWordType.eYesOrNot)
        ruleSet[-1].sRule.append(eWordType.eAdjust)
        ruleSet[-1].sRule.append(eWordType.eParticles)
        ruleSet[-1].sRule.append(eWordType.eNoun)
        ruleSet[-1].sRule.append(eWordType.eQuestion)

        ruleSet.append(sentenceRule())
        ruleSet[-1].sRule.append(eWordType.eSubject)
        ruleSet[-1].sRule.append(eWordType.eParticles)
        ruleSet[-1].sRule.append(eWordType.eNoun)
        ruleSet[-1].sRule.append(eWordType.eAdverb)
        ruleSet[-1].sRule.append(eWordType.eAdjust)
        ruleSet[-1].sRule.append(eWordType.eQuestion)

        ruleSet.append(sentenceRule())
        ruleSet[-1].sRule.append(eWordType.eSubject)
        ruleSet[-1].sRule.append(eWordType.eParticles)
        ruleSet[-1].sRule.append(eWordType.eNoun)
        ruleSet[-1].sRule.append(eWordType.eYesOrNot)
        ruleSet[-1].sRule.append(eWordType.eAdjust)
        ruleSet[-1].sRule.append(eWordType.eParticles)
        ruleSet[-1].sRule.append(eWordType.eQuestion)

        ruleSet.append(sentenceRule())
        ruleSet[-1].sRule.append(eWordType.eSubjectOrNoun)
        ruleSet[-1].sRule.append(eWordType.eHaveOrNot)
        ruleSet[-1].sRule.append(eWordType.eAdjust)
        ruleSet[-1].sRule.append(eWordType.eParticles)
        ruleSet[-1].sRule.append(eWordType.eNoun)
        ruleSet[-1].sRule.append(eWordType.eQuestion)

        ruleSet.append(sentenceRule())
        ruleSet[-1].sRule.append(eWordType.eSubject)
        ruleSet[-1].sRule.append(eWordType.eParticles)
        ruleSet[-1].sRule.append(eWordType.eNoun)
        ruleSet[-1].sRule.append(eWordType.eHaveOrNot)
        ruleSet[-1].sRule.append(eWordType.eVerb)
        ruleSet[-1].sRule.append(eWordType.eQuestion)

        ruleSet.append(sentenceRule())
        ruleSet[-1].sRule.append(eWordType.eNoun)
        ruleSet[-1].sRule.append(eWordType.eParticles)
        ruleSet[-1].sRule.append(eWordType.eNoun)
        ruleSet[-1].sRule.append(eWordType.eVerb)
        ruleSet[-1].sRule.append(eWordType.eAdjust)
        ruleSet[-1].sRule.append(eWordType.eParticles)
        ruleSet[-1].sRule.append(eWordType.eNoun)
        ruleSet[-1].sRule.append(eWordType.eQuestion)

        ruleSet.append(sentenceRule())
        ruleSet[-1].sRule.append(eWordType.eIf)
        ruleSet[-1].sRule.append(eWordType.eSubjectOrNoun)
        ruleSet[-1].sRule.append(eWordType.eVerb)
        ruleSet[-1].sRule.append(eWordType.eComma)
        ruleSet[-1].sRule.append(eWordType.eSubject)
        ruleSet[-1].sRule.append(eWordType.eWillBe)
        ruleSet[-1].sRule.append(eWordType.eVerb)
        ruleSet[-1].sRule.append(eWordType.eQuestion)

        ruleSet.append(sentenceRule())
        ruleSet[-1].sRule.append(eWordType.eBecause)
        ruleSet[-1].sRule.append(eWordType.eAdjust)
        ruleSet[-1].sRule.append(eWordType.eParticles)
        ruleSet[-1].sRule.append(eWordType.eNoun)
        ruleSet[-1].sRule.append(eWordType.eHaveOrNot)
        ruleSet[-1].sRule.append(eWordType.eVerb)
        ruleSet[-1].sRule.append(eWordType.eComma)
        ruleSet[-1].sRule.append(eWordType.eSo)
        ruleSet[-1].sRule.append(eWordType.eSubjectOrNoun)
        ruleSet[-1].sRule.append(eWordType.eWillBe)
        ruleSet[-1].sRule.append(eWordType.eVerb)

        ruleSet.append(sentenceRule())
        ruleSet[-1].sRule.append(eWordType.eSince)
        ruleSet[-1].sRule.append(eWordType.eSubject)
        ruleSet[-1].sRule.append(eWordType.eAll)
        ruleSet[-1].sRule.append(eWordType.eVerb)
        ruleSet[-1].sRule.append(eWordType.eRe)
        ruleSet[-1].sRule.append(eWordType.eComma)
        ruleSet[-1].sRule.append(eWordType.eThen)
        ruleSet[-1].sRule.append(eWordType.eVerb)
        ruleSet[-1].sRule.append(eWordType.eBa)

        for rule in ruleSet:
            self._sentenceMgr.append(rule)


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
            elif type == eWordType.eParticles:
                sentence += u"的"
            elif type == eWordType.eAdverb:
                sentence += self._wMgr.getAdv()
            elif type == eWordType.eQuestion:
                sentence += u"嗎？"
            elif type == eWordType.eYesOrNot:
                if random.randint(0, 10) <= 5:
                    sentence += u"是"
                else:
                    sentence += u"不是"
            elif type == eWordType.eHaveOrNot:
                if random.randint(0, 10) <= 5:
                    sentence += u"有"
                else:
                    sentence += u"沒有"
            elif type == eWordType.eHave:
                sentence += u"有了"
            elif type == eWordType.eIf:
                sentence += u"如果"
            elif type == eWordType.eWillBe:
                sentence += u"會"
            elif type == eWordType.eBecause:
                sentence += u"因為"
            elif type == eWordType.eSo:
                sentence += u"所以"
            elif type == eWordType.eSince:
                sentence += u"既然"
            elif type == eWordType.eThen:
                sentence += u"那麼就"
            elif type == eWordType.eBa:
                sentence += u"吧"
            elif type == eWordType.eComma:
                sentence += u"，"
            elif type == eWordType.eAll:
                sentence += u"都"
            elif type == eWordType.eRe:
                sentence += u"了"
            elif type == eWordType.eSubjectOrNoun:
                index = 0
                text = ""
                isNoun = True
                if random.randint(0, 10) <= 5:
                    isNoun = True
                    num = self._wMgr.getNounNum()
                    index = random.randint(0, int(num * self.map(value, 0, 255, 1, 5)/5.0))
                else:
                    isNoun = False
                    index = self._wMgr.getSubjectNum()
                    
                if isNoun:
                    text = self._wMgr.getNoun(0, index)
                    self.addToOneDaySet(text)
                else:
                    text = self._wMgr.getSubject(0, index)
                sentence += text
        return sentence;

    def testAllRule(self):
        result = []
        id = 1
        for ruleSet in self._sentenceMgr:
            rule = ruleSet.sRule
            sentence = ""
            for type in rule:
                if type == eWordType.eNoun:
                    num = self._wMgr.getNounNum()
                    text = self._wMgr.getNoun(0, num)
                    sentence += text
                elif type == eWordType.eVerb:
                    num = self._wMgr.getVerbNum()
                    text = self._wMgr.getVerb(0, num)
                    sentence += text
                elif type == eWordType.eAdjust:
                    num = self._wMgr.getAdjNum()
                    text = self._wMgr.getAdj(0, num)
                    sentence += text            
                elif type == eWordType.eSubject:
                    num = self._wMgr.getSubjectNum()
                    sentence += self._wMgr.getSubject(0, num)
                elif type == eWordType.eParticles:
                    sentence += u"的"
                elif type == eWordType.eAdverb:
                    sentence += self._wMgr.getAdv()
                elif type == eWordType.eQuestion:
                    sentence += u"嗎？"
                elif type == eWordType.eYesOrNot:
                    if random.randint(0, 10) <= 5:
                        sentence += u"是"
                    else:
                        sentence += u"不是"
                elif type == eWordType.eHaveOrNot:
                    if random.randint(0, 10) <= 5:
                        sentence += u"有"
                    else:
                        sentence += u"沒有"
                elif type == eWordType.eHave:
                    sentence += u"有了"
                elif type == eWordType.eIf:
                    sentence += u"如果"
                elif type == eWordType.eWillBe:
                    sentence += u"會"
                elif type == eWordType.eBecause:
                    sentence += u"因為"
                elif type == eWordType.eSo:
                    sentence += u"所以"
                elif type == eWordType.eSince:
                    sentence += u"既然"
                elif type == eWordType.eThen:
                    sentence += u"那麼就"
                elif type == eWordType.eBa:
                    sentence += u"吧"
                elif type == eWordType.eComma:
                    sentence += u"，"
                elif type == eWordType.eAll:
                    sentence += u"都"
                elif type == eWordType.eRe:
                    sentence += u"了"
                elif type == eWordType.eSubjectOrNoun:
                    index = 0
                    text = ""
                    if random.randint(0, 10) <= 5:
                        isNoun = True
                        index = self._wMgr.getNounNum()
                        text = self._wMgr.getNoun(0, index)

                    else:
                        isNoun = False
                        index = self._wMgr.getSubjectNum()
                        text = self._wMgr.getSubject(0, index)
                    sentence += text
            result.append(str(id) + ":" + sentence)
            id += 1
        return result;

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

        