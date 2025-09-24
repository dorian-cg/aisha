from models.light import Light
from data.mock import mock_db


def get_lights() -> list[Light]:
    return mock_db.lights


def get_light_for_device(device_id: str) -> Light | None:
    lights = get_lights()

    for light in lights:
        if light.device_id == device_id:
            return light

    return None


def turn_light_on(device_id: str) -> bool:
    lights = get_lights()
    for light in lights:
        if light.device_id == device_id:
            light.is_on = True
            return True

    return False


def turn_light_off(device_id: str) -> bool:
    lights = get_lights()
    for light in lights:
        if light.device_id == device_id:
            light.is_on = False
            return True

    return False
