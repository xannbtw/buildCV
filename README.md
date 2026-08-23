# 🚀 BuilCV

BuildCV es una plataforma diseñada para adaptar y optimizar currículums vitae utilizando Inteligencia Artificial. La aplicación extrae la información de un CV en formato PDF, la procesa y permite a los usuarios generar versiones adaptadas específicamente a diferentes ofertas laborales mediante el modelo Gemini de Google.

El frontend presenta una interfaz moderna y un renderizado en tiempo real basado en el estándar profesional "Jake Ryan", mientras que el backend en Python orquesta la extracción y la IA.

## ✨ Características Principales

- **Extracción de PDF con IA:** Lectura inteligente de archivos PDF para estructurar datos (personales, experiencia, educación) en formato JSON.
- **Optimización con Gemini AI:** Reescritura adaptativa de la experiencia laboral enfocada en los requerimientos específicos de un *prompt* o vacante.
- **Autenticación Segura:** Sistema de Login/Registro gestionado mediante Supabase Auth.
- **Almacenamiento Privado en la Nube:** Base de datos PostgreSQL con políticas RLS (Row Level Security) que garantizan que cada usuario solo pueda acceder a sus propios documentos.
- **Renderizado Profesional:** Plantilla de currículum limpia, minimalista y amigable con sistemas ATS (Applicant Tracking Systems).

## 🛠️ Stack Tecnológico

**Frontend:**
- Vue 3 (Composition API) + TypeScript
- Tailwind CSS (Estilizado con sistema de valores arbitrarios y variables de marca)
- Vite

**Backend:**
- Python 3
- FastAPI (API RESTful)
- Google GenAI SDK (Gemini Flash)
- PyPDF (Lectura de documentos)

**Base de Datos y Auth:**
- Supabase (PostgreSQL)

## 📁 Estructura del Proyecto (Monorepo)

```text
buildCV/
├── optimizadorcv-frontend/ # Aplicación de usuario (Vue 3)
│   ├── src/        # Vistas, Componentes y Store global
│   └── supabase.ts # Conexión con la BD
└── optimizadorcv-backend/ # Lógica de servidor e IA (FastAPI)
    └── main.py     # Endpoints y Prompts para Gemini
