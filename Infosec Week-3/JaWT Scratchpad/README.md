## Challenge Description
Check the admin scratchpad! https://jupiter.challenges.picoctf.org/problem/58210/

## Writeup
The challenge requires us to login to the admin scratchpadd but does not let us login by simply entering 'admin' as the username. This is what we see if we type 'admin'.
![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/01f13b5b-3171-4b2c-947e-cab7afb90ecc)

The webpage provides us with two links within it:
- [JWT](https://jwt.io)
- [John](https://github.com/openwall/john)


Now if I type in my name as 'notadmin' I am redirected to an empty scratchpad.
![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/21654868-2667-4890-b087-189d27813239)

I looked at the cookies of this page and found out this `jwt` cookie:
![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/3d19a9ee-a633-46de-937e-51874ef575d1)

I pasted this cookie in the JWT website we were provided with and this is what I got
![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/58ba01b9-54f1-4cfa-be43-598998f43f1d)

Clearly this cookie decides the scratchpad of the user. All we have to do is change the name to `admin` and verify the signature using the password.
For finding the password we will need [John the Ripper](https://github.com/openwall/john). I installed it on my linux subsystem.

I used John the Ripper to get the password for the JWT token using this simple code:

`john jawt.txt --wordlist=../Wordlists/rockyou.txt --format=HMAC-SHA256`

The `jawt.txt` file contains the token and I used the publically available `rockyou.txt` password list using the format `HS256`.
![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/e2ffb8da-f8a4-4ca4-b438-9a7a2e89ad5f)

Now I wen tback to the JWT site and changed the `user` to `admin` and verified the signature by putting the secret as `ilovepico`
![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/e5d3b36a-cdb5-4826-8e86-49773eab8168)

Now editing the cookie value and pasting this new cookie we get our flag on the website:
![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/288f3e0d-0875-410b-b0f5-79521ccece85)


## Flag
picoCTF{jawt_was_just_what_you_thought_44c752f5}
