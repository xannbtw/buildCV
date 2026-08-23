from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel 
import os
import json
import io
from dotenv import load_dotenv
from google import genai
from google.genai import types
from pypdf import PdfReader
from typing import List

#cargar .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Api Key no encontrada.")

# GEMINI
client = genai.Client(api_key=api_key)

# inicializar app
app = FastAPI()

# configuracion CORS para conectar back con front
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "https://optimizadorcv-frontend-ufxe-theta.vercel.app/"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# modelo de datos que se recibe del front 
class GenerarRequest(BaseModel):
    instruccion: str
    cv_base: dict

class DatosPersonales(BaseModel):
    fullName: str
    jobTitle: str
    email: str       # <--- NUEVO
    phone: str       # <--- NUEVO

class Experiencia(BaseModel):
    company: str
    position: str
    date: str        # <--- NUEVO (Ej: "Enero 2023 - Presente")
    location: str    # <--- NUEVO (Ej: "Remoto" o "Santiago, Chile")
    description: str

class Educacion(BaseModel): # <--- NUEVA CLASE
    institution: str
    degree: str
    date: str

class CVRespuesta(BaseModel):
    personal: DatosPersonales
    experience: List[Experiencia]
    education: List[Educacion]  # <--- AGREGAR A LA RESPUESTA FINAL

# endpoints 
@app.post("/api/generar-cv")
async def generar_cv(datos: GenerarRequest):
    print("CV generado")

    prompt = f"""
    Eres un experto en Recursos Humanos. A continuación te proporciono el currículum REAL de un candidato en formato JSON:
    
    {json.dumps(datos.cv_base)}
    
    El candidato postula a una oferta con esta instrucción: "{datos.instruccion}".
    
    Tu tarea es ADAPTAR las descripciones de su experiencia y su título profesional para destacar lo más relevante para esta oferta.
    REGLA ESTRICTA: NO inventes empresas, cargos ni experiencia que no existan en el JSON base. Solo mejora la redacción y resalta los logros pertinentes.
    
    DEBES responder ÚNICA y EXCLUSIVAMENTE con un objeto JSON válido, manteniendo esta estructura:
    {{
      "personal": {{
        "fullName": "Mantén el nombre real",
        "jobTitle": "Adapta el cargo",
        "email": "Mantén el correo",
        "phone": "Mantén el teléfono"
      }},
      "experience": [
        {{
          "company": "Mantén la empresa real",
          "position": "Mantén el cargo real",
          "date": "Mantén la fecha real",
          "location": "Mantén la ubicación real",
          "description": "Redacción adaptada a la oferta, sin inventar hechos."
        }}
      ],
      "education": "Devuelve exactamente el mismo arreglo de education que venía en el cv_base sin modificarlo"
    }}
    """
    try:
        response = client.models.generate_content(
            model='gemini-3.6-flash',
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
            ),
        )
        
        texto_limpio = response.text.strip()
        diccionario_cv = json.loads(texto_limpio)
        
        print("¡CV generado con éxito!")
        return diccionario_cv
        
    except Exception as e:
        print(f"Error al procesar con la IA: {e}")
        return {"error": "Hubo un problema procesando tu CV con IA."}


@app.post("/api/procesar-pdf")
async def procesar_pdf(file: UploadFile = File(...)):
    print(f"Archivo: {file.filename}")
    try:
        contenido_pdf = await file.read()
        lector = PdfReader(io.BytesIO(contenido_pdf))
        
        texto_completo = ""
        for pagina in lector.pages:
            texto_completo += pagina.extract_text() + "\n"
        
        print("PDF extraido con exito")

        prompt = f"""
          Eres un experto en Recursos Humanos. A continuación te proporciono el texto extraído del currículum original de un candidato.
          
          Tu tarea es leer esta información, limpiarla, mejorar la redacción para que suene profesional y devolverla ÚNICA y EXCLUSIVAMENTE como un objeto JSON válido, sin texto adicional.
          
          TEXTO DEL CV:
          {texto_completo}
          
          Usa exactamente esta estructura:
          {{
            "personal": {{
              "fullName": "Extraer nombre",
              "jobTitle": "Extraer o deducir el cargo principal",
              "email": "Extraer correo",
              "phone": "Extraer teléfono"
            }},
            "experience": [
              {{
                "company": "Nombre empresa",
                "position": "Cargo",
                "date": "Fechas de inicio y fin (ej. Enero 2023 - Presente)",
                "location": "Ubicación o modalidad",
                "description": "Mejora la redacción de sus logros y responsabilidades."
              }}
            ],
            "education": [
              {{
                "institution": "Nombre de la universidad o colegio",
                "degree": "Título obtenido o carrera",
                "date": "Fecha de estudio"
              }}
            ]
          }}
          """
        
        response = client.models.generate_content(
            model='gemini-3.6-flash',
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
            ),
        )
        
        return json.loads(response.text.strip())


    except Exception as e:
        print(f"Error procesando PDF: {e}")
        return {"error": "No se pudo procesar el documento."}