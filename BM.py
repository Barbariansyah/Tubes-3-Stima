from queue import PriorityQueue
from StopWord import removeStopWord
#BM
def lastoccurrence(database):
    MAX_CHAR = 256
    lastOcc = [-1]*MAX_CHAR
    for i in range (len(database)):
        lastOcc[ord(database[i])]=i
    return lastOcc

def BMExact(pat,txt):
    M = len(pat)
    N = len(txt)
    lastOcc = lastoccurrence(pat)
    shift = 0
    exact = 0
    count_same = 0
    j=0
    found = False
    while (shift<=N-M):
        j = M-1
        while (j>=0 and pat[j]==txt[shift+j]):
            j-=1
            count_same+=1
        if j<0:
            if (shift+M<N):
                shift += (M-lastOcc[ord(txt[shift+M])])
            else:
                shift +=1
            found = True
            exact = count_same/N
            break
        else:
            if (exact < (float)(count_same/N)):
                exact = (float)(count_same/N)
            count_same = 0
            if (j-lastOcc[ord(txt[shift+j])]>1):
                shift +=j-lastOcc[ord(txt[shift+j])]
            else:
                shift +=1
    if (exact < (float)(count_same/N)):
        exact = (float)(count_same/N)
    if (found):
        return exact
    else :
        return 0

def BMNotExact(pat,txt):
    N = len(txt)
    conf =0
    same_char = 0
    for words in pat.split(' '):
        same_char += len(txt)*BMExact(words,txt)
    space = txt.count(' ')
    if (space>pat.count(' ')):
        space = pat.count(' ')
    conf = float ((same_char+space)/(N))
    return conf

def BM(query,dictionary):
    output = []
    posiblequery = PriorityQueue()
    foundexact = False
    #iterasi semua keys dari dictionary
    for keys in dictionary:
        #Jika ketemu persis 
        temp_keys = removeStopWord(keys)
        #print(temp_keys)
        #print(BMExact(query,temp_keys))
        if (BMExact(query,temp_keys)==1):
            output.append(keys)
            foundexact = True
            break
        else:
            posiblequery.put((1-BMNotExact(query,temp_keys),keys))
    if (foundexact):
        return output
    else:
        countpos = 0
        above7 = False
        output = []
        while not posiblequery.empty():
            data = posiblequery.get()
            #print(1-data[0]," ",data[1])
            if ((1-data[0])>=0.75):
                above7 = True
                output.append(data[1])
                countpos+=1
                if ((1-data[0])>=1):
                    break
            elif (not above7):
                if((1-data[0])>=0.25):
                    output.append(data[1])
                    countpos+=1
                elif (len(output)>=1):
                    output.append(data[1])
                    countpos+=1
            if (countpos>=3):
                break
            
        return output