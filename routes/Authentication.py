from fastapi import APIRouter
from schemas.User import UserIn
router = APIRouter()


@router.post('/login')
def Login():
    pass

@router.post('/register' , description='Add new User' , name='Register New User')
def Register(User:UserIn):

    return User


@router.post('/logout')
def Logout():
    pass