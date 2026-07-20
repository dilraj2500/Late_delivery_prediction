from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from backend.routes import router
from database.database import engine
from database.models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Late Delivery Risk Prediction API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="frontend"), name="static")

@app.get("/ui")
def frontend():
    return FileResponse("frontend/index.html")

app.include_router(router)