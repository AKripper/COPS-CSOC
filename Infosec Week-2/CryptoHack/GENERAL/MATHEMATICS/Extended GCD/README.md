## Challenge Description
Using the two primes `p = 26513, q = 32321`, find the integers u,v such that

`p * u + q * v = gcd(p,q)`

Enter whichever of `u` and `v` is the lower number as the flag.


## Writeup
For this challenge I learnt about [extended Euclidean algoritm](https://web.archive.org/web/20230511143526/http://www-math.ucdenver.edu/~wcherowi/courses/m5410/exeucalg.html) and then wrote the program that efficiently gives us values of `u` and `v` for any given `p` and `q`.
[Here](eea.py) is the script. 

For this challenge we get `GCD: 1, u: 10245, v: -8404`
Clearly -8404 is the lower number and is thus our flag.

## Flag
-8404
