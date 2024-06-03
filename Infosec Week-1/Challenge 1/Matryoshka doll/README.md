## Challenge Description
Matryoshka dolls are a set of wooden dolls of decreasing size placed one inside another. What's the final one? Image: [this](dolls.jpg)

## Writeup
I started with checking the metadata of the image but dindn't manage to get anything out of it so I looked at the challenge description again. It then clicked to me that there could be files inside the image that needed to be extracted. So I used the command `binwalk -e dolls.jpg` for this purpose.

Extracting [dolls.jpg](dolls.jpg) gave another image [2_c.jpg](2_c.jpg) which on extracting gave image [3_c.jpg](3_c.jpg) which again on extracting gave [4_c.jpg](4_c.jpg) which on extracting finally gives our flag.

## Flag
picoCTF{ac0072c423ee13bfc0b166af72e25b61}
