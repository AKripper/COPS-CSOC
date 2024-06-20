## Challenge
Given file:
- [encoded.txt](encoded.txt)

## Writeup
the given encoded string can be divided to four parts:
```
enc1 -> 01000011 01010011 01001111 01000011 00110010
enc2 -> 33 7b 6a 75 35 37 5f
enc3 -> ZDFmZjNyM243XzNuYw==
enc4 -> 60 144 61 156 66 65 137 154 60 154 175
```

Each of the parts are encoded in a different way.
[Here](script.py) is the script.

### enc1
I converted the 8 bit binary numbers to their corresponding ascii values.
It decodes to `CSOC2`.

### enc2
I converted the hexadecimal numbers to their corresponding ascii values.
It decodes to `3{ju57_`.

### enc3
I base64 decoded the string.
It decodes to `d1ff3r3n7_3nc`.

### enc4
It took me a while to figure out that these numbers are actually octal. So I cconverted them to their corresponding ascii values.
It decodes to `0d1n65_l0l}`

## Flag
CSOC23{ju57_d1ff3r3n7_3nc0d1n65_l0l}
