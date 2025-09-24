from models.thermo import Thermo
from data.mock import mock_db


def get_thermos() -> list[Thermo]:
    return mock_db.thermos


def get_thermo_for_device(device_id: str) -> Thermo | None:
    thermos = get_thermos()

    for thermo in thermos:
        if thermo.device_id == device_id:
            return thermo

    return None
