## Challenge Description
Files can always be changed in a secret way. Can you find the flag? 

[cat.jpg](cat.jpg)

## Writeup
I started by checking the metadata of the image using exiftool. There the licence looked a bit suspicious.

![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/ec0a740d-10c1-4b8f-a276-cfc2b901e04f)

So I just base64 decoded the string using the command:

`echo "cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9" | base64 -d` 

and boom we get our flag.

## Flag
picoCTF{the_m3tadata_1s_modified}
