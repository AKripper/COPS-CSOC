## Challenge Description
Last time, I promise! Only 25 characters this time. Log in as admin 

Site: [http://mercury.picoctf.net:29772/](http://mercury.picoctf.net:29772/)

Filter: [http://mercury.picoctf.net:29772/filter.php](http://mercury.picoctf.net:29772/filter.php)

## Writeup
This time there is a charecter limit to the username and password.

Given the filters are: or and true false union like = > < ; -- /* */ admin

Clearly the filters are the same as before. For the previous challenge (Web Gauntlet 2) I used the following credentials:
- Username : **ad' || 'min**    (11 characters)
- Password : **1' IS NOT '2**   (12 characters)

As the character limit has not been reached yet. I tried the same credentials for this challenge and it did work.

![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/dda9fa0d-978b-4ab8-86d5-68d77a536217)

For more explanation on how I got the username and password look up at my writup for [Web Gauntlet 2](https://github.com/AKripper/COPS-CSOC/tree/main/Infosec%20Week-3/Web%20Gauntlet%202)

## Flag
picoCTF{k3ep_1t_sh0rt_30593712914d76105748604617f4006a}
