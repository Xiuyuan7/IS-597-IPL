import helpers
import secrets

while True:
    username = input("username: ")
    password = input("password: ")
    if helpers.start(username, password):
        break
