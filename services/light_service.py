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
