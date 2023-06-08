with open('key.txt', 'r') as key:
    key = key.read()
# 65
char_count = 94
# def peek(x): print(list(x))
# peek = lambda x: print(list(x))
def numeric (string):
    return map(lambda x: ord(x)-32, string)

def alphabetic (numbers):
    result =  map(lambda x: chr(x+32), numbers)
    # result = list(result)
    return ''.join(result)

def encrypt(plaintext, key):
    plaintext = list( numeric(plaintext) )
    key = list( numeric(key) )
    print(plaintext)
    print(key)
    print(type(plaintext))
    print(type(key))
    result = map(lambda a, b: (a+b)%char_count, plaintext, key)
    result = list(result)
    return alphabetic(result)

def decrypt(ciphertext, key):
    ciphertext = numeric(ciphertext)
    key = numeric(key)
    result = map(lambda a, b: (a-b)%char_count, ciphertext, key)
    return alphabetic(result)

message = "one time pad"


message = message.upper()
message = message.replace(" ", "")
print(f"original:  '{message}'")
x = encrypt(message, key)

print(f"encrypted: '{x}'")
print(type(x))
x = decrypt(x, key)

print(f"decrypted: '{x}'")

