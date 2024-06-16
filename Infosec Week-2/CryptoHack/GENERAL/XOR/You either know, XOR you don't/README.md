## Challenge Description
I've encrypted the flag with my secret key, you'll never be able to guess it.
```
Remember the flag format and how it might help you in this challenge!
```

`0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104`

## Writeup
I converted the hexadecimal string to bytes. Now I have the flag which is likely xorer with a key.
Now to find the key I xor it with the string "crypto{" because this is the starting part of the flag. This gives us `myXORke+y_Q\x0bHOMe$~seG8bGURN\x04DFWg)a|\x1dTM!an\x7f`

By observation the hey is likely to be "myXORkey" so I tried this and it worked.
[Here](script.py) is the script.

## Flag
crypto{1f_y0u_Kn0w_En0uGH_y0u_Kn0w_1t_4ll}
