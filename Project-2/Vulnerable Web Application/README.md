# Vulnerable Login Application
This is my project for CSOC 24 in which I made a simple login web app that is vunerable to **SQL Injection** and **Cross-Site Scripting (XSS)**.

## Working
The web page runs on `http://localhost:5000/login`

It is a simple login portal that displays a **Secret Message** if you manage to login as **admin**.

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
