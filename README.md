# Policy Compliant Password Generator
Simple password generator to comply with certain policies on password.

## Instructions to setup:
1. Create a secret in `/etc/secret_key.txt`. This should be a sufficiently long string.
2. Run `gunicorn` web server using `gunicorn password_generator.wsgi` in the password_generator-project subfolder.