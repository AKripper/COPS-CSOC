## Challenge Description
This image passes LSB statistical analysis, but we can't help but think there must be something to the visual artifacts present in this image...

Download the image [here](Ninja-and-Prince-Genji-Ukiyoe-Utagawa-Kunisada.flag.png)

## Writeup
Looking at the image, it looked like an MSB encoded image as such images can couse changes in the actual colour of the original image. Lsb images on the other hand look almost alike the original image as chaning the Least significan bit can cause less significant changes in teh image.

So now I looked up in the internet on how to extract MSB from an image and found out a wonderful tool do do my job.

I used Stegsolve to open the image, went to analyse and data extract.

![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/d7f30fd4-843c-42b4-9db7-7e565b1bc6ee)

Selecting the bitplanes and then clicking preview displays the following text.

![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/30730518-5cd9-4129-8be0-da1af28f0a6e)

I copied the text to my notepad and searched for the flag format 'pico'.

And boom...I found the whole flag within the text

![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/16eba166-04c7-4386-afc9-a60935053015)

## Flag
picoCTF{15_y0ur_que57_qu1x071c_0r_h3r01c_b5e03bc5}
