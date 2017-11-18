def permutation_r(n):
	head = n[len()-1];
	n.pop(-1);
	if (n.len()<=1):
		sequence = [];
		sequence.append(n[0]);
		return sequence;
	else
		sequence = permutation_r(n);
		baseStr = sequence[0];
		baseStrNum = sequence.len();
		for i in sequence:
			sequence[i] = head + sequence[i];
		for i in xrange(0,baseStr):
			elementToSwap = baseStr[i];
			for j in xrange(0,baseStrNum):
				sequence.append(sequence[j].replace(head,elementToSwap));
			