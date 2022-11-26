def deleteConsecutiveSimilar(integerList):
    repeat = len(integerList)
    while repeat > 0:
        lst = []
        ind = 0
        while ind in range(len(integerList) - 1):
            for item1 in integerList[ind]:
                for item2 in integerList[ind + 1]:
                    if item1 == item2:
                        lst.append(integerList[ind])
                        lst.append(integerList[ind + 1])
            ind = ind + 1
        for i in lst:
            for j in integerList:
                if i == j:
                    integerList.pop(integerList.index(j))
        repeat = repeat - 1
    return integerList