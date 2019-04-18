import random
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory, StopWordRemover, ArrayDictionary
from BM import BM
from KMP import KMP
from Regex import Regex
def removeStopWord(query):
    factory = StopWordRemoverFactory().get_stop_words()
    more_stopword = ['!','.',',','?']
    data = factory +more_stopword
    dic = ArrayDictionary(data)
    stopword = StopWordRemover(dic)
    return stopword.remove(query)

def read_dictionary(filename):
    dic = {}
    with open(filename) as file:
        lines = file.readlines()
        for line in lines:
            question,answer = line.strip().split(':|:')
            dic.update({removeStopWord(question):answer})
    return dic

def randomQuestion(dic):
    temp = random.randint(0,len(dic)-1)
    return list(dic.keys())[temp]

def answer(output,dic):
    if len(output)==0:
        return "Maksud anda = " + randomQuestion(dic)
    elif len(output)==1:
        return str(dic[output[0]])
    else:
        ans = "Maksud anda = "
        for i in range (len(output)):
            if (i>2):
                break
            else:
                ans += str(i+1)+". "+str(output[i])+" "
        return ans

def askBot(query,dic,method):
    query = removeStopWord(query)
    if method=="KMP":
        return answer(KMP(query,dic),dic)
    elif method == "BM":
        return answer(BM(query,dic),dic)
    elif method == "Regex":
        return answer(BM(query,dic),dic)
