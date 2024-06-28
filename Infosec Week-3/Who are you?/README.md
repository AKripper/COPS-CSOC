## Challenge Description
Let me in. Let me iiiiiiinnnnnnnnnnnnnnnnnnnn 

http://mercury.picoctf.net:39114/

## Writeup
The website did not have much for us so I opened it in Burp Suite.
Now the text says, "Only people who use the official PicoBrowser are allowed on this site!"


So I changed the Request Header `User-Agent` to `PicoBrowser`. This is what it showed me.
![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/1c87aa3a-0f07-4c24-a61c-1f521be5ae16)

Now I searced for the request header that fits this. I found out this [site](https://datatracker.ietf.org/doc/html/rfc2616#section-5.3).
`Referer` Request fits our requirements. So now I added a Request Header named `Referer` to `mercury.picoctf.net:39114`
![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/7efccde3-2e46-4779-9efb-acc04f36c0b5)

Now I searcehd for a `Date` Header on this [site](https://www.geeksforgeeks.org/http-headers-date/). So I added the `Date` header with the year `2018`.
![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/f139dd6e-58e3-44f9-be3e-f9c0d667f6d2)

Now to Stop tracking we need to add the `DNT`(Do Not Track) header with value `1`.
![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/1d84bf4c-f42f-4395-8380-0360d38955f6)

Fo this we need to restrict the website to those with the ip address of Sweden. For this I used the `X-Forwarded-For` Request with value `103.81.143.0`, i.e a random ip address from Sweden.
![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/935aa11e-7a7b-4668-b297-906c33661892)

For this we have to change the `Accept-Language` header to `sv-SE` which stands for Swedish.
![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/bf0429ec-f823-4c31-870e-7c06f57e6c43)

This gives us our flag.
## Flag
picoCTF{http_h34d3rs_v3ry_c0Ol_much_w0w_20ace0e4}
