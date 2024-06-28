## Challenge Description
Let me in. Let me iiiiiiinnnnnnnnnnnnnnnnnnnn 

http://mercury.picoctf.net:39114/

## Writeup
The website did not have much for us so I opened it in Burp Suite.
Now the text says, "Only people who use the official PicoBrowser are allowed on this site!"


So I changed the Request Header `User-Agent` to `PicoBrowser`. This is what it showed me.
![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/1c87aa3a-0f07-4c24-a61c-1f521be5ae16)

Now I searced for the request header that fits this. I found out this [site](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers#request_context).
`Referer` Request fits our requirements. So now I added a Request Header named `Referer` to `mercury.picoctf.net:39114`
![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/7efccde3-2e46-4779-9efb-acc04f36c0b5)



## Flag
