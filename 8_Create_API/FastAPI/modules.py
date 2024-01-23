from typing import Optional, List, Union
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum


class Gender(str, Enum):
    male = 'male'
    female = 'female'


class Role(str, Enum):
    admin = 'admin'
    user = 'user'
    student = 'student'


class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: Optional[str]
    last_name: Optional[str]
    gender: Optional[Gender]
    roles: Optional[List[Role]]


class UserUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    gender: Optional[Gender] = None
    roles: Optional[List[Role]] = None
