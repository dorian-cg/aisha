from typing import List
from fastapi import APIRouter, WebSocket
from services import agent_service
from models.message import Message

agent_router = APIRouter(prefix="/agent")


@agent_router.websocket("/")
async def on_message(websocket: WebSocket):
    await websocket.accept()
    while True:
        messages: List[Message] = await websocket.receive_json()
        response = await agent_service.ask(messages)
        await websocket.send_json([response])
