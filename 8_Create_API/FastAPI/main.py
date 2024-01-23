from fastapi import FastAPI, HTTPException
from typing import List
from uuid import uuid4, UUID

from modules import User, Gender, Role, UserUpdate


app = FastAPI()

db:List[User] = [
    User(
        id = uuid4(),
        first_name = 'Dias',
        last_name= 'Muratbaev',
        gender = Gender.male,
        roles = [Role.student]
    ),
    User(
        id = uuid4(),
        first_name = 'Matiu',
        last_name= 'Makkonahi',
        gender = Gender.male,
        roles = [Role.admin, Role.user]
    )
]
@app.get('/')
async def root():
    return {"Hello":"World"}


@app.get('/api/v1/users')
async def fetchall_user():
    return db


@app.post('/api/v1/users')
async def createUser(user:User):
    db.append(user)
    return {'id: ': user.id, 'name: ':  user.first_name}



@app.put('/api/v1/users/{user_id}')
async def update_user(user_id: UUID, user: UserUpdate):
    for existing_user in db:
        if existing_user.id == user_id:
            if user.first_name is not None:
                existing_user.first_name = user.first_name
            if user.last_name is not None:
                existing_user.last_name = user.last_name
            if user.gender is not None:
                existing_user.gender = user.gender
            if user.roles is not None:
                existing_user.roles = user.roles
            return {"message": "User updated successfully"}
    raise HTTPException(
        status_code=404,
        detail=f'User with id {user_id} not found'
    )



@app.delete('/api/v1/users/{user_id}')
async def deleteUser(user_id:UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return 
    raise HTTPException(
        status_code = 404,
        detail = f'User with id {user_id} not found.'
    )