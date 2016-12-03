from r4nd0m.SourceCode import RandomnessTests as r
 
# The Blum Blum Shub PRNG, xn+1 = xn2 mod M
def blumblumshub(seed, mod, rounds=10):
    global x
    x = seed
    for i in range(rounds):
        yield (x * x) % mod

mod = 11 * 19
seed = 3
prng = blumblumshub(seed, mod)
print("Numbers from Blum Blum Shub:")
for x in prng:
    print(x)

