def insert_sort(arr):
    if len(arr) <= 2:
        if arr[0] > arr[1]:
            temp = arr[0]
            arr[0] = arr[1]
            arr[1] = temp
        return arr
    last = arr[len(arr) - 1]
    sortedArr = insert_sort(arr[:len(arr) - 1])

    low = 0
    high = len(sortedArr) - 1
    mid = 0
    while(high >= low):
        mid = int(high + low) // 2
        if last > sortedArr[mid]:
            low = mid + 1
        else:
            high = mid - 1
    if sortedArr[mid] <= last:
        sortedArr.insert(mid + 1, last)
    else:
        sortedArr.insert(mid, last)
    return sortedArr


a = [5, 2, 3, 4, 7, 9]
print(insert_sort(a))
