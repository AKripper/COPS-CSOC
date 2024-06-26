## Challenge Description
There is a secure website running at https://jupiter.challenges.picoctf.org/problem/40742/. Try to see if you can login as admin!

## Writeup
I started by going to the login portal inside in the website.

This time the login portal asks for only the password.

![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/451f2df1-8a03-453d-acb0-c261711c2025)

So I browsed on the web for some basic [SQL injections](https://en.wikipedia.org/wiki/SQL_injection).

![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/34a15984-bbee-4f96-a7b2-537d06801759)

Setting the password parameter as true may work out well for us, so I will be filling the following credentials:
- password : **' OR '1'='1**

Entering this gives us the following error

![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/8237d2b9-c6cf-48b8-82dc-bb237556ff77)

To overcome this I checked the source code for the website. There I found out something.

![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/967abf68-2de0-4ace-9960-f94368fc949c)

I set the `debug` parameter value to `1` and tried submitting the password again, and this time it showed this message

![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/4c88aee9-ac6e-41bc-8a9b-1e82c5bcdeab)

So now I filled the password as **' BE '1'='1**. This time it displayed the flag.
![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/e3644eb6-0936-4652-aa17-bfd95236b6e9)

We have thus solved our challenge.

## Flag
picoCTF{3v3n_m0r3_SQL_4424e7af}
