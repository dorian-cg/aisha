from models.room import Room
from data.mock import mock_db


def get_rooms() -> list[Room]:
    return mock_db.rooms


def get_room_by_id(room_id: str) -> Room | None:
    rooms = get_rooms()

    for r in rooms:
        if r.id == room_id:
            return r

    return None


def get_room_by_name(name: str) -> Room | None:
    rooms = get_rooms()

    for r in rooms:
        if r.name == name:
            return r

    return None
