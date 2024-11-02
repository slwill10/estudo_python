def enough(cap, on, wait):
    restante = cap - on

    if restante >= wait:
        return 0
    else:
        return abs(wait - restante)
   

print(enough(10, 5, 5)) # 0
print(enough(100, 60, 50)) # 10
print(enough(20, 5, 5)) # 0