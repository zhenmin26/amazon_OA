def findMaximumMaximaCount(categories: str) -> int:
    def findMax(hashmap: dict):
        keys = hashmap.keys()
        maxVal = -1
        index = 0
        for key in keys:
            if hashmap[key] > maxVal:
                maxVal = hashmap[key]
                index = key
        return index

    chmap = {}
    count = {}
    for i in categories:
        chmap[i] = chmap.get(i, 0) + 1
        #         print(chmap)
        # compare
        c = findMax(chmap)
        count[c] = count.get(c, 0) + 1
    res = count[findMax(count)]
    return res


cat = "bccaaacb"
print(findMaximumMaximaCount(cat))