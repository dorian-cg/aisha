from typing import List
from fastapi import APIRouter
from services import thermo_service
from models.thermo import Thermo

thermo_router = APIRouter(prefix="/thermo")


@thermo_router.get("/get/all")
def get_thermos() -> List[Thermo]:
    return thermo_service.get_thermos()


@thermo_router.get("/get/device/{device_id}")
def get_thermo_for_device(device_id: str) -> Thermo:
    return thermo_service.get_thermo_for_device(device_id)
