import random

range_password =int(input("""
        How long is the password?
                """)) 

password = "1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"

result = ''

if type(range_password) == int:
    for _ in range(range_password):
        result += random.choice(password)
    else:
        print(result)