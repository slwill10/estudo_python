
array1 = [True,  True,  True,  False,
                True,  True,  True,  True ,
                True,  False, True,  False,
                True,  False, False, True ,
                True,  True,  True,  True ,
                False, False, True,  True ]

ovelha = 0

for n in array1:
    if n:
        ovelha += 1
print(ovelha)
