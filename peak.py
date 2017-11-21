def peak_w(n):
    i = 0
    while i < len(n) - 1:
        if i > 2 and n[i - 1] < n[i] and n[i] > n[i + 1]:
            return n[i]
        i += 1

    if n[i] > n[i - 1]:
        return n[i]
    else:
        return n[0]

def peak_f(n):
    for i in range(0, len(n)):
        if i ==1:
            continue
        if n[i - 1] < n[i] and i < len(n) -1 and  n[i] > n[i + 1] :
            return n[i]
    if n[-1] >= n[-2]:
        return n[-1]
    else:
        return n[0]

a = [1, 2, 3, 5, 3]
b = [1, 2, 3, 4, 5]
c = [5, 4, 3, 2, 1]
print(peak_w(a))
print(peak_w(b))
print(peak_w(c))
print(peak_f(a))
print(peak_f(b))
print(peak_f(c))
