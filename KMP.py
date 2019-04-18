from queue import PriorityQueue
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

def KMPExact(pat,query):
    PI = Prefix_Suffix(pat)
    M = len(pat)
    N = len(query)
    i = 0
    j = 0
    exact = 0
    while i<N:
        if pat[j] == query[i]:
            i+=1
            j+=1
        if j==M:
            exact = float(j/M)
            break
        elif i<N and pat[j]!=query[i]:
            if (exact < float((j-1)/M)):
                exact = float(j/M)
            if j!=0:
                j = PI[j-1]
            else:
                i+=1
    if (j<M):
        if (exact < float((j-1)/M)):
            exact = float(j/M)
    return exact

def KMPNotExact(pat,query):
    M = len(pat)
    conf =0
    same_char = 0
    for words in pat.split(' '):
        same_char += len(words)*KMPExact(words,query)
    space = query.count(' ')
    if (space>pat.count(' ')):
        space = pat.count(' ')
    conf = float ((same_char+space)/(M))
    return conf

def KMP(query,dictionary):
    output = []
    posiblequery = PriorityQueue()
    foundexact = False
    #iterasi semua keys dari dictionary
    for keys in dictionary:
        #Jika ketemu persis 
        if (KMPExact(keys,query)==1):
            output.append(keys)
            foundexact = True
            break
        else:
            posiblequery.put((1-KMPNotExact(keys,query),keys))
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
                if((1-data[0])>=0.5):
                    output.append(data[1])
                    countpos+=1
            if (countpos>=3):
                break
            
        return output