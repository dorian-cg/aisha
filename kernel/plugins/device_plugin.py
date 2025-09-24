from typing import List, Annotated
from semantic_kernel.functions import kernel_function
from models import Device
from services import device_service


class DevicePlugin:
    @kernel_function(
        name="get_all_devices",
        description="Gets all devices",
    )
    def get_all_devices(self) -> Annotated[List[Device], "A list of all devices"]:
        return device_service.get_devices()

    @kernel_function(
        name="get_devices_for_room",
        description="Gets devices for a specific room",
    )
    def get_devices_for_room(
        self, room_id: Annotated[str, "The ID of the room"]
    ) -> Annotated[List[Device], "A list of devices in the room"]:
        return device_service.get_devices_for_room(room_id)

    @kernel_function(
        name="get_device_by_id",
        description="Gets a device by its ID",
    )
    def get_device_by_id(
        self, device_id: Annotated[str, "The ID of the device"]
    ) -> Annotated[Device, "The device with the specified ID"]:
        return device_service.get_device_by_id(device_id)

    @kernel_function(
        name="get_device_by_name",
        description="Gets a device by its name",
    )
    def get_device_by_name(
        self, name: Annotated[str, "The name of the device"]
    ) -> Annotated[Device, "The device with the specified name"]:
        return device_service.get_device_by_name(name)
