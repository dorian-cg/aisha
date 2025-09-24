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
