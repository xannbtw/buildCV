# 🚀 BuildCV

BuildCV es una plataforma SaaS diseñada para revolucionar la creación y adaptación de currículums vitae utilizando Inteligencia Artificial. La aplicación extrae la información de un CV base, la procesa a través de AI y genera versiones altamente optimizadas enfocadas en los requerimientos específicos de cualquier oferta laboral.

Con un enfoque en la usabilidad, la plataforma ofrece un editor visual dinámico donde el usuario tiene el control total de su información antes de generar el documento final listo para postular.

## ✨ Características Principales

- **Motor de Inteligencia Artificial:** Integración con Gemini Flash para la reescritura adaptativa y estructuración inteligente de perfiles profesionales.
- **Editor Dinámico en Tiempo Real:** Interfaz reactiva que permite modificar datos de contacto y gestionar (añadir/eliminar) bloques de experiencia laboral y educación al instante.
- **Exportación Nativa a PDF:** Renderizado del currículum en formato A4 estricto desde el cliente, manteniendo un diseño minimalista optimizado para sistemas ATS (Applicant Tracking Systems).
- **Experiencia Responsiva:** Interfaz de usuario (UI) completamente adaptada a dispositivos móviles, con navegación fluida y menús colapsables.
- **Seguridad en la Nube:** Autenticación de usuarios y almacenamiento de datos gestionado por Supabase, utilizando políticas RLS para garantizar la privacidad de los documentos.

## 🛠️ Stack Tecnológico

- **Frontend:** Vue 3 (Composition API), TypeScript, Tailwind CSS, `html2pdf.js`.
- **Backend:** Python 3, FastAPI, Google GenAI SDK, PyPDF.
- **Base de Datos y Auth:** Supabase (PostgreSQL).
- **Infraestructura de Despliegue:** Frontend alojado en Vercel y API Backend orquestada en Railway.
