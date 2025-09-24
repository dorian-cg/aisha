from dataclasses import dataclass


@dataclass
class Lock:
    id: str = ""
    device_id: str = ""
    is_locked: bool = False
