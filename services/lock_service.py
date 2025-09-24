from models.lock import Lock
from data.mock import mock_db


def get_locks() -> list[Lock]:
    return mock_db.locks


def get_lock_for_device(device_id: str) -> Lock | None:
    locks = get_locks()

    for lock in locks:
        if lock.device_id == device_id:
            return lock

    return None


def lock(device_id: str):
    locks = get_locks()
    for lock in locks:
        if lock.device_id == device_id:
            lock.is_locked = True


def unlock(device_id: str):
    locks = get_locks()
    for lock in locks:
        if lock.device_id == device_id:
            lock.is_locked = False
