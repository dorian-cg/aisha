from fastapi import FastAPI, WebSocket
from fastapi.staticfiles import StaticFiles

app = FastAPI()

@app.websocket("/agent")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_json({"type": "message", "data": f"Hello I'm A.I.S.H.A"})


# Mount static files after routes so ASGI scopes for websockets are handled by the
# websocket route instead of StaticFiles (which asserts on non-http scopes).
app.mount("/", StaticFiles(directory="public", html=True), name="public")