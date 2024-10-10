def find_outlier(integers):
    impar = []
    par = []
    for i in integers:
        if i % 2 == 0:
            par.append(i)
        else:
            impar.append(i)
    if len(impar) == 1:
        return impar[0]
    else:
        return par[0]

        

print(find_outlier([2, 4, 6, 8, 10, 3])) # 3
print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
print(find_outlier([160, 3, 1719, 19, 11, 13, -21])) # 160