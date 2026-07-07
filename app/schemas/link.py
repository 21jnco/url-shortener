from pydantic import BaseModel, HttpUrl
from datetime import datetime


class LinkCreate(BaseModel):
    long_url: HttpUrl


class LinkResponse(BaseModel):
    id: int
    long_url: str
    short_code: str
    click_count: int
    created_at: datetime

    model_config = { 
        'from_attributes': True
    }
