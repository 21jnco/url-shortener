from pydantic import BaseModel, Field, EmailStr


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"