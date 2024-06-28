## Challenge Description
We have several pages hidden. Can you find the one with the flag?

Additional details will be available after launching your challenge instance.

## Writeup
We see the website has nothing much for us. I then went to see the source code it had a suspicious looking link in it.
![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/1e68cd0d-5074-46cb-adb3-92fda524cd08)

The link in my instance looked like this:
- `http://saturn.picoctf.net:51148`


Now I redirected this by adding `/secret/` at the end of the link:
- `http://saturn.picoctf.net:51148/secret`


Now viewing the source code for this webpage, we see this:
![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/51260b8a-f7a6-4b62-8004-e87ff3017106)

So I redirected the link again by adding `/hidden/` at the end:
- `http://saturn.picoctf.net:51148/secret/hidden/`


Again looking at the source code for this link
![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/7955967a-b779-41ea-be0d-f8c100142f07)

So I redirected the link by adding `/superhidden/` at the end:
- `http://saturn.picoctf.net:51148/secret/hidden/superhidden/`

The source code for this website contains the required flag.
![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/0680c441-39b6-4641-9a54-20c05c0c09bd)


## Flag
picoCTF{succ3ss_@h3n1c@10n_39849bcf}
