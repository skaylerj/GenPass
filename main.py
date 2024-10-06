import random
password = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
question = int(input("Какой длины будет ваш пароль?"))
password_1 = "" 

for i in range(question):
    password_1 += random.choice(password)

print(password_1)
