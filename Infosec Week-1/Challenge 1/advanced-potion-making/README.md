## Challenge Description
Ron just found his own copy of advanced potion making, but its been corrupted by some kind of spell. Help him recover it!

[advanced-potion-making](advanced-potion-making)

## Writeup

I started by checking the file type and metadata but found nothing out of it. So my next step was to check the hexdump of the image. The hexdump appeared to be that of a PNG file
so I compared the image to an actual PNG image and modified the corrupted bits.

![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/31a40b79-e2cc-4e46-965d-8871b4d2b7b5)

After modification and renaming the file by adding file extension `.png` I got a blank [image](advanced-potion-making.png)

Now because this is a blank image I decided to open it on MS Paint. Here I filled the background black and this is what I found.
![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/f8b4c1d8-c5ff-4311-bb6f-15878ec13e47)

We found our flag.

## Flag
picoCTF{w1z4rdry}
