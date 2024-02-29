from Crypto.Util.number import getPrime
import random

slots = [getPrime(8) for _ in range(20)]
for i in range(len(slots)):
    while slots.count(slots[i]) >= 2:
        slots[i] = getPrime(8)
state = [random.randrange(0, slots[i]-1) for i in range(20)]

flag = "DIMI{You just scammed Wane with math... Poor Wane!}"

def main():
    coins = 1000

    print('Welcome to Wane\'s casino zone.')
    print('If you get 7 for all slots, you\'ll get flag!')
    print("Slot size:", slots)

    while coins > 0:
        print(f'You only have {coins} coins, that means you can only rotate {coins} time.')
        rotation = int(input('Enter Slots you want to rotate: '))
        if rotation < 0:
            print("You can't rotate negative times!")
            continue
        
        flagged = True
        for i in range(20):
            state[i] = (state[i] + slots[i] + rotation) % slots[i]
            if state[i] != 7:
                flagged = False
        
        print("The result is...", state)
        if flagged:
            print("Congs. Here's flag:", flag)
            return
        
        coins -= 1
    print("Oh no! You spent all coins! How poor...")

if __name__ == "__main__":
    main()