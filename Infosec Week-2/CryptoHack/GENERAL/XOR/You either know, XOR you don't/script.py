from pwn import *

str="0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
byte=bytes.fromhex(str)
key="myXORkey"
flag=xor(byte,key)
print(flag)