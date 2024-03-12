import random

class Pull:
    def __init__(self):
        pass
    def pull(self):
        return random.getrandbits(8)

genshin = Pull()
cnt = 0

while True:
    print("Pull your Furina")
    print("Enter -1 to exit")
    print("> ", end='')
    i = int(input())
    if i == -1:
        break
    result = genshin.pull()

    if cnt == 100:
        print("Success!!! You pulled Furina and finally you can brag to your friends!!!!!!!")
        print("Here's your flag as reward:", end='')
        with open('./flag', 'r') as f:
            print(f.read())
        exit(0)
    if result == i:
        cnt += 1
        print(f"Okay.. You pulled right result, and remaining {101-cnt}")
    else:
        print(f"No.. You pulled {i} and the RNG pulled {result}, as result you just pulled 3 stars..")

