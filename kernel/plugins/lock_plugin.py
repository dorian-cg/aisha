from typing import List, Annotated
from semantic_kernel.functions import kernel_function
from models.lock import Lock
from services import lock_service


class LockPlugin:
    @kernel_function(
        name="get_all_locks",
        description="Gets all locks in the smart home",
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

    @kernel_function(
        name="lock",
        description="Locks a lock device",
    )
    def lock(
        self, device_id: Annotated[str, "The ID of the device"]
    ) -> Annotated[bool, "Whether the lock was locked successfully"]:
        return lock_service.lock(device_id)

    @kernel_function(
        name="unlock",
        description="Unlocks a lock device",
    )
    def unlock(
        self, device_id: Annotated[str, "The ID of the device"]
    ) -> Annotated[bool, "Whether the lock was unlocked successfully"]:
        return lock_service.unlock(device_id)
