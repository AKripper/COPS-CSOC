from pwn import *

str="73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
byte=bytes.fromhex(str)
for i in range(100):
    print(i,"->",xor(byte,i))