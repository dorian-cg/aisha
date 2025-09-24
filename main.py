from dotenv import load_dotenv

# run before anything else is imported
load_dotenv(override=True)  #  load .env file if it exists


from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from api.device_routes import device_router
from api.light_routes import light_router
from api.lock_routes import lock_router
from api.room_routes import room_router
from api.thermo_routes import thermo_router

from ws.agent_routes import agent_router
from data.mock import build_mock_data


build_mock_data()

app = FastAPI(title="A.I.S.H.A")

# Include routers directly with the app, not with an intermediate router
app.include_router(device_router, prefix="/api")
app.include_router(light_router, prefix="/api")
app.include_router(lock_router, prefix="/api")
app.include_router(room_router, prefix="/api")
app.include_router(thermo_router, prefix="/api")
app.include_router(agent_router, prefix="/ws")

# Mount static files at /static instead of root
app.mount("/", StaticFiles(directory="public", html=True), name="static")
