# 🏠 Operación Casa: Automatización con Python & Telegram

Este proyecto nace de una necesidad real: gestionar las tareas diarias del hogar y la logística financiera de forma automática. Es un bot de Telegram desarrollado en **Python** que actúa como asistente personal.

## 🐾 Funcionalidades Principales

1. **Gestión de Cuidado de Mascotas (Operación Pau):** - Notificaciones automáticas diarias (14:30 y 22:30) para asegurar que Pau (mi Bulldog Francés) reciba su ración de comida a tiempo.
   
2. **Control de Finanzas del Hogar:**
   - Cálculo automático de facturas (Alquiler, Vodafone, Nintendo, Luz y Gas).
   - Generación de informe de gastos el día 30 de cada mes con el desglose total y el reparto del 50% por persona.

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3.x
* **Librerías:** * `python-telegram-bot` (vía Requests) para la comunicación con la API.
    * `schedule` para la gestión de tareas cronometradas.
    * `json` para la persistencia de datos sensibles y configuración.

## 🔐 Seguridad y Configuración

El proyecto utiliza un archivo `config.json` (protegido mediante `.gitignore`) para gestionar el Token de la API y los IDs de los usuarios de forma segura, siguiendo las mejores prácticas de desarrollo para evitar la exposición de credenciales.

---
*Proyecto desarrollado por **Emidio Faisca** como parte de mi transición al sector IT.*