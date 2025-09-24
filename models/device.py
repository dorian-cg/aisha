from dataclasses import dataclass
from typing import TypeVar, Generic

T = TypeVar("T")


@dataclass
class Device(Generic[T]):
    id: str = ""
    room_id: str = ""
    name: str = ""
    kind: str = ""
