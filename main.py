from fastapi import FastAPI, WebSocket, logger
from fastapi.staticfiles import StaticFiles
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

app = FastAPI()


@app.websocket("/agent")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        try:
            data = await websocket.receive_json()
            response = await process_message(data)
            await websocket.send_json(response)
        except Exception as e:
            # Try to notify the client about the error; if that fails, break the loop.
            try:
                await websocket.send_json({"type": "error", "data": str(e)})
            except Exception:
                break


# Mount static files after routes so ASGI scopes for websockets are handled by the
# websocket route instead of StaticFiles (which asserts on non-http scopes).
app.mount("/", StaticFiles(directory="public", html=True), name="public")


async def process_message(message: dict) -> dict:
    try:
        match message["type"]:
            case "init":
                return {
                    "type": "message",
                    "data": "Hello! How can I assist you today?",
                }
            case "message":
                history = ChatHistory()
                history.add_user_message(message["data"])

                result = await chat_completion.get_chat_message_content(
                    chat_history=history,
                    settings=execution_settings,
                    kernel=kernel,
                )

                return {
                    "type": "command",
                    "data": {
                        "message": result.content,
                    },
                }
            case _:
                return {
                    "type": "message",
                    "data": "I'm sorry, I don't understand that. Can you please rephrase?",
                }
    except Exception as e:
        logger.error(f"Error processing message: {e}")
        return {
            "type": "message",
            "data": "I'm sorry, I can't process your request right now.",
        }
