def coin_count(amount,n):
	coinNum = []
	n.sort()
	for i in range(len(n)-1,-1,-1):
		coin = amount // n[i]
		coinNum.append(coin)
		amount = amount - coin * n[i]
	return coinNum

n = [1,2,5,10,25,100]
coin_arr = coin_count(3174,n)
for i in range(0, len(n)):
	print('Coin value: '+ str(n[i])+'\'s num: '+str(coin_arr[i]))
