## Challenge Description
There is a website running at https://jupiter.challenges.picoctf.org/problem/53751/ (link).
Someone has bypassed the login before, and now it's being strengthened. Try to see if you can still login!

## Writeup
I went to the website and it was just like the first challenge. So I went to the admin login portal. This again seems to be an SQL injection challenge so I tried out some techniques.

I started by putting the credentials:
- username : admin
- password : admin

And it gave a login error. Now I tried this SQL injection:
- username : admin';--
- password : (anything)

And surprisingly it worked. 


Thus the challenge is solved. For more information on the thought process and resources look up at my writeup on [Irish-Name-Repo 1](https://github.com/AKripper/COPS-CSOC/tree/main/Infosec%20Week-3/Irish-Name-Repo%201)

## Flag
 picoCTF{m0R3_SQL_plz_c34df170}
