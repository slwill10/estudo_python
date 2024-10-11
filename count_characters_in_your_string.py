def count(s):
    if not s:
        return {}
    
    letra = {}
    
    for i in s:
        if i in letra:
            letra[i] += 1
        else:
            letra[i] = 1
    return letra

count('aba')
print(count('')), {}
print(count('aa'), ),{'a' : 2}
print(count('aabb')), {'b' : 2, 'a' : 2}