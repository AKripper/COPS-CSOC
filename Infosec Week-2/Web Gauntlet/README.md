## Challenge Description
Can you beat the filters? Log in as admin 
[http://jupiter.challenges.picoctf.org:44979/](http://jupiter.challenges.picoctf.org:44979/)
[http://jupiter.challenges.picoctf.org:44979/filter.php](http://jupiter.challenges.picoctf.org:44979/filter.php)


## Writeup
The link provided opens a login page that requires us to enter a username and password. Now for starting I tried the username and password as `admin` and `admin`. It displays an invalid username/password message along with a text in the background saying:

**SELECT * FROM users WHERE username='admin' AND password='admin'**

![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/bce2eee5-1848-4492-8c7b-53d82c479215)

This looks like an SQL Query. So we might need to use an SQL injection for this. 

Also in the filters page we see the only filter is `or`, so we have to avoid using it in our SQL injection.

### Round 1 (Filter : or)
I tried using the most basic SQL injection technique that is commenting out the part of the query that asks for the password, i.e, make the query look like this:

- SELECT * FROM users WHERE username='**admin';--**' AND password='admin'

I inserted `';` after `admin` to end the statement and then `--` comments out the rest of the statement. So to be able to do this we have to write our username as `admin';--`. This helps us enter Round 2.
- **Username:** 'admin';--'

### Round 2 (Filter : or and like = --)
For this round we have more filters including the comment(--) parameter we had used in the previous round. So we might need to find some other ways to comment out the text. For this I did some research and found out this [cheatsheet](https://www.sisense.com/blog/sql-symbol-cheatsheet/). I scrolled over to find this.

![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/dbf80918-85a9-4f58-82cf-5192850ab38e)

Clearly we can use `#` for inline comments. So we can update our new username accordingly.
- **Username:** 'admin';#'

### Round 3 (Filter : or and = like > < --)
We see that our previous username can still be used and nothing has been filtered out here.
- **Username:** 'admin';#'

### Round 4 (Filter : or and = like > < -- admin)
Now `admin` word has been filtered so we cannot use it in our SQL query. So for this problem I had two things in mind:
1. To convert ASCII numbers letter by letter to form the word `admin`.

## Flag

