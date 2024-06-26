## Challenge Description
RSA encryption is modular exponentiation of a message with an exponent `e` and a modulus `N` which is normally a product of two primes: `N = p * q`.

Together the exponent and modulus form an RSA "public key" `(N, e)`. The most common value for `e` is `0x10001` or `65537`.

"Encrypt" the number `12` using the exponent `e = 65537` and the primes `p = 17` and `q = 23`. What number do you get as the ciphertext?

## Writeup
In RSA encryption, a message `m` is encoded to a ciphertext `c` in the following way:
```
c = m^e mod N
(or)
c = pow(m,e,N)
```
[Here](rsa2.py) is the script.

## Flag
301
