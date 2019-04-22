from queue import PriorityQueue
from StopWord import removeStopWord
#KMP
def Prefix_Suffix(database):
    length = 0
    M = len(database)
    arr = [0]*M
    arr[0]
    i = 1
    while (i<M):
        if database[i] == database[length]:
            length+=1
            arr[i] = length
            i+=1
        else:
            if length!=0:
                length = arr[length-1]
            else:
                arr[i] = 0
                i+=1
    return arr

def KMPExact(pat,txt):
    PI = Prefix_Suffix(pat)
    M = len(pat)
    N = len(txt)
    i = 0
    j = 0
    exact = 0
    count_same = 0
    found = False
    while i<N:
        if pat[j] == txt[i]:
            i+=1
            j+=1
            count_same+=1
        if j==M:
            exact = float(count_same/N)
            found = True
            break
        elif i<N and pat[j]!=txt[i]:
            if (exact < float(count_same/N)):
                exact = float(count_same/N)
            count_same = 0
            if j!=0:
                j = PI[j-1]
            else:
                i+=1
    if (j<M):
        if (exact < float(count_same/N)):
            exact = float(count_same/N)
    if (found):
        return exact
    else:
        return 0

def KMPNotExact(pat,txt):
    N = len(txt)
    conf =0
    same_char = 0
    for words in pat.split(' '):
        same_char += len(txt)*KMPExact(words,txt)
    space = txt.count(' ')
    if (space>pat.count(' ')):
        space = pat.count(' ')
    conf = float ((same_char+space)/(N))
    return conf

def KMP(query,dictionary):
    output = []
    posiblequery = PriorityQueue()
    foundexact = False
    #iterasi semua keys dari dictionary
    for keys in dictionary:
        #Jika ketemu persis 
        temp_keys = removeStopWord(keys)
        if (KMPExact(query,temp_keys)==1):
            output.append(keys)
            foundexact = True
            break
        else:
            posiblequery.put((1-KMPNotExact(query,temp_keys),keys))
    if (foundexact):
        return output
    else:
        countpos = 0
        above9 = False
        output = []
        while not posiblequery.empty():
            data = posiblequery.get()
            if ((1-data[0])>=0.75):
                above9 = True
                output.append(data[1])
                countpos+=1
                if ((1-data[0])>=1):
                    break
            elif (not above9):
                if((1-data[0])>=0.25):
                    output.append(data[1])
                    countpos+=1
                elif (len(output)>=1):
                    output.append(data[1])
                    countpos+=1
            if (countpos>=3):
                break
            
        return output