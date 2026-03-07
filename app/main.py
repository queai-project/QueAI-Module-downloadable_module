from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import time
import os 
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="Downloadable Plugin",
    root_path="/api/downloadable_plugin"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Endpoint que simula una tarea de IA (ej: generar texto)
@app.get("/process")
async def process_data(text: str = "mundo"):
    return {
        "status": "success",
        "result": f"{text.upper()} {  str(os.getenv('archivo'))}.📝",
        "module": "Demo Plugin v1.0"
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# Servir los archivos estáticos de la UI
app.mount("/ui", StaticFiles(directory="frontend_dist", html=True), name="ui")
