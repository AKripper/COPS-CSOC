## Challenge Description
Cryptosystems like RSA works on numbers, but messages are made up of characters. How should we convert our messages into numbers so that mathematical operations can be applied?

The most common way is to take the ordinal bytes of the message, convert them into hexadecimal, and concatenate. This can be interpreted as a base-16/hexadecimal number, and also represented in base-10/decimal.

To illustrate:
```
message: HELLO
ascii bytes: [72, 69, 76, 76, 79]
hex bytes: [0x48, 0x45, 0x4c, 0x4c, 0x4f]
base-16: 0x48454c4c4f
base-10: 310400273487
```

Convert the following integer back into a message:

`11515195063862318899931685488813747395775516287289682636499965282714637259206269`

## Writeup
We need to install PyCryptodome and import it with `from Crypto.Util.number import *` for this challenge. To install use the command `pip install PyCryptodome gmpy2 pwntools`.
I wrote this [script](B2L.py) for this challenge.

## Flag
crypto{3nc0d1n6_4ll_7h3_w4y_d0wn}
