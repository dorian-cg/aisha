from semantic_kernel import Kernel
from semantic_kernel.contents.chat_history import ChatHistory
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from semantic_kernel.connectors.ai.function_choice_behavior import (
    FunctionChoiceBehavior,
)
from semantic_kernel.connectors.ai.open_ai.prompt_execution_settings.azure_chat_prompt_execution_settings import (
    AzureChatPromptExecutionSettings,
)

execution_settings = AzureChatPromptExecutionSettings()
execution_settings.function_choice_behavior = FunctionChoiceBehavior.Auto()

chat_completion = AzureChatCompletion(
    deployment_name="o4-mini",
    api_key="",
    api_version="2025-01-01-preview",
    endpoint="https://dorianco.openai.azure.com",
)

kernel = Kernel()
kernel.add_service(chat_completion)
