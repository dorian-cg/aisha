from typing import List
from fastapi import APIRouter, WebSocket
from services import agent_service
from models.message import Message

agent_router = APIRouter()


@agent_router.websocket("/agent")
async def on_message(websocket: WebSocket):
    await websocket.accept()
    while True:
        data: List[dict] = await websocket.receive_json()
        messages = [Message(**item) for item in data]
        response = await agent_service.ask(messages)
        await websocket.send_json([response])
