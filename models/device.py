from dataclasses import dataclass


@dataclass
class Device:
    id: str = ""
    room_id: str = ""
    name: str = ""
    kind: str = ""
