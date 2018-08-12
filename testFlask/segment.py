# -*- coding: UTF-8 -*-

from opencc import OpenCC 
import jieba
import jieba.posseg as pseg

class segment:
    
    __t2s = None
    __s2t = None

    def splitMsg(self, input):
        s_sentence = self.__t2s.convert(input)
        words = pseg.cut(s_sentence)
        result = "";
        for word in words:
            result += word.word + "[" + word.flag + "],"
        return self.__s2t.convert(result);

    def __init__(self):
        self.__t2s = OpenCC('t2s')
        self.__s2t = OpenCC('s2t')
