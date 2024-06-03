## Challenge Description
We found this [file](tunn3l_v1s10n). Recover the flag.

## Writeup
I started with checking metadata of the file using exiftool. I found out that it was an image file with `.bmp` file extension. I tried opening it but it does not open. So I checked the hexdump of the file and found this.

![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/b72b8a12-dd7c-4be4-a5de-51919b91fef6)

To correct this I looked for a [sample bmp image](https://filesamples.com/formats/bmp) and compared the hexdump of both the images.

![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/a3b31945-cb56-4ca8-8083-d6d1232967a5)

After correcting the the hex values I also added the `.bmp` extension by renaming the file.

Opening the image gives a false flag.

![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/4b272c34-6d68-4903-8074-b8c1507ef2d2)

...this is rather reassuring as we are on the right track.

Now I noticed that the image dimensions are somewhat not right...so I looked up how to change image dimensions.

![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/a44f3718-9f0a-439f-9825-8a7f18732b48)

Image dimensions are stored within the hexdump of the image and here it represents (width x hieght) as 46Ex132. So I chenged it to 46Ex350 and we get our flag after opening the image.

![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/91d41f2c-a72d-42c6-b2b6-fd2bbbb43061)


## Flag
picoCTF{qu1t3_a_v13w_2020}
