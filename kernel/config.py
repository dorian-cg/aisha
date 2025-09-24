import os
import logging
from semantic_kernel import Kernel
from semantic_kernel.utils.logging import setup_logging
from semantic_kernel.connectors.ai.function_choice_behavior import (
    FunctionChoiceBehavior,
)
from semantic_kernel.connectors.ai.open_ai import (
    AzureChatCompletion,
    AzureChatPromptExecutionSettings,
)
from kernel.plugins.device_plugin import DevicePlugin
from kernel.plugins.light_plugin import LightPlugin
from kernel.plugins.lock_plugin import LockPlugin
from kernel.plugins.room_plugin import RoomPlugin
from kernel.plugins.thermo_plugin import ThermoPlugin

setup_logging()
kernel_logger = logging.getLogger("kernel")
kernel_logger.setLevel(logging.DEBUG)

execution_settings = AzureChatPromptExecutionSettings(
    function_choice_behavior=FunctionChoiceBehavior.Auto()
)

chat_completion = AzureChatCompletion(
    deployment_name=os.getenv("AZ_OPENAI_DEPLOYMENT_NAME"),
    api_key=os.getenv("AZ_OPENAI_CHAT_COMPLETION_API_KEY"),
    api_version=os.getenv("AZ_OPENAI_API_VERSION"),
    endpoint=os.getenv("AZ_OPENAI_ENDPOINT"),
)

kernel = Kernel()
kernel.add_service(chat_completion)

kernel.add_plugin(DevicePlugin(), "Device")
kernel.add_plugin(LightPlugin(), "Light")
kernel.add_plugin(LockPlugin(), "Lock")
kernel.add_plugin(RoomPlugin(), "Room")
kernel.add_plugin(ThermoPlugin(), "Thermo")
