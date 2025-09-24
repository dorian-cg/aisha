from typing import List, Annotated
from semantic_kernel.functions import kernel_function
from models.thermo import Thermo
from services import thermo_service


class ThermoPlugin:
    @kernel_function(
        name="get_all_thermos",
        description="Gets all thermos",
    )
    def get_all_thermos(self) -> Annotated[List[Thermo], "A list of all thermos"]:
        return thermo_service.get_thermos()

    @kernel_function(
        name="get_thermo_for_device",
        description="Gets the thermo for a specific device",
    )
    def get_thermo_for_device(
        self, device_id: Annotated[str, "The ID of the device"]
    ) -> Annotated[Thermo | None, "The thermo for the specified device or None"]:
        return thermo_service.get_thermo_for_device(device_id)
