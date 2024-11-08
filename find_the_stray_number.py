def stray(arr):
    num = {}

    for n in arr:
        if n in num:
            num[n] += 1
        else:
            num[n] = 1

    for key, value in num.items():
        if value == 1:
            print(key) 

stray([1, 1, 1, 1, 1, 1, 2]), 2
stray([2, 3, 2, 2, 2]), 3
stray([3, 2, 2, 2, 2]), 3