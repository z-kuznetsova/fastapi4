from fastapi import FastAPI, APIRouter
from models.good import User, Task
from models.schemas import UserCreate, UserUpdate, UserResponse, TaskCreateWithOwner, TaskUpdate, TaskResponse
from db import create_db_connection

# Создаем основной объект FastAPI
app = FastAPI()

# Создаем объект APIRouter для работы с пользователями
router_users = APIRouter()
router_tasks = APIRouter()


# Создаем методы для работы с пользователями

@router_users.get("/")
def get_users():
    db = create_db_connection()
    users = db.query(User).all()
    return users


@router_users.get("/{user_id}")
def get_user(user_id: int):
    db = create_db_connection()
    user = db.query(User).get(user_id)
    return user


@router_users.post("/")
def create_user(user: UserCreate):
    db = create_db_connection()
    new_user = User(name=user.name, email=user.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router_users.put("/{user_id}")
def update_user(user_id: int, user: UserUpdate):
    db = create_db_connection()
    db.query(User).filter(User.id == user_id).update(user.dict())
    db.commit()
    return {"message": "User updated successfully"}


@router_users.delete("/{user_id}")
def delete_user(user_id: int):
    db = create_db_connection()
    db.query(User).filter(User.id == user_id).delete()
    db.commit()
    return {"message": "User deleted successfully"}


# Для модели `Task`:
@router_tasks.get("/")
def get_tasks():
    db = create_db_connection()
    tasks = db.query(Task).all()
    return tasks


@router_tasks.get("/{task_id}")
def get_task(task_id: int):
    db = create_db_connection()
    task = db.query(Task).get(task_id)
    return task


@router_tasks.post("/")
def create_task(task: TaskCreateWithOwner):
    db = create_db_connection()
    new_task = Task(title=task.title, description=task.description, owner_id=task.owner_id)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


@router_tasks.put("/{task_id}")
def update_task(task_id: int, task: TaskUpdate):
    db = create_db_connection()
    db.query(Task).filter(Task.id == task_id).update(task.dict())
    db.commit()
    return {"message": "Task updated successfully"}


@router_tasks.delete("/{task_id}")
def delete_task(task_id: int):
    db = create_db_connection()
    db.query(Task).filter(Task.id == task_id).delete()
    db.commit()
    return {"message": "Task deleted successfully"}


app.include_router(router_users, prefix="/users", tags=["Users"])
app.include_router(router_tasks, prefix="/tasks", tags=["Tasks"])

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000)