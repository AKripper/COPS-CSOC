## Challenge Description
Given the two primes:
```
p = 857504083339712752489993810777

q = 1029224947942998075080348647219
```
and the exponent:

`e = 65537`

What is the private key `d`?

## Writeup
It is given that, In RSA the private key is the [modular multiplicative](https://en.wikipedia.org/wiki/Modular_multiplicative_inverse) inverse of the exponent `e` modulo the totient of `N`.

Thus we will have:
```
d*e ≡ 1 mod Φ(N)
(or)
(d*e) % Φ(N) = 1
```
Now for calculating inverse, we require the extended Euclidean Algorithm which says: `a*x + b*y = gcd(a, b)`. Substituting `a=e`, `x=d`, `b=Φ(N)` and then modulus `Φ(N)` we get:
```
e*d + Φ(N)*y ≡ gcd(e, Φ(N)) mod Φ(N)
e*d + 0 ≡ gcd(e, Φ(N)) mod Φ(N)
e*d = 1 mod Φ(N)
```
So we have to apply extended Euclidean Algorithm for `e` and `Φ(N)` and then the value of `x` we get is the required private key `d`.

[Here](rsa4.py) is the script.

## Flag
121832886702415731577073962957377780195510499965398469843281
