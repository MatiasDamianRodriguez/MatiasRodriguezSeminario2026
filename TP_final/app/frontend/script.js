// Maneja el formulario: arma el JSON, llama a la API y muestra la predicción o el mensaje de error correspondiente.
const formulario = document.getElementById("formulario");
const caja = document.getElementById("resultado");

function mostrar(clase, texto) {
  // Muestra un mensaje en la caja de resultado con el estilo indicado (ok, error o cargando).
  caja.hidden = false;
  caja.className = clase;
  caja.textContent = texto;
}

formulario.addEventListener("submit", async (evento) => {
  evento.preventDefault();

  const datos = {
    largo_sepalo: parseFloat(document.getElementById("largo_sepalo").value),
    ancho_sepalo: parseFloat(document.getElementById("ancho_sepalo").value),
    largo_petalo: parseFloat(document.getElementById("largo_petalo").value),
    ancho_petalo: parseFloat(document.getElementById("ancho_petalo").value),
  };

  mostrar("cargando", "Consultando... (si la API estaba dormida, puede tardar hasta un minuto)");

  try {
    const { estado, cuerpo } = await llamarPredecir(datos);

    if (estado === 422) {
      mostrar("error", "Entrada inválida: revisá que los 4 valores sean números mayores que cero.");
    } else if (estado === 200) {
      const prob = (cuerpo.probabilidad * 100).toFixed(1);
      mostrar("ok", `Predicción: ${cuerpo.prediccion} (probabilidad ${prob}%)`);
    } else {
      mostrar("error", `La API respondió con un error inesperado (código ${estado}).`);
    }
  } catch (error) {
    mostrar("error", "No se pudo conectar con la API. Verificá que esté encendida e intentá de nuevo.");
  }
});