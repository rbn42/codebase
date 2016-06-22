# 主要实验python3
import numpy as np
import struct
#from bitstring import BitArray
print('二进制到整形')
s = '00010000'
print(s)
i = int(s, 2)
print(i)

print('浮点到bytes')
print(struct.pack('f', 1.0))
print('长整形到bytes')
print(struct.pack('L', 1))
print('bytes到长整形')
print(struct.unpack('L', b'00000000'))

print('整形到bytes')
i = 4
l = i.to_bytes(4, 'big')
print(l)

# print('byte到bit')
#input_str = '0xff'
#c = BitArray(hex=input_str)
# print(c.bin)
print('整形到bit')
print(bin(128))

print('整形数组到bytes')
print(bytes([224, 224, 192]))

print('整形数组到bit')
a = np.zeros(3, dtype='uint8')
print(np.unpackbits(a))
print('bit数组到整形数组')
a = [0, 1, 1, 1] * 8
l = np.packbits(np.asarray(a, dtype='b'))
print(l)
