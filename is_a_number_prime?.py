def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num*0.05) + 1):
        if num % i == 0:
            return False
    return True

# Exemplos de uso
print(is_prime(7))   # Deve retornar True
print(is_prime(1))   # Deve retornar False
print(is_prime(-1))  # Deve retornar False
print(is_prime(73))   # Deve retornar False
print(is_prime(75))  
print(is_prime(2))  