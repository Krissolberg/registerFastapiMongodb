import motor.motor_asyncio
from bson.objectid import ObjectId
from decouple import config

MONGO_DETAILS = config("MONGO_DETAILS")  # read environment variable

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.guests

guest_collection = database.get_collection("guests_collection")

# helpers


def guest_helper(guest) -> dict:
    return {
        "id": str(guest["_id"]),
        "name": guest["name"],
        "number_of_guests": guest["number_of_guests"],
        "hotel_room": guest["hotel_room"]
    }


# Retrieve all guests present in the database
async def retrieve_guests():
    guests = []
    async for guest in guest_collection.find():
        guests.append(guest_helper(guest))
    return guests


# Add a new guest into to the database
async def add_guest(guest_data: dict) -> dict:
    guest = await guest_collection.insert_one(guest_data)
    new_guest = await guest_collection.find_one({"_id": guest.inserted_id})
    return guest_helper(new_guest)


# Retrieve a guest with a matching ID
async def retrieve_guest(id: str) -> dict:
    guest = await guest_collection.find_one({"_id": ObjectId(id)})
    if guest:
        return guest_helper(guest)


# Update a guest with a matching ID
async def update_guest(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    guest = await guest_collection.find_one({"_id": ObjectId(id)})
    if guest:
        updated_guest = await guest_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_guest:
            return True
        return False


# Delete a guest from the database
async def delete_guest(id: str):
    guest = await guest_collection.find_one({"_id": ObjectId(id)})
    if guest:
        await guest_collection.delete_one({"_id": ObjectId(id)})
        return True