![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/bf34d85c-fa43-4071-b770-81cf5607f4df)## Challenge Description
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


## Flag
