import json
import random

class wordMgr:
    def __load(self, path, set):
        with open(path, 'r', encoding='UTF-8') as file:
            str = file.read()
            data = json.loads(str)

            for val in data['text']:
                set.append(val)

    def getNounNum(self):
        return len(self._nounSet)

    def getVerbNum(self):
        return len(self._verbSet)

    def getNoun(self):
        return getNoun(0, self.getNounNum())

    def getNoun(self, s, n):
        if(n > self.getNounNum()):
            n = self.getNounNum()
        index = random.randint(s, n)
        return self._nounSet[index]

    def addNoun(self, noun):
        if noun not in self._nounSet:
            print("Add noun:" + noun)
            self._nounSet.append(noun)

    def getVerb(self):
        return getVerb(0, self.getVerbNum())

    def getVerb(self, s, n):
        if(n > self.getVerbNum()):
            n = self.getVerbNum()
        index = random.randint(s, n)
        return self._verbSet[index]

    def addVerb(self, verb):
        if verb not in self._verbSet:
            print("Add verb:" + verb)
            self._verbSet.append(verb)

    def setup(self, rid):
        self._nounSet = []
        self._verbSet = []
        self._rid = rid
        nounPath = "sentenceSet/noun_" + str(rid) + ".json"
        verbPath = "sentenceSet/verb_" + str(rid) + ".json"   
        self.__load(nounPath, self._nounSet)
        self.__load(verbPath, self._verbSet)



