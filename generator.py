import random
import string
from cryptography.fernet import Fernet
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def generate_key(master_password: str):
    salt = b'salt_'
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=100000)
    return base64.urlsafe_b64encode(kdf.derive(master_password.encode()))

print("--- WARNING ---")
print("If you forget your Master Password, there is NO way to recover your saved passwords.")
print("---------------")

master_pwd = input("Enter your Master Password: ")
length = int(input("Password length: "))
pwd_to_save = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))

print(f"Generated Password: {pwd_to_save}")

key = generate_key(master_pwd)
f = Fernet(key)
encrypted_pwd = f.encrypt(pwd_to_save.encode())

with open("passwords.enc", "ab") as file:
    file.write(encrypted_pwd + b"\n")

print("Password encrypted and saved to passwords.enc!")
