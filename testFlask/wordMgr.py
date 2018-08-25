import json
import random

class wordMgr:
    def __load(self, path, set):
        with open(path, 'r', encoding='UTF-8') as file:
            str = file.read()
            data = json.loads(str)

            for val in data['text']:
                set.append(val)

    def __save(self, path, set):
        with open(path, 'w', encoding='UTF-8') as file:
            data = {'text':set}
            jsonStr = json.dumps(data, ensure_ascii=False)
            file.write(jsonStr)

    def getNounNum(self):
        return len(self._nounSet)

    def getVerbNum(self):
        return len(self._verbSet)

    def getSubjectNum(self):
        return len(self._subjectSet)

    def getAdjNum(self):
        return len(self._adjSet)

    def getNoun(self):
        return getNoun(0, self.getNounNum())

    def getNoun(self, s, n):
        if(n > self.getNounNum()):
            n = self.getNounNum()
        index = random.randint(s, n - 1)
        return self._nounSet[index]

    def addNoun(self, noun):
        if noun not in self._nounSet:
            self._nounSet.append(noun)
            return True
        else:
            return False


    def getVerb(self):
        return getVerb(0, self.getVerbNum())

    def getVerb(self, s, n):
        if(n > self.getVerbNum()):
            n = self.getVerbNum()
        index = random.randint(s, n - 1)
        return self._verbSet[index]

    def addVerb(self, verb):
        if verb not in self._verbSet:
            self._verbSet.append(verb)
            return True
        else:
            return False

    def getSubject(self):
        return getSubject(0, self.getSubjectNum())

    def getSubject(self, s, n):
        if(n > self.getSubjectNum()):
            n = self.getSubjectNum()
        index = random.randint(s, n - 1)
        return self._subjectSet[index]

    def addSubject(self, subject):
        if subject not in self._subjectSet:
            self._subjectSet.append(subject)
            return True
        else:
            return False

    def getAdj(self):
        return getAdj(0, self.getAdjNum())

    def getAdj(self, s, n):
        if(n > self.getAdjNum()):
            n = self.getAdjNum()
        index = random.randint(s, n - 1)
        return self._adjSet[index]

    def addAdj(self, adj):
        if adj not in self._adjSet:
            self._adjSet.append(adj)
            return True
        else:
            return False

    def getAdv(self):
        index = random.randint(0, len(self._advSet) - 1)
        return self._advSet[index]

    def saveToFile(self):
        self.__save(self._nounPath, self._nounSet)
        self.__save(self._verbPath, self._verbSet)
        self.__save(self._subjectPath, self._subjectSet)
        self.__save(self._adjPath, self._adjSet)

    def setup(self, rid):
        self._nounSet = []
        self._verbSet = []
        self._subjectSet = []
        self._adjSet = []
        self._advSet = [u"很好",u"非常",u"十分",u"有點",u"不太"]
        self._rid = rid
        self._nounPath = "sentenceSet/noun_" + str(rid) + ".json"
        self._verbPath = "sentenceSet/verb_" + str(rid) + ".json"   
        self._adjPath = "sentenceSet/adj_" + str(rid) + ".json"
        self._subjectPath = "sentenceSet/sub_" + str(rid) + ".json"
        self.__load(self._nounPath, self._nounSet)
        self.__load(self._verbPath, self._verbSet)
        self.__load(self._adjPath, self._adjSet)
        self.__load(self._subjectPath, self._subjectSet)



