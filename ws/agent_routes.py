from fastapi import APIRouter, WebSocket, logger

agent_router = APIRouter(prefix="/agent")


@agent_router.websocket("/")
async def on_message(websocket: WebSocket):
    await websocket.accept()
    while True:
        try:
            data = await websocket.receive_json()
            await websocket.send_json(data)
        except Exception as e:
            logger.error(f"Error processing message: {e}")
            await websocket.send_json(
                {"error": "An error occurred processing message."}
            )
