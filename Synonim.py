def initializeSynonim(filename):
    dic = {}
    with open(filename) as file:
        lines = file.readlines()
        for line in lines:
            word,synonim = line.strip().split(':|:')
            dic.update({word.lower().strip():synonim.lower().strip()})
    return dic
def changeSynonim(query):
    temp = ""
    dic = initializeSynonim("synonim.txt")
    for word in query.split(' '):
        if(dic.__contains__(word)):
            temp +=dic[word]+" "
        else:
            temp += word+" "
    return temp.strip()

