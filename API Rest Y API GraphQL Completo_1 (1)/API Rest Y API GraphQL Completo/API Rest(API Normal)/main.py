from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import stanza

# Descarga el modelo solo si no está (primera vez)
stanza.download('es')

# Cargar el modelo en español
nlp = stanza.Pipeline('es')

# Crear la app FastAPI
app = FastAPI()

# Permitir peticiones del frontend (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelo para el texto recibido
class Texto(BaseModel):
    texto: str

# Ruta para análisis
@app.post("/analizar")
def analizar_texto(data: Texto):
    doc = nlp(data.texto)
    resultado = []
    for sent in doc.sentences:
        for word in sent.words:
            resultado.append({
                "texto": word.text,
                "pos": word.pos,
                "lemma": word.lemma,
                "caracteristicas": word.feats or ""
            })
    return {"analisis": resultado}