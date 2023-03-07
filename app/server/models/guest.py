from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class GuestSchema(BaseModel):
    name: str = Field(...)
    number_of_guests: int = Field(..., gt=0, lt=3)
    hotel_room: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "name": "Mads Madsen",
                "number_of_guests": "2",
                "hotel_room": "ja"
            }
        }


class UpdateGuestModel(BaseModel):
    fullname: Optional[str]
    number_of_guests: Optional[int]
    hotel_room: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "fullname": "John Doe",
                "number_of_guests": "1",
                "hotel_room": "nei"
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}