## Challenge Description
Lets say we pick `p = 17`. Calculate `3^17 mod 17`. Now do the same but with `5^17 mod 17`.

What would you expect to get for `7^16 mod 17`? Try calculating that.
```
This interesting fact is known as Fermat's little theorem.
We'll be needing this (and its generalisations) when we look at RSA cryptography.
```
Now take the prime `p = 65537`. Calculate `273246787654^65536 mod 65537`.

Did you need a calculator?

## Writeup
For `a^b mod c`, we have the python function `pow(a,b,c)`. We get `pow(3,17,17)=3` and `pow(5,17,17)=5`, this shows that if we would have `pow(3,16,17)`, we are dividing it with three, and the answer thus will be `1`. The same holds for 5.

So we can generalize by saying that if we have a prime number p, then:

```
pow(a,p-1,p)=1
```

Thus our flag is 1.

## Flag
1
