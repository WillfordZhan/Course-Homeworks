def permutation_r(n):
	head = n[len(n)-1]
	if (len(n)<=1):
		sequence1 = []
		sequence1.append(n[0])
		return sequence1
	else:
		sequence = permutation_r(n[:-1])
		baseStr = sequence[0]
		baseStrNum = len(sequence)
		i = 0
		while i < len(sequence):
			sequence[i] = head + sequence[i]
			i += 1
		for k in baseStr:
			elementToSwa = k
			for j in range(0,baseStrNum):
				ele = sequence[j]
				eleSwapInd = ele.index(elementToSwa)
				ele = ele.replace(head,elementToSwa)
				ele = ele[:eleSwapInd] + head + ele[eleSwapInd + 1:]
				sequence.append(ele)
		return sequence

a = ["A", "B", "C"]
print(permutation_r(a))