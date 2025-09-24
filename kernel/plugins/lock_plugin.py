from typing import List, Annotated
from semantic_kernel.functions import kernel_function
from models.lock import Lock
from services import lock_service


class LockPlugin:
    @kernel_function(
        name="get_all_locks",
        description="Gets all locks",
    )
    def get_all_locks(self) -> Annotated[List[Lock], "A list of all locks"]:
        return lock_service.get_locks()

    @kernel_function(
        name="get_lock_for_device",
        description="Gets the lock for a specific device",
    )
    def get_lock_for_device(
        self, device_id: Annotated[str, "The ID of the device"]
    ) -> Annotated[Lock | None, "The lock for the specified device or None"]:
        return lock_service.get_lock_for_device(device_id)
