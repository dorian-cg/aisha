from typing import List
from fastapi import APIRouter, HTTPException
from models.room import Room
from services import room_service

room_router = APIRouter(prefix="/room", tags=["Room Endpoints"])


@room_router.get("/all")
def get_rooms() -> List[Room]:
    return room_service.get_rooms()


@room_router.get("/get/id/{room_id}")
def get_room_by_id(room_id: str) -> Room:
    room = room_service.get_room_by_id(room_id)

    if not room:
        raise HTTPException(status_code=404)

    return room


@room_router.get("/get/name/{name}")
def get_room_by_name(name: str) -> Room:
    room = room_service.get_room_by_name(name)

    if not room:
        raise HTTPException(status_code=404)

    return room
