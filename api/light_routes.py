from typing import List

from fastapi import APIRouter
from services import light_service

from models.light import Light

light_router = APIRouter(prefix="/light")


@light_router.get("/get/all")
def get_lights() -> List[Light]:
    return light_service.get_lights()


@light_router.get("/get/device/{device_id}")
def get_light_for_device(device_id: int) -> Light:
    return light_service.get_light_for_device(device_id)
