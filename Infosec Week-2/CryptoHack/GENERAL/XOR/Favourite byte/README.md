## Challenge Description
For the next few challenges, you'll use what you've just learned to solve some more XOR puzzles.

I've hidden some data using XOR with a single byte, but that byte is a secret. Don't forget to decode from hex first.

`73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d`

## Writeup
First I converted the hexadecimal string to bytes and printed it. It looked like the flag has been xored with some quantity which is most likely constant. So I ran a program that xors the string with numbers til 100. And I found the flag at 16, meaning the flag was xored with the number 16.

This [script](fav.py) demonstrates this.

## Flag
crypto{0x10_15_my_f4v0ur173_by7e}
