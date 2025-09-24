from models.lock import Lock
from data.mock import mock_db


def get_locks() -> list[Lock]:
    return mock_db.locks


def get_lock_for_device(device_id: int) -> Lock | None:
    locks = get_locks()

    for lock in locks:
        if lock.device_id == device_id:
            return lock

    return None
