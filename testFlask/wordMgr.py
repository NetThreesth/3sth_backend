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
            jsonStr = json.dump(set, ensure_ascii=False)
            file.write(jsonStr)

    def getNounNum(self):
        return len(self._nounSet)

    def getVerbNum(self):
        return len(self._verbSet)

    def getAdjNum(self):
        return len(self._adjSet)

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

    def getAdj(self):
        return getAdj(0, self.getAdjNum())

    def getAdj(self, s, n):
        if(n > self.getAdjNum()):
            n = self.getAdjNum()
        index = random.randint(s, n)
        return self._adjSet[index]

    def addAdj(self, adj):
        if adj not in self._adjSet:
            print("Add adj:" + adj)
            self._adjSet.append(adj)

    def saveToFile(self):
        self.__save(self._nounPath, self._nounSet)
        self.__save(self._verbPath, self._verbSet)

    def setup(self, rid):
        self._nounSet = []
        self._verbSet = []
        self._adjSet = []
        self._rid = rid
        self._nounPath = "sentenceSet/noun_" + str(rid) + ".json"
        self._verbPath = "sentenceSet/verb_" + str(rid) + ".json"   
        #self._adjPath = "sentenceSet/adj_" + str(rid) + ".json"
        self.__load(self._nounPath, self._nounSet)
        self.__load(self._verbPath, self._verbSet)
        #self.__load(adjPath, self._adjSet)



