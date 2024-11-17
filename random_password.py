import random 
import string


join = string.ascii_letters + string.digits + string.punctuation

qntd = int(input("Digite a quantidade de caracteres que deseja na senha: "))

password = ''.join(random.choice(join) for _ in range(qntd))

print(f"Sua senha é -> {password}")

