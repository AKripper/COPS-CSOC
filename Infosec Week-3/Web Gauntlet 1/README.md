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

Clearly we can use `#` for inline comments. Now our query looks like this:
 SELECT * FROM users WHERE username='**admin';#**' AND password='admin'


So we can update our new username accordingly.
- **Username:** 'admin';#'

### Round 3 (Filter : or and = like > < --)
We see that our previous username can still be used and nothing has been filtered out here.
- **Username:** 'admin';#'

### Round 4 (Filter : or and = like > < -- admin)
Now `admin` word has been filtered so we cannot use it in our SQL query. So for this problem I had decided to concencate two words like `adm` and `in` to form `admin`. Now I found out a way to concatenate strings in the [cheatsheet](https://www.sisense.com/blog/sql-symbol-cheatsheet/).

![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/c54ab6a8-4993-4524-9500-6f3006d9b00c)

So our query must look like this:
- SELECT * FROM users WHERE username='**adm'||'in';#**' AND password='admin'

So the username becomes:
- **Username:** 'adm'||'in';#'

### Round 5 (Filter : or and = like > < -- union admin)
This time a new word `union` has been filtered out but since we did not use it in the previous round so we can use the same username as before to go to the next round.

( The previous round could have been solved using the UNION statement. The UNION operator is used to combine the results of two or more SELECT statements into a single result set )

- **Username:** 'adm'||'in';#'

---
Now  going back to the 'filter.php' webpage we can find the source code for the login, and scrolling down we get the flag.

![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/13e1241a-5696-4667-b964-d766b7188d96)

## Flag
picoCTF{y0u_m4d3_1t_16f769e719ab9d3e310fd13dc1262ee1}
