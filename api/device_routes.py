from typing import List
from fastapi import APIRouter, HTTPException
from models.device import Device
from services import device_service

device_router = APIRouter(prefix="/device", tags=["Device Endpoints"])


@device_router.get("/all")
def get_devices() -> List[Device]:
    return device_service.get_devices()


@device_router.get("/room/{room_id}")
def get_devices_for_room(room_id: str) -> List[Device]:
    return device_service.get_devices_for_room(room_id)


@device_router.get("/device/{device_id}")
def get_device_by_id(device_id: str) -> Device:
    device = device_service.get_device_by_id(device_id)

    if not device:
        raise HTTPException(status_code=404)

    return device


@device_router.get("/name/{name}")
def get_device_by_name(name: str) -> Device:
    device = device_service.get_device_by_name(name)

    if not device:
        raise HTTPException(status_code=404)

    return device
