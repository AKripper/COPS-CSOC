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
d*e ≡ 1 (mod Φ(N))
(or)
(d*e) % Φ(N) = 1
```
Now for calculating inverse, we require the extended Euclidean Algorithm which says: `a*x + b*y = gcd(a, b)`. Substituting `a=d`, `x=e`, `b=Φ(N)` and then modulus `Φ(N)` we get:
```
d*e + Φ(N)*y ≡ gcd(d, Φ(N)) mod Φ(N)
```

## Flag
