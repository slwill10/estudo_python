def descending_order(num):
    nume = list(str(num))
    nume.sort(reverse = True)
    return int(''.join(nume))



print(descending_order(0)) # 0
print(descending_order(15)) # 51
print(descending_order(123456789)) #987654321