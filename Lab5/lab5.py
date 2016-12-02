import datetime
import binascii

from r4nd0m.SourceCode import RandomnessTests as r


date = datetime.datetime.now();    

# m = 11*22
# xi = 7

# def rng():
#     global xi
#     xi = (xi * xi) % m
#     return xi

# for i in range(12):
#     print rng()


b = str(date).split(' ')[1].replace(':', '')
bin = ' '.join(format(ord(x), 'b') for x in b ).replace(' ', '')
print(bin)

ones = 0 
zeros = 0
for c in bin:
    if c == '0':
        ones = ones + 1
    elif c == '1':
        zeros = zeros + 1


ra = r.RandomnessTester(None)
p_value = ra.monobit(bin)
print(p_value)