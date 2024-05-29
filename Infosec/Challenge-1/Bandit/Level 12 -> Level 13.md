# Writeup
When we open the `data.txt` file, we see a hexdump. We see that the first 2 bytes of the file are 1f, 8b. This got me into some research where i learnt that files compressed in different methods have different magic numbers.

For this challenge I learnt that the magic number of some compressions are as follows:
1. *gzip* - 1f8b 
2. *bunzip2 - 425a

And thats all there is to this challenge.
After a series of decompressing the .gz and .bz2 files we come to a stage where the file is neither .gz or .bz2

![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/52e410ef-c600-4876-b99b-16e922b68b60)

Here we see that a part of the hexdump is of .gz type. So I just copied the following part in a new file and decompressed it alone, and that worked.
On the next step we get a similar hexdump but now part of the hexdump is .bz2 type so we folllow the same steps.

Finally after this last decompression we get our password.

![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/6b5e68f4-29cd-4bb9-a054-4f9eeec435b4)

## Password
wbWdlBxEir4CaE8LaPhauuOo6pwRmrDw
