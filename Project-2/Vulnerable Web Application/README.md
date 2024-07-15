![image](https://github.com/user-attachments/assets/a20f17c8-f478-48d8-935a-00b58f5b9cb7)![image](https://github.com/user-attachments/assets/245f954d-988d-4b94-b465-8531ccd832f2)# Vulnerable Login Application
This is my project for CSOC 24 in which I made a simple login web app that is vunerable to **SQL Injection**.

## Working
The web page runs on `http://localhost:5000/login`

It is a simple login portal that displays a **Secret Message**(A random compliment) if you manage to login as **admin**.

This is what the login page looks like:

![image](https://github.com/user-attachments/assets/7ad813c9-f058-42ef-b31b-a921dd3e0aec)

Now we may enter the web page if we know the username and password, i.e:
- Username: **admin**
- Password: **password123**

![image](https://github.com/user-attachments/assets/7c7c8557-7b3a-4811-897a-7162165066f0)

But, we can also enter the webpage through an **SQL Injection**:
- Username: **' or 1=1;--**
- Password: **anything**

![image](https://github.com/user-attachments/assets/d2ed4b64-4110-44eb-bf98-9145f23658e5)


## Set Up
This is the structure of the directory.
```
simple_login_app/
    ├── app.py
    ├── requirements.txt
    ├── Dockerfile
    ├── docker-compose.yml
    ├── templates/
    │   ├── login.html
    │   └── home.html
    └── static/
```

After having all the files you will simply need to run these commands on the terminal inside the directory `simple_login_app`.
```
docker-compose build
docker-compose up
```
This builds and runs the web app.

## Files
1. **app.py** - The Python script to create the Flask web application.

2. **requirements.txt** - Contains the dependencies for the Flask application.

3. **Dockerfile** - Defines the Docker image and how to build it.

4. **docker-compose.yml** - Defines the Docker services for the application.

5. **login.html** - Contains the HTML code for the login page.

6. **home.html** - Contains the HTML code for the home page.

##
