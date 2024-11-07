def reverse_seq(n):
    count = []
    for y in range(n, 0, -1):
        count.append(y)
    return count
print(reverse_seq(5)),[5,4,3,2,1]