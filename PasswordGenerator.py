import random 

characters = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHJIKLMNOPQRSTUVWXYZ!@#$%^&*()?"

chosen = random.sample(characters, 6)
password = "".join(chosen)
print(password)