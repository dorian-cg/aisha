from typing import List
from fastapi import APIRouter, HTTPException, Response
from models.lock import Lock
from services import lock_service

lock_router = APIRouter(prefix="/lock", tags=["Lock Endpoints"])


@lock_router.get("/all")
def get_locks() -> List[Lock]:
    return lock_service.get_locks()


@lock_router.get("/{device_id}")
def get_lock_for_device(device_id: int) -> Lock:
    lock = lock_service.get_lock_for_device(device_id)

    if not lock:
        raise HTTPException(status_code=404)

    return lock


@lock_router.patch("/{device_id}/lock")
def lock_device(device_id: int):
    if not lock_service.get_lock_for_device(device_id):
        raise HTTPException(status_code=404)

    lock_service.lock_device(device_id)

    return Response(status_code=200)


@lock_router.patch("/{device_id}/unlock")
def unlock_device(device_id: int):
    if not lock_service.get_lock_for_device(device_id):
        raise HTTPException(status_code=404)

    lock_service.unlock_device(device_id)

    return Response(status_code=200)
