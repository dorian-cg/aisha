from typing import List
from fastapi import APIRouter, HTTPException, Response
from models.light import Light
from services import light_service

light_router = APIRouter(prefix="/light", tags=["Light Endpoints"])


@light_router.get("/all")
def get_lights() -> List[Light]:
    return light_service.get_lights()


@light_router.get("/{device_id}")
def get_light_for_device(device_id: str) -> Light:
    light = light_service.get_light_for_device(device_id)

    if not light:
        raise HTTPException(status_code=404)

    return light


@light_router.patch("/{device_id}/turn_on")
def turn_light_on(device_id: str):
    if not light_service.get_light_for_device(device_id):
        raise HTTPException(status_code=404)

    light_service.turn_light_on(device_id)

    return Response(status_code=200)


@light_router.patch("/{device_id}/turn_off")
def turn_light_off(device_id: str):
    if not light_service.get_light_for_device(device_id):
        raise HTTPException(status_code=404)

    light_service.turn_light_off(device_id)

    return Response(status_code=200)
