## Challenge Description
RSA relies on the difficulty of the factorisation of the modulus `N`. If the primes can be found then we can calculate the [Euler totient](https://leimao.github.io/article/RSA-Algorithm/) of `N` and thus decrypt the ciphertext.

Given `N = p*q` and two primes:

`p = 857504083339712752489993810777`

`q = 1029224947942998075080348647219`

What is the totient of N?

## Writeup
For `N = p*q`, we have Euler Totient `Φ(N) = Φ(p*q) = Φ(p)*Φ(q) = (p-1)*(q-1)`

[Here](rsa3.py) is the script.

## Flag
882564595536224140639625987657529300394956519977044270821168
