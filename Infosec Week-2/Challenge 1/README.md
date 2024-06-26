## Challenge
We have two files given for this challenge:
- [source.enc](source.enc)
- [output.txt](output.txt)


## Writeup
The `source.enc` file contains a base64 encoded string. Use the command `cat source.enc | base64 -d` to decode this file. Decoding resulted in a python code. I analyse the code and explained all the steps in the source code [here](source.py).

The code involves a simple encoding of a flag using XOR.

Now I need to find out the strings that corresponds to the XORed outputs. Example:
```
AA  ->  4100   # 4141 ^ 41 = 4100
AB  ->  4103   # 4142 ^ 41 = 4103
AC  ->  4102   # 4143 ^ 41 = 4102
```
Clearly, "AA" is being encoded to 4100 and so on. We need to find out the 2 charecter strings that result in encoding to the output.

So I just calculated the encoded value of all the possible 2 character combinations in the ASCII table. I then iterated it such that it prints the string that corresponds to xorred value of four digits along output string. For this I used the encoding algorithm given in the source code.

[Here](script.py) is my script.

## Flag
CSOC23{345y_ba5364_4nd_x0r?}
