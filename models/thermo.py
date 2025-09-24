from dataclasses import dataclass


@dataclass
class Thermo:
    id: str = ""
    device_id: str = ""
    is_on: bool = False
    temperature: int = 22
