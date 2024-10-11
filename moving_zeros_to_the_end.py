def move_zeros(lst):
    list = []
    count_zero = 0
    for num in lst:
        if num != 0:
            list.append(num)  
        else:
            count_zero += 1
    list.extend([0] * count_zero)

    return list

print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))
print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))