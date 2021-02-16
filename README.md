# Policy Compliant Password Generator
Simple password generator to comply with certain policies on password.

![Screenshot 2](/screenshot-2.png "Screenshot 2")
![Screenshot 1](/screenshot-1.png "Screenshot 1")

## Instructions to setup:
1. Export a secret key as an environment variable `export SECRET_KEY=$(secret_key)`. This should be a sufficiently long string.
2. Run `gunicorn` web server using `gunicorn password_generator.wsgi` in the password_generator-project subfolder.

Check it out [here](https://damp-cliffs-72839.herokuapp.com/).
