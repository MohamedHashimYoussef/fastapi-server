from pydantic import BaseModel , Field , EmailStr



class UserIn(BaseModel):
    email : EmailStr = Field(... , title='Email'  , description='**Email** must be an Email')
    username : str = Field(... , title='Username' , example='mohamedhashem' , description='**Username** must be greater than 3 ' , min_length=3 , max_length=30)
    password : str = Field(... , title='Password' , example='********' , description='**Password** must be greater than 8' , min_length=8 , max_length=50)



