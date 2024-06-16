## Challenge Description
Below is a series of outputs where three random keys have been XOR'd together and with the flag. Use the above properties to undo the encryption in the final line to obtain the flag.

```
KEY1 = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf
```

## Writeup
Firstly I converted all the hex strings to bytes. Now I XOR the 4th string with 3rd string to get `FLAG ^ KEY1` and the finally XOR this with the 1st string to get `FLAG`.
This [script](xorprop.py) demonstrates this.

## Flag
crypto{x0r_i5_ass0c1at1v3}
