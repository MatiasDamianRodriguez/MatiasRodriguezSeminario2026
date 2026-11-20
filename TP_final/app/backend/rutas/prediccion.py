# Define POST /predecir y valida la entrada con Pydantic; si falta un campo o el tipo es incorrecto, FastAPI responde 422.
from fastapi import APIRouter
from pydantic import BaseModel, Field

from prediccion import predecir_especie

router = APIRouter()


class Entrada(BaseModel):
    largo_sepalo: float = Field(gt=0)
    ancho_sepalo: float = Field(gt=0)
    largo_petalo: float = Field(gt=0)
    ancho_petalo: float = Field(gt=0)


@router.post("/predecir")
def predecir(datos: Entrada):
    return predecir_especie(
        datos.largo_sepalo, datos.ancho_sepalo, datos.largo_petalo, datos.ancho_petalo
    )