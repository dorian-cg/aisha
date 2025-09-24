from typing import List
from fastapi import APIRouter
from services import lock_service
from models.lock import Lock

lock_router = APIRouter(prefix="/lock")


@lock_router.get("/get/all")
def get_locks() -> List[Lock]:
    return lock_service.get_locks()


@lock_router.get("/get/device/{device_id}")
def get_lock_for_device(device_id: int) -> Lock:
    return lock_service.get_lock_for_device(device_id)
