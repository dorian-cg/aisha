from typing import List
from fastapi import APIRouter, HTTPException, Response
from services import thermo_service
from models.thermo import Thermo

thermo_router = APIRouter(prefix="/thermo", tags=["Thermo Endpoints"])


@thermo_router.get("/all")
def get_thermos() -> List[Thermo]:
    return thermo_service.get_thermos()


@thermo_router.get("/{device_id}")
def get_thermo_for_device(device_id: str) -> Thermo:
    thermo = thermo_service.get_thermo_for_device(device_id)

    if not thermo:
        raise HTTPException(status_code=404)

    return thermo


@thermo_router.patch("/{device_id}/temperature/{temperature}")
def set_thermo_temperature(device_id: str, temperature: int):
    if not thermo_service.get_thermo_for_device(device_id):
        raise HTTPException(status_code=404)

    thermo_service.set_thermo_temperature(device_id, temperature)

    return Response(status_code=200)


@thermo_router.patch("/{device_id}/turn_on")
def turn_thermo_on(device_id: str):
    if not thermo_service.get_thermo_for_device(device_id):
        raise HTTPException(status_code=404)

    thermo_service.turn_thermo_on(device_id)

    return Response(status_code=200)


@thermo_router.patch("/{device_id}/turn_off")
def turn_thermo_off(device_id: str):
    if not thermo_service.get_thermo_for_device(device_id):
        raise HTTPException(status_code=404)

    thermo_service.turn_thermo_off(device_id)

    return Response(status_code=200)
