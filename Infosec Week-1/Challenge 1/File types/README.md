## Challenge Description
This file was found among some files marked confidential but my pdf reader cannot read it, maybe yours can.
You can download the file from [here](Flag.pdf).

## Writeup
I checked the file type and found out that the given file is not a pdf file but an sh script.

![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/51a09f7d-4e12-45e0-bc58-2674cd9aff80)

Above is part of the script. So I followed what the script said and typed `sh Flag.pdf`.

When I first ran the command I got this error.
![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/f825f587-84fc-46c3-8d3d-a3e7f4a11614)

I then found out that this error was because I did no have 'sharutils' installed on my system. So after installing and running the command, I got this.
![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/49fdb2c5-bd96-4a1d-9644-2ac7f9bf679b)

This is the start of a series of file types that are needed to be decompressed. Given below is the order of decompression of the flag and the syntax used.
1. `ar`-` ar x flag`
2. `bzip2`-`binwalk -e flag`
3. `bzip2`-`binwalk -e flag`
4. `gzip`-`binwalk -e 20`
5. `gzip`-`binwalk -e flag.gz`
6. `gzip`-`binwalk -e flag.gz`
7. `lzip`-`lzip -d flag`
8. `lz4`-`flag.out flag`
9. `lzma`-`xz -d flag.xz`
10. `lzop`-`lzop -d flag.lzo`
11. `lzip`-`lzip -d flag`
12. `xz`-`xz -d falg.xz`
13. `flag` 

This `flag.txt` contains a hexadecimal string which we can convert using `cat flag | xxd -r -p`

## Flag
picoCTF{f1len@m3_m@n1pul@t10n_f0r_0b2cur17y_3c79c5ba}
