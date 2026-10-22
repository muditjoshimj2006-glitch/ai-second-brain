from pydantic import BaseModel

 
# Register User
class UserCreate(BaseModel):
    name: str
    email: str
    password: str



# Login User
class UserLogin(BaseModel):
    email: str
    password: str


# create Note
class NoteCreate(BaseModel):
    title: str