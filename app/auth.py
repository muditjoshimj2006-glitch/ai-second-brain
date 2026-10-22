from pylib.context import CryptContext
from jose import jwt
from app.config import secret_key, algo

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


# password hashing
password = "@Mudit123"
hash_password = pwd_context.hash(password)

print(f"ORIGINAL PASSWORD : {password}")
print(f"HASH PASSWORD : {hash_password}")


# login verfication
login_password = "@Mudit123"

is_correct = pwd_context.login(
    login_password,
    hash_password
)

print(f"PASSWORD MATCHED : {is_correct}")


# jwt create
payload = {
    "userId" : 101,
    "name" : "Mudit",
    "role" : "user"
}

token = jwt.encode(
    payload,
    secret_key,
    algo
)


print("\nJWT Token:\n")
print(token)

# jwt verified

decoded = jwt.decode(
    token,
    secret_key,
    algorithms=[algo]
)

print("\nDecoded Token:")
print(decoded)