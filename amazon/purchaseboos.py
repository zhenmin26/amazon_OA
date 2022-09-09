def purchasebooks(volumes: list) -> list:
    # prequel
    toBuy = []
    target = 1
    res = []

    for i in volumes:
        attemp = []
        if i != target:
            # add i to toBuy
            toBuy.append(i)
            attemp = [-1]
        elif i == target:
            attemp = [i]
            target += 1
            while toBuy:
                # buy the book, target update to next book
                if target in toBuy:
                    attemp.append(target)
                    toBuy.remove(target)
                    target += 1
        res.append(attemp)
    #         print(res)
    return res

volumes = [1,4,3,2,5]
result = purchasebooks(volumes)
print(result)