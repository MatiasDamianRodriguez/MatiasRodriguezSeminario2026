// Habla con la API: manda los datos a /predecir con fetch y
//  devuelve el código de estado y el JSON recibido.

// Dirección de la API publicada en Render (sin barra final).
const API_URL = "https://matiasrodriguezseminario2026.onrender.com";

async function llamarPredecir(datos) {
  const respuesta = await fetch(`${API_URL}/predecir`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(datos),
  });
  const cuerpo = await respuesta.json();
  return { estado: respuesta.status, cuerpo: cuerpo };
}