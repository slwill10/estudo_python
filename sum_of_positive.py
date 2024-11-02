def positive_sum(arr):
    qtd = 0
    for n in arr:
        if n > 0:
            qtd += n 
    return qtd

print(positive_sum([1,2,3,4,5])) # 15
print(positive_sum([1,-2,3,4,5]))# 13
print(positive_sum([-1,2,3,4,-5])) # 9