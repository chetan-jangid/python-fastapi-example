from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException

from models import Gender, Role, User

app = FastAPI()

db: List[User] = [
  User(
    id = "928271d5-e627-46c8-94f7-e4326d90ed82",
    first_name = "Rock",
    last_name = "Buster",
    gender = Gender.male,
    roles = [Role.student]
  ),
  User(
    id = "a5807b5a-df16-4911-95e5-0fb88f6d4a4c",
    first_name = "Alex",
    last_name = "Jones",
    gender = Gender.male,
    roles = [Role.admin, Role.user]
  )
]

@app.get("/")
def root():
  return {"hello": "world"}

@app.get("/api/v1/users")
async def fetch_users():
  return db

@app.post("/api/v1/users")
async def register_user(user: User):
  db.append(user)
  return {"id": user.id}

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
  for user in db:
    if user.id == user_id:
      db.remove(user)
      return
  raise HTTPException(
    status_code = 404,
    detail = f"user with id: {user_id} does not exists"
  )

