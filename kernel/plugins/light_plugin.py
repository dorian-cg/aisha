from typing import List, Annotated
from semantic_kernel.functions import kernel_function
from models.light import Light
from services import light_service


class LightPlugin:
    @kernel_function(
        name="get_all_lights",
        description="Gets all lights",
    )
    def get_all_lights(self) -> Annotated[List[Light], "A list of all lights"]:
        return light_service.get_lights()

    @kernel_function(
        name="get_light_for_device",
        description="Gets the light for a specific device",
    )
    def get_light_for_device(
        self, device_id: Annotated[str, "The ID of the device"]
    ) -> Annotated[Light | None, "The light for the specified device or None"]:
        return light_service.get_light_for_device(device_id)

    @kernel_function(
        name="turn_light_on",
        description="Turns a light on for a specific device",
    )
    def turn_light_on(self, device_id: Annotated[str, "The ID of the device"]) -> None:
        return light_service.turn_light_on(device_id)

    @kernel_function(
        name="turn_light_off",
        description="Turns a light off for a specific device",
    )
    def turn_light_off(self, device_id: Annotated[str, "The ID of the device"]) -> None:
        return light_service.turn_light_off(device_id)
