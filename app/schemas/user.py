from pydantic import BaseModel, Field, EmailStr


class UserCreate(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    email: EmailStr = Field(max_length=255)
    password: str = Field(min_length=8, max_length=255)


class UserEmailUpdate(BaseModel):
    email: EmailStr


class UserPasswordUpdate(BaseModel):
    current_password: str = Field(min_length=8, max_length=255)
    password: str = Field(min_length=8, max_length=255)


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr

    model_config = {
        'from_attributes': True
    }
