import random

class Cipher:
    def __init__(self):
        self.blocks = random.randrange(1, 25)
    def encrypt(self, what):
        ret = ""
        for i in what:
            ord_i = ord(i)
            if ord('A') <= ord_i <= ord('Z'):
                ord_i = ((ord_i - ord('A') + 26 + self.blocks) % 26) + ord('A')
            elif ord('a') <= ord_i <= ord('z'):
                ord_i = ((ord_i - ord('a') + 26 + self.blocks) % 26) + ord('a')
            ret += chr(ord_i)
        return ret

cipher = Cipher()
enc_flag = "DIMI{" + cipher.encrypt('Caesar_Cipher_is_basic_skillz') + "}"

while True:
    print("Welcome to Wane-Ciphersystem")
    print("[1] Encrypt Your data")
    print("[2] Get encrypted flag data")
    option = int(input('> '))
    if option == 1:
        what = input('Enter data: ')
        print(cipher.encrypt(what))
    elif option == 2:
        print(enc_flag)
