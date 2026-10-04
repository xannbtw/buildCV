from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel 
import os
import json
import io
import time
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

# inicializar
app = FastAPI()

# configuracion CORS 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "https://optimizadorcv-frontend-ufxe-theta.vercel.app", "https://buildcv.lat", "https://www.buildcv.lat"],
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
    email: str      
    phone: str       

class Experiencia(BaseModel):
    company: str
    position: str
    date: str 
    location: str 
    description: str

class Educacion(BaseModel): 
    institution: str
    degree: str
    date: str

class CVRespuesta(BaseModel):
    personal: DatosPersonales
    experience: List[Experiencia]
    education: List[Educacion]

# endpoints 
@app.post("/api/generar-cv")
async def generar_cv(datos: GenerarRequest):
    print(f"Instrucción: {datos.instruccion}") 
    
    prompt = f"""
    Eres un experto en Recursos Humanos. A continuación tienes el currículum REAL de un candidato en formato JSON:
    
    {json.dumps(datos.cv_base, ensure_ascii=False)}
    
    El candidato postula a la siguiente oferta: "{datos.instruccion}".
    
    TU MISIÓN:
    Devuelve un objeto JSON con la MISMA estructura exacta, pero aplicando estas 2 únicas mejoras:
    1. Modifica el campo 'jobTitle' en 'personal' para que haga match perfecto con la oferta.
    2. Mejora la redacción del campo 'description' en 'experience' para destacar las habilidades útiles para este puesto, basándote solo en su experiencia real.
    
    REGLA DE ORO (ESTRICTA): 
    Debes COPIAR INTACTOS los valores reales de fullName, email, phone, company, date, location y todo el arreglo de education. NO uses placeholders ni textos de relleno. Si un campo viene vacío, déjalo vacío.
    REGLA CRÍTICA: Si las instrucciones del usuario mencionan una experiencia laboral actual o nueva que NO estaba en el texto del currículum original, tienes estrictamente PERMITIDO y OBLIGADO extraer esos datos, redactarlos de forma profesional y agregarlos como un bloque nuevo dentro del arreglo 'experience'.
    Responde ÚNICA y EXCLUSIVAMENTE con el JSON final válido.
    """
    
    max_reintentos = 4
    for intento in range(max_reintentos):
        try:
            response = client.models.generate_content(
                model='gemini-3.5-flash-lite',
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_mime_type="application/json",
                ),
            )
            texto_limpio = response.text.strip()
            diccionario_cv = json.loads(texto_limpio)
            return diccionario_cv
            
            
        except Exception as e:
            error_str = str(e)
            if "503" in error_str and intento < max_reintentos - 1:
                print(f"Servidor de Google saturado (503). Reintentando en 5 segundos... (Intento {intento + 1}/3)")
                time.sleep(5)
            else:
                print(f"Error al procesar con la IA: {e}")
                return {"error": "Hubo un problema procesando tu CV con IA."}
                
    return {"error": "Los servidores de IA están demasiado ocupados. Intenta en unos minutos."}


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
              "phone": "Extraer teléfono",
              "summary": "Resumen Profesional extraido de la experiencia laboral"
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
        
        max_reintentos = 4
        for intento in range(max_reintentos):
            try:
                response = client.models.generate_content(
                    model='gemini-3.5-flash-lite',
                    contents=prompt,
                    config=types.GenerateContentConfig(
                        response_mime_type="application/json",
                    ),
                )
                texto_limpio = response.text.strip()
                diccionario_cv = json.loads(texto_limpio)
                return diccionario_cv
            
            
            except Exception as e:
                error_str = str(e)
                if "503" in error_str and intento < max_reintentos - 1:
                    print(f"Servidor de Google saturado (503). Reintentando en 5 segundos... (Intento {intento + 1}/3)")
                    time.sleep(5)
                else:
                    print(f"Error al procesar con la IA: {e}")
                    return {"error": "Hubo un problema procesando tu CV con IA."}
                
        return {"error": "Los servidores de IA están demasiado ocupados. Intenta en unos minutos."}
        
        return json.loads(response.text.strip())


    except Exception as e:
        print(f"Error procesando PDF: {e}")
        return {"error": "No se pudo procesar el documento."}