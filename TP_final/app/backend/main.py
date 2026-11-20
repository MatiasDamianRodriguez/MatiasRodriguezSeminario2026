# Crea la app FastAPI, habilita CORS para el frontend, define /health y enchufa las rutas de predicción.
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from rutas.prediccion import router as router_prediccion

app = FastAPI(title="API Iris")

# Permite que el frontend en otro dominio llame a la API; en producción reemplazá "*" por la URL de tu frontend.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health():
    return {"estado": "ok"}


app.include_router(router_prediccion)