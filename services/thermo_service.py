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


def turn_thermo_on(device_id: str):
    thermos = get_thermos()
    for thermo in thermos:
        if thermo.device_id == device_id:
            thermo.is_on = True
            return True

    return False


def turn_thermo_off(device_id: str):
    thermos = get_thermos()
    for thermo in thermos:
        if thermo.device_id == device_id:
            thermo.is_on = False
            return True

    return False


def put_thermo_temperature(device_id: str, temperature: int):
    thermos = get_thermos()
    for thermo in thermos:
        if thermo.device_id == device_id:
            thermo.temperature = temperature
            return True

    return False
