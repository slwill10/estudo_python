def grow(arr):
    produc = 1
    for i in arr:
        produc *= i
    return produc

print(grow([2, 3, 4, 5]))