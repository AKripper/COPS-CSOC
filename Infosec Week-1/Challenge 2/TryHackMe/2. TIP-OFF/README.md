## Backgroud
The OSINT Dojo recently found themselves the victim of a cyber attack. It seems that there is no major damage, and there does not appear to be any other significant indicators of compromise on any of our systems. However during forensic analysis our admins found an image left behind by the cybercriminals. Perhaps it contains some clues that could allow us to determine who the attackers were? 

We've copied the image left by the attacker, you can view it in your browser [here](https://raw.githubusercontent.com/OsintDojo/public/3f178408909bc1aae7ea2f51126984a8813b0901/sakurapwnedletter.svg).

## Question
1. What username does the attacker go by?

## Writeup

I downloaded the image and checked the metadata of the image using exiftool.

![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/1c45f21d-d5e3-4096-b9ff-79d1d84ec876)

The path of the image shows the image was uploaded by 'SakuraSnowAngelAiko' from her Desktop folder. 

## Answer
1. SakuraSnowAngelAiko
