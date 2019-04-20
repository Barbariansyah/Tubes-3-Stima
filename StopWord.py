from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory, StopWordRemover, ArrayDictionary
def removeStopWord(query):
    factory = StopWordRemoverFactory().get_stop_words()
    more_stopword = ['!','.',',','?']
    data = factory +more_stopword
    dic = ArrayDictionary(data)
    stopword = StopWordRemover(dic)
    return stopword.remove(query)