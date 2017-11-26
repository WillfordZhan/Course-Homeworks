def inversion(n):
    if len(n) == 1:
        counter = 0
        return n, counter
    else:
        mid = len(n) // 2
        # can assign all the return values to multiple variables
        al, counterl = inversion(n[:mid])
        ar, counterr = inversion(n[mid:])
        counter = counterl + counterr
        indexL = 0
        indexR = 0
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
        return sortedList, counter


a = [5, 4, 1, 3, 9]
print("The inversion of the input is: ", inversion(a)[1])
