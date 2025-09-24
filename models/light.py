from dataclasses import dataclass


@dataclass
class Light:
    id: str = ""
    device_id: str = ""
    is_on: bool = False
