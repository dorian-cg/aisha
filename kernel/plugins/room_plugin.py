from typing import List, Annotated
from semantic_kernel.functions import kernel_function
from models.room import Room
from services import room_service


class RoomPlugin:
    @kernel_function(
        name="get_all_rooms",
        description="Gets all rooms in the smart home",
    )
    def get_all_rooms(self) -> Annotated[List[Room], "A list of all rooms"]:
        return room_service.get_rooms()

    @kernel_function(
        name="get_room_by_id",
        description="Gets a room by its ID",
    )
    def get_room_by_id(
        self, room_id: Annotated[str, "The ID of the room"]
    ) -> Annotated[Room | None, "The room with the specified ID or None"]:
        return room_service.get_room_by_id(room_id)

    @kernel_function(
        name="get_room_by_name",
        description="Gets a room by its name",
    )
    def get_room_by_name(
        self, name: Annotated[str, "The name of the room"]
    ) -> Annotated[Room | None, "The room with the specified name or None"]:
        return room_service.get_room_by_name(name)
