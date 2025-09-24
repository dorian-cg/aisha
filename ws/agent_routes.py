from typing import List
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from services import agent_service
from models.message import Message

agent_router = APIRouter()


@agent_router.websocket("/agent")
async def on_connect(websocket: WebSocket):
    await websocket.accept()
    is_connected = True
    while is_connected:
        try:
            data: List[dict] = await websocket.receive_json()
            messages = [Message(**item) for item in data]
            response = await agent_service.ask(messages)

            await websocket.send_json([response])

        except WebSocketDisconnect:
            is_connected = False
