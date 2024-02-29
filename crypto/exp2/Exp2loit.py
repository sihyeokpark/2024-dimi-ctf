from Crypto.Util.number import getPrime, bytes_to_long

N, e = getPrime(2048), getPrime(256)

print('N =', N)
print('e =', e)

a = int(input(), 16) # should be hex value
b = int(input(), 16)

if a >= 2**2048 or a < 2**1024 or b < 2**1024 or b >= 2**2048:
    print('I don\'t accept "vulnerable" values')
    exit(1)

c = pow(a, e, N) * pow(b, e, N)

with open('./flag', 'r') as file:
    flag = file.read()

print(c)
if c == pow(bytes_to_long(b'wane is god'), e, N):
    print(flag)
