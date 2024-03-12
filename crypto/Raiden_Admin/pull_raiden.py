import random

class Pull:
    def __init__(self):
        self.a = random.randint(0, 10 ** 9 * 4)
        self.b = random.randint(0, 10 ** 9 * 4)
        self.m = 1 << 32
        self.seed = random.randint(0, 10 ** 9 * 4)
        for _ in range(random.randrange(10 ** 3, 10 ** 4)):
            self.change_seed()
    def change_seed(self):
        self.seed = (self.seed * self.a + self.b) % self.m
    def pull(self):
        self.change_seed()
        return self.seed

genshin = Pull()

while True:
    print("Pull your Raiden Shogun")
    print("Enter -1 to exit")
    print("> ", end='')
    i = int(input())
    if i == -1:
        break
    result = genshin.pull()
    if result == i:
        print("Success!!! You pulled Raiden Shogun and finally you can brag to your friends!!!!!!!")
        print("Here's your flag as reward:", end='')
        with open('./flag', 'r') as f:
            print(f.read())
        exit(0)
    else:
        print(f"No.. You pulled {i} and the RNG pulled {result}, as result you just pulled 3 stars..")

