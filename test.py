import re

user = "apmihal"

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")

def valid_username(username):
    return USER_RE.match(username)

if valid_username(user):
    print("that works!")
else:
    print("try again")
