## Background
It appears that our attacker made a fatal mistake in their operational security. They seem to have reused their username across other social media platforms as well. This should make it far easier for us to gather additional information on them by locating their other social media accounts. 

## Questions
1. What is the full email address used by the attacker?
2. What is the attacker's full real name?

## Writeup

I searched the username directly of google and found a github account with the same username. After a bit of wandering around I found a PGP folder with a public key inside it
I base64 decoded the public key and extracted all the strings from it and it had the email address hidden among it.

![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/539cae5e-472a-4013-ad7c-a678046fd000)

Now I had to search the real name so for that I typed the username on google again and scrolled a bit down when I found this.

![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/21077b51-5421-433a-8666-ad7f45002295)

So I gave this name a try and it did work.

## Answers
1. SakuraSnowAngel83@protonmail.com
2. Aiko Abe
