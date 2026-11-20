# Carga el modelo una sola vez y expone predecir_especie(), la función que usa la API para clasificar una flor.
from pathlib import Path
import joblib
import pandas as pd

RUTA_MODELO = Path(__file__).resolve().parent.parent / "modelo" / "modelo.joblib"
modelo = joblib.load(RUTA_MODELO)  # se carga al importar, o sea una sola vez al arrancar

CLASES = ["setosa", "versicolor", "virginica"]
COLUMNAS = ["sepal length (cm)", "sepal width (cm)", "petal length (cm)", "petal width (cm)"]


def predecir_especie(largo_sepalo, ancho_sepalo, largo_petalo, ancho_petalo):
    # Devuelve la especie más probable, su probabilidad y las probabilidades de las 3 clases.
    fila = pd.DataFrame(
        [[largo_sepalo, ancho_sepalo, largo_petalo, ancho_petalo]], columns=COLUMNAS
    )
    probas = modelo.predict_proba(fila)[0]
    idx = int(probas.argmax())
    return {
        "prediccion": CLASES[idx],
        "probabilidad": round(float(probas[idx]), 4),
        "probabilidades": {c: round(float(p), 4) for c, p in zip(CLASES, probas)},
    }


if __name__ == "__main__":
    # Prueba rápida sin la API: python prediccion.py
    print(predecir_especie(5.1, 3.5, 1.4, 0.2))