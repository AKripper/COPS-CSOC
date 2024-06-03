## Challenge Description
Ron just found his own copy of advanced potion making, but its been corrupted by some kind of spell. Help him recover it!

[advanced-potion-making](advanced-potion-making)

## Writeup

I started by checking the file type and metadata but found nothing out of it. So my next step was to check the hexdump of the image. The hexdump appeared to be that of a PNG file
so I compared the image to an actual PNG image and modified the corrupted bits.

![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/31a40b79-e2cc-4e46-965d-8871b4d2b7b5)

After modification and renaming the file by adding file extension `.png` I got a blank [image](advanced-potion-making.png)

## Flag
