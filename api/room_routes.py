from typing import List
from fastapi import APIRouter
from services import room_service
from models.room import Room

room_router = APIRouter(prefix="/room")


@room_router.get("/get/all")
def get_rooms() -> List[Room]:
    return room_service.get_rooms()


@room_router.get("/get/id/{room_id}")
def get_room_by_id(room_id: str) -> Room:
    return room_service.get_room_by_id(room_id)


@room_router.get("/get/name/{name}")
def get_room_by_name(name: str) -> Room:
    return room_service.get_room_by_name(name)
