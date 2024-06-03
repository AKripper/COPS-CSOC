## Challenge Description
I've hidden a flag in this file. Can you find it? Forensics is [fun.pptm](Forensics%20is%20fun.pptm)

## Writeup
`.pptm` file is a macro-enabled presentation file, i.e., it has an automated way of doing tasks is what I understood. I then checked the metadata of the file using exiftool and found something interesting.
![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/78ec9254-6cc5-404d-a26b-42e52d2f3196)

I tried opening it in Microsoft PowerPoint but found nothing useful. I then went forward to extract the file using binwalk. I then wandered about a bit an found file named 'hidden' inside the 'slideMasters' directory.

Opening the file was this text:`Z m x h Z z o g c G l j b 0 N U R n t E M W R f d V 9 r b j B 3 X 3 B w d H N f c l 9 6 M X A 1 f Q`

This was just a base64 encoded string of the flag.

## Flag
picoCTF{D1d_u_kn0w_ppts_r_z1p5}
