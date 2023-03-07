from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.server.database import (
    add_guest,
    delete_guest,
    retrieve_guest,
    retrieve_guests,
    update_guest,
)
from app.server.models.guest import (
    ErrorResponseModel,
    ResponseModel,
    GuestSchema,
    UpdateGuestModel,
)

router = APIRouter()

@router.post("/", response_description="guest data added into the database")
async def add_guest_data(guest: GuestSchema = Body(...)):
    guest = jsonable_encoder(guest)
    new_guest = await add_guest(guest)
    return ResponseModel(new_guest, "guest added successfully.")