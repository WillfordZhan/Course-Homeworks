def coin_count(n):
    coin_num = 0
    coin_num = n // 100
    left = n % 100
    if left != 0:
        coin_num += left// 25
        left = left  % 25
        if left != 0:
            coin_num += left// 10
            left = left  % 10
            if left != 0:
                coin_num += left// 5
                left = left  % 5
    coin_num += left
    return coin_num

def coin_count(n,arr):
    coin_count = 0
    for i in arr:
        coin_count = amount // i
        coin_list　

print(coin_count(224))