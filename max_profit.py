def max_profit(n):
    if len(n) <= 2:
        if n[0] >= n[1]:
            n[0], n[1] = n[1], n[0]
        maxp = n[0] - n[1]
        return maxp, n[0], n[1]
        
    else:
        mid = len(n) // 2
        print(mid)
        LTuple = max_profit(n[:mid])
        RTuple = max_profit(n[mid:])
        maxL = LTuple[0]
        maxR = RTuple[0]
        maxAll = RTuple[2] - LTuple[1]
        maxPro = max(maxL, maxR, maxAll)
        if maxPro == maxL:
            return maxPro, LTuple[1], LTuple[2]
        elif maxPro == maxR:
            return maxPro, RTuple[1], RTuple[2]
        else:
            return maxPro, LTuple[1], RTuple[2]


a = [7, 4, 9, 1, 2, 7, 9, 14]
print(max_profit(a))
