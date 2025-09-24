from models.device import Device
from data.mock import mock_db


def get_devices() -> list[Device]:
    return mock_db.devices


def get_devices_for_room(room_id: str) -> list[Device]:
    devices = get_devices()

    return [d for d in devices if d.room_id == room_id]


def get_device_by_id(device_id: str) -> Device | None:
    devices = get_devices()

    for d in devices:
        if d.id == device_id:
            return d

    return None


def get_device_by_name(name: str) -> Device | None:
    devices = get_devices()

    for d in devices:
        if d.name == name:
            return d

    return None
