def inversion(n):
    if len(n) == 1:
        return n
    elif len(n) == 2:
        if n[0] > n[1]:
            n[0],n[1] = n[1],n[0]
        return n
    else:
        mid = len(n) // 2
        al = inversion(n[:mid])
        ar = inversion(n[mid:])
        indexL = 0
        indexR = 0
        counter = 0
        sortedList = []
        while indexL <= len(al) - 1 and indexR <= len(ar) - 1:
            if al[indexL] > ar[indexR]:
                counter += 1
                sortedList.append(ar[indexR])
                indexR += 1
            else:
                sortedList.append(al[indexL])
                indexL += 1
        while indexL <= len(al) - 1:
            counter += len(ar)
            sortedList.append(al[indexL])
            indexL += 1
        while indexR <= len(ar) - 1:
            sortedList.append(ar[indexR])
            indexR += 1
        return sortedList
    
a = [5,4,1,3,9]
print(inversion(a))