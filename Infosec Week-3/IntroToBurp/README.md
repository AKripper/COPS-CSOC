## Challenge Description

## Writeup
The Website requires us to register and then submit an `OTP` to continue. So I opened the site on [Burp Suite](https://portswigger.net/burp) as teh challenge name hints us to use it.

I then submitted test values for registering in the website:

![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/19c0be6c-5cf1-4f32-8a85-78e9c3db0134)

We see that the Request Header `otp` has the test value that I submitted.

![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/b168c535-1ea3-41a2-ad2b-20b04ad130e7)

I thought removing this header might help us bypass the OTP Request and it indeed worked.

![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/29caaa25-54f7-45e6-be68-6031ba9bbe54)

We thus get our flag.

## Flag
picoCTF{#0TP_Bypvss_SuCc3$S_2e80f1fd}
