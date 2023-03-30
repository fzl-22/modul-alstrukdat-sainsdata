def mean(n):
    sum = 0
    for i in range(len(n)):
        sum = sum + int(n[i])
    return round(sum/len(n), 2)

def median(n):
    myList = [int(i) for i in n]
    myList.sort()
    return myList[int(len(n)/2)]

def modus(n):
    myDict = {}
    for i in n:
        if i not in myDict.keys():
            myDict[i] = n.count(i)

    result = []
    for key, value in myDict.items():
        if value == max(myDict.values()):
            result.append(key)
    return result

N = input()
meanResult = mean(N)
medianResult = median(N)
modusResult = modus(N)
print(f"Mean: {meanResult}")
print(f"Median: {medianResult}")
print(f"Modus: {' '.join(modusResult)}")
