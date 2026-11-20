# Crea la app FastAPI, limita CORS a la página publicada, define /health y enchufa las rutas de predicción.
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from rutas.prediccion import router as router_prediccion

app = FastAPI(title="API Iris")

# Solo estos sitios pueden leer las respuestas desde un navegador: la página de GitHub Pages y Live Server (pruebas locales).
ORIGENES_PERMITIDOS = [
    "https://matiasdamianrodriguez.github.io",
    "http://127.0.0.1:5500",
    "http://localhost:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGENES_PERMITIDOS,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health():
    # Responde sin tocar el modelo; sirve para comprobar que el servidor está vivo.
    return {"estado": "ok"}


app.include_router(router_prediccion)