from Crypto.Cipher import AES
import os

KEY = os.urandom(16)
FLAG = b"DIMI{You_are_the_master_of_AES!}"

def menu():
    print("1. decrypt ciphertext")
    print("2. get encrypted FLAG")

def main():
    print("Welcome to my AES server!")
    menu()
    while True:
        i = int(input("Whatdoyouwant? > "))
        if i == 1:
            ciphertext = bytes.fromhex(input("ciphertext (hex) > "))

            cipher = AES.new(KEY, AES.MODE_ECB)
            pt = cipher.decrypt(ciphertext)
            print(pt.hex())

        elif i == 2:
            iv = os.urandom(16)

            cipher = AES.new(KEY, AES.MODE_CBC, iv)
            enc = cipher.encrypt(FLAG)
            print(iv.hex() + enc.hex())

        else:
            print("something wrong...")

main()