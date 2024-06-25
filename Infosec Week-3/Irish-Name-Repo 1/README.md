## Challenge Description
There is a website running at https://jupiter.challenges.picoctf.org/problem/50009/ or http://jupiter.challenges.picoctf.org:50009. 
Do you think you can log us in? Try to see if you can login!

## Writeup
I started by wondering around the website and then on the side panel I found the admin login page.

![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/9c5b9889-c045-4d85-9287-ec1088d29ed3)

Admin login page required me to write the username and password. I tired the following credentials:
- username : **admin**
- password : **admin**

This gave a login failed message

![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/51f0b3ed-75ca-4ab4-8c0e-c496aa0ad01d)

Now I the credentials to be stored in an SQLite database. The basic query for this looks like this:

- SELECT username, password FROM users WHERE username='USERNAME' AND password='PASSWORD'

So I would want is such that the query ignores the password I type and directly redirect me to the admin portal. This can work if I comment out the part of the query that comes after username

This is how the query will look like:
- SELECT username, password FROM users WHERE username='USERNAME';--' AND password='PASSWORD'

## Flag
picoCTF{s0m3_SQL_fb3fe2ad}
