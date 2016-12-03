from r4nd0m.SourceCode import RandomnessTests as r
 
# The Blum Blum Shub PRNG, xn+1 = xn2 mod M
def blumblumshub(seed, mod, rounds=10):
    global x
    x = seed
    for i in range(rounds):
        yield (x * x) % mod

mod = 11 * 19
seed = 3
prng = blumblumshub(seed, mod, 50)

bindata = ""
for x in prng:
    bindata += bin(x)[-1:]

randtest = r.RandomnessTester(None)
pValue = randtest.monobit(bindata)
if pValue < 0.01:
    print("%s. This PRNG is not considered random as per the monobit test, NIST SP 800-22" % pValue)
else:
    print("%s. This PRNG is considered random as per the monobit test, NIST SP 800-22" % pValue)