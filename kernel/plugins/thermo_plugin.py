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

    @kernel_function(
        name="turn_thermo_on",
        description="Turns a thermo on for a specific device",
    )
    def turn_thermo_on(self, device_id: Annotated[str, "The ID of the device"]) -> None:
        return thermo_service.turn_thermo_on(device_id)

    @kernel_function(
        name="turn_thermo_off",
        description="Turns a thermo off for a specific device",
    )
    def turn_thermo_off(
        self, device_id: Annotated[str, "The ID of the device"]
    ) -> None:
        return thermo_service.turn_thermo_off(device_id)

    @kernel_function(
        name="put_thermo_temperature",
        description="Sets the temperature for a thermo device",
    )
    def put_thermo_temperature(
        self,
        device_id: Annotated[str, "The ID of the device"],
        temperature: Annotated[int, "Desired temperature as integer"],
    ) -> None:
        return thermo_service.put_thermo_temperature(device_id, temperature)
