import hashlib
import scrypt
import base64

print ("************HASH CALCULATOR************")
print("========================================")

string = input("Enter your text to convert: ")
print(' 1. md2','\n','2. md5','\n','3. sha1','\n','4. sha256','\n','5. sha512','\n','6. base64',)
input = input('Enter code: ')
def hashConvert(string, input):
    if input == '1':
        return hashlib.md2(string.encode()).hexdigest()
    elif input == '2':
        return hashlib.md5(string.encode()).hexdigest()
    elif input == '3':
        return hashlib.sha1(string.encode()).hexdigest()
    elif input == '4':
        return hashlib.sha256(string.encode()).hexdigest()
    elif input == '5':
        return hashlib.sha512(string.encode()).hexdigest()
    elif input == '6':
        return base64.b64encode(string.encode())
    else:
        return 'Invailed Hash Type'

    
hash_value = hashConvert(string, input)
print(hash_value)