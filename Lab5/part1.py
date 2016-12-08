 # The Blum Blum Shub PRNG, xn+1 = xn2 mod M
def blumblumshub(seed, mod, length=12):
    global x
    x = seed
    for i in range(length):
        yield (x * x) % mod

mod = 11 * 19
seed = 3
prng = blumblumshub(seed, mod, 12)
print("Numbers from Blum Blum Shub:")
for x in prng:
    print(x)

