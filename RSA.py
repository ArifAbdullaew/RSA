# coding: cp1251
import math
from ascii_codes import ascii_dict

my_st = "010000110101001001011001010100000101010001001111"
# print(hex(ord("CRYPTO")))

e = int(input("Your exponent\n"))
p = int(input("Simple number\n"))
q = int(input("Simple number\n"))
opentext = input("Your Opentext\n")
binr = list(opentext)


# print(list(opentext))


def evklidv(a, b):
    i = 1
    y2 = 0
    y1 = 1
    while (a != 0) & (b != 0):
        q = a // b
        r = a % b
        y = y2 - (q * y1)
        a = b
        b = r
        y2 = y1
        y1 = y
        i += 1
    return y2, i


n = p * q
f = (p - 1) * (q - 1)
d, m = evklidv(f, e)

bits = []
for letter in list(opentext):
    bits.append(ascii_dict[letter])
    print(''.join(bits))
binarystring = ''.join(bits)

# arr = []
# for i in binr:
#     s = ""
#     arr.append(bin(ord(i))[2:])
#     print(arr)
# binarystring = ''.join(arr)
# print(''.join(arr))

lenblock = math.floor(math.log(n, 2))
# if len(binarystring) % lenblock != 0:
# binarystringfull = binarystring.zfill('', (len(binarystring) - len(binarystring) % lenblock))
i = 0
while len(binarystring) % lenblock != 0:
    binarystring = binarystring.zfill(i)
    i += 1
print(binarystring)
# blocks = binarystring.zfill((len(binarystring) - len(binarystring) % lenblock) + len(binarystring))
ssplit = list(map(''.join, zip(*[iter(binarystring)] * lenblock)))
print(ssplit)
# print(d, m)
# if math.gcd(f, q) != 1:
#   print("Error: exponent value is not coprime to euler function")

# print(evklidv(21280, 13))
ssplit = [int(block, 2) for block in ssplit]
print(ssplit)

ssplit = [bin((num**e) % n)[2:].zfill(lenblock+1) for num in ssplit]
print(ssplit)

# bits = []
# for letter in list(opentext):
#     bits.append(ascii_dict[letter])
#     print(''.join(bits))
# binarystring = ''.join(bits)


# arr_encode = []
# for numbes in ssplit:
#     arr_encode.append(ssplit[numbes])
#     print(arr_encode)
# binarystring = ''.join(arr_encode)
# print(''.join(arr_encode))
ssplit = ''.join(ssplit)
print(ssplit)
k = 0
while len(ssplit) % 8 != 0:
    ssplit = ssplit.zfill(k)
    k += 1
print(ssplit)

encodenum = list(map(''.join, zip(*[iter(ssplit)] * 8)))
print(encodenum)

print([list(ascii_dict.keys())[list(ascii_dict.values()).index(i)] for i in encodenum])
# array_encodetext = []
# for symbol in list(encodenum):
#     array_encodetext.append(ascii_dict[symbol])
#     print(''.join(array_encodetext))
# encodetext = ''.join(array_encodetext)
# print(encodetext)

# lenblockencode = lenblock + 1
# arrencode = []
# for i in len(ssplit):
#     arrencode.append(ssplit)
#     print(''.join(arrencode))

