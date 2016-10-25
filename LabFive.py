import datetime
import binascii
date = datetime.datetime.now();


    

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

print(ones)
print(zeros)
