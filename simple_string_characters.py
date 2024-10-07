def solve(s):
    numero = 0
    maiuscula = 0
    minuscula = 0
    resto = 0
    for x in s:
        if x.isdigit():
            numero += 1
        elif x.isupper():
            maiuscula += 1
        elif x.islower():
            minuscula += 1
        else:
            resto += 1
    return [maiuscula, minuscula, numero, resto]


print(solve("Codewars@codewars123.com"))
print(solve("bgA5<1d-tOwUZTS8yQ"))
print(solve("P*K4%>mQUDaG$h=cx2?.Czt7!Zn16p@5H"))
print(solve("RYT'>s&gO-.CM9AKeH?,5317tWGpS<*x2ukXZD"))
print(solve("$Cnl)Sr<7bBW-&qLHI!mY41ODe")) 