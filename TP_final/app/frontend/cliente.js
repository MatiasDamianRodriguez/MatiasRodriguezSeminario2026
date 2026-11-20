// Habla con la API: manda los datos a /predecir con fetch y
//  devuelve el código de estado y el JSON recibido.

const API_URL = "http://127.0.0.1:8000";

async function llamarPredecir(datos) {
  const respuesta = await fetch(`${API_URL}/predecir`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(datos),
  });
  const cuerpo = await respuesta.json();
  return { estado: respuesta.status, cuerpo: cuerpo };
}