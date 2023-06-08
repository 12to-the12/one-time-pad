with open('key.txt', 'r') as key:
    key = key.read()

def numeric (string):
    return map(lambda x: ord(x)-65, string)

def alphabetic (numbers):
    result =  map(lambda x: chr(x+65), numbers)
    return ''.join(result)

def encrypt(plaintext, key):
    plaintext = numeric(plaintext)
    key = numeric(key)
    result = map(lambda a, b: (a+b)%26, plaintext, key)
    return alphabetic(result)

def decrypt(ciphertext, key):
    ciphertext = numeric(ciphertext)
    key = numeric(key)
    result = map(lambda a, b: (a-b)%26, ciphertext, key)
    return alphabetic(result)

message = "one time pad"

message = message.upper()
message = message.replace(" ", "")

x = encrypt(message, key)

print(x)

x = decrypt(x, key)

print(x)

