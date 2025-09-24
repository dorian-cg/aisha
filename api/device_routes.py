from typing import List
from fastapi import APIRouter
from models.device import Device
from services import device_service

device_router = APIRouter(prefix="/device")


@device_router.get("/get/all")
def get_devices() -> List[Device]:
    return device_service.get_devices()


@device_router.get("/get/room/{room_id}")
def get_devices_for_room(room_id: str) -> List[Device]:
    return device_service.get_devices_for_room(room_id)


@device_router.get("/get/id/{device_id}")
def get_device_by_id(device_id: str) -> Device:
    return device_service.get_device_by_id(device_id)


@device_router.get("/get/name/{name}")
def get_device_by_name(name: str) -> Device:
    return device_service.get_device_by_name(name)
