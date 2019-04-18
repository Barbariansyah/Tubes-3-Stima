from queue import PriorityQueue
#BM
def lastoccurrence(database):
    MAX_CHAR = 256
    lastOcc = [-1]*MAX_CHAR
    for i in range (len(database)):
        lastOcc[ord(database[i])]=i
    return lastOcc

def BMExact(pat,query):
    M = len(pat)
    N = len(query)
    lastOcc = lastoccurrence(pat)
    shift = 0
    exact = 0
    j=0
    while (shift<=N-M):
        j = M-1
        while (j>=0 and pat[j]==query[shift+j]):
            j-=1
        if j<0:
            exact = float((M-j-1)/M)
            if (shift+M<N):
                shift += (M-lastOcc[ord(query[shift+M])])
            else:
                shift +=1
            break
        else:
            if (exact < float((M-j-1)/M)):
                exact = float((M-j-1)/M)
            if (j-lastOcc[ord(query[shift+j])]>1):
                shift +=j-lastOcc[ord(query[shift+j])]
            else:
                shift +=1
    if (exact < float((M-j-1)/M)):
        exact = float((M-j-1)/M)
    return exact

def BMNotExact(pat,query):
    M = len(pat)
    conf =0
    same_char = 0
    for words in pat.split(' '):
        same_char += len(words)*BMExact(words,query)
    space = query.count(' ')
    if (space>pat.count(' ')):
        space = pat.count(' ')
    conf = float ((same_char+space)/(M))
    return conf

def BM(query,dictionary):
    output = []
    posiblequery = PriorityQueue()
    foundexact = False
    for keys in dictionary:
        if (BMExact(keys,query)==1):
            output.append(keys)
            foundexact = True
            break
        else:
            posiblequery.put((1-BMNotExact(keys,query),keys))
    if (foundexact):
        return output
    else:
        countpos = 0
        above9 = False
        output = []
        while not posiblequery.empty():
            data = posiblequery.get()
            #Tingkat condifendent diatas 90%
            if ((1-data[0])>=0.9):
                above9 = True
                output.append(data[1])
                countpos+=1
                #TIngkat condifident 100%
                if ((1-data[0])>=1):
                    break
            #TIngkat confident dibawah 90% tapi diatas 50%
            elif (not above9):
                if((1-data[0])>=0.5):
                    output.append(data[1])
                    countpos+=1
            #Apabila sudah ada 3 kemungkinan iterasi dihentikan
            if (countpos>=3):
                break
        return output
