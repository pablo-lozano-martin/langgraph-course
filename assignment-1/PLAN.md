# 🧑‍💻 LangGraph: Ejercicio Backend

## 🎯 Objetivo
Crea un agente backend usando LangGraph que procese consultas de usuario, mantenga memoria, rote tareas y soporte puntos de control/feedback humano. Implementa toda la lógica en uno o más archivos `.py` (sin frontend).

## Tareas principales 🚦

### 1. Construcción del agente 🤖
- Crea un agente que responda preguntas usando una base de conocimiento simple (puede ser hardcodeada o cargada de un archivo).
- Usa LangGraph para definir el workflow.

### 2. Integración de memoria 🧠
- Implementa memoria de corto plazo para guardar las últimas 3 consultas y respuestas.
- Incluye campos extra en el estado además de los mensajes, como por ejemplo un resumen, contador de interacciones, etc.
- *Opcional:* Agrega memoria externa (por ejemplo, guardar/cargar desde archivo).

### 3. Ruteo y cadenas 🔀
- Rotea consultas a diferentes cadenas según el tipo (ej: matemáticas, conocimiento general, fallback).
- Cada cadena debe tener su propia lógica.

### 4. Puntos de control y feedback humano 🗣️
- Agrega un punto de control donde el agente pida feedback humano si no está seguro de la respuesta.
- Registra el feedback y permite reintentar o continuar.

## Tareas avanzadas (opcionales) ✨
- Implementa puntos de control dinámicos (por ejemplo, según score de confianza).
- Agrega salida en streaming (simula respuestas parciales).
- Soporta "time travel" (volver a un estado previo de memoria).

## Entregables 📦
- Uno o más archivos `.py` con la lógica del agente, cadenas, memoria y workflow.
- Actualiza este `PLAN.md` con tu diseño, pasos y notas.

---

**Consejo:** Empieza simple y agrega las opciones avanzadas al final. Usa comentarios para explicar tu workflow y lógica.
