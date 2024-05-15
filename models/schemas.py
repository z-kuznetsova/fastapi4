from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str

class UserUpdate(BaseModel):
    name: str
    email: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str

class TaskCreateWithOwner(BaseModel):
    title: str
    description: str
    owner_id: int

class TaskUpdate(BaseModel):
    title: str
    description: str

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    owner_id: int