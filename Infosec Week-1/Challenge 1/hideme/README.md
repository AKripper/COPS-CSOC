## Challenge Description
Every file gets a flag.

The SOC analyst saw one image been sent back and forth between two people. They decided to investigate and found out that there was more than what meets the eye [here](flag.png).

## Writeup
I started with checking the metadata of the file using exiftool. 

![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/b8973320-891e-442f-bb33-c7ae030b7955)

So I checked the hexdump of the image and it did contain some text after the 'IEND' chunk. But I couldn't make anything out of it so I binwalked the file and found something.

![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/a8f661d6-e170-42bc-a656-f9aa2ce2eb21)

The secret folder is of our interest and it did contain another flag.png that gave us our flag.

![flag](https://github.com/AKripper/COPS-CSOC/assets/167231621/7bf81cef-b1ae-4b15-bbfd-dfdb9ab1ef01)

## Flag
picoCTF{Hiddinng_An_imag3_within_@n_ima9e_cda72af0}
