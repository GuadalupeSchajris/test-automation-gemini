# Test Automation with Gemini

Generador automatico de tests unitarios en Python usando la API de Gemini (Google AI).

## Que hace?

Lee codigo Python de un archivo, lo envia a Gemini con un prompt optimizado, y genera tests unitarios con pytest automaticamente.

## Estructura

- app.py - Codigo de ejemplo a testear
- test_generator.py - Script principal con Gemini
- config.py - Tu API key (no se sube a GitHub)
- config.example.py - Plantilla de configuracion
- tests_generados.py - Tests generados por la IA
- README.md - Este archivo

## Instalacion

# Clonar repo
git clone https://github.com/GuadalupeSchajris/test-automation-gemini.git
cd test-automation-gemini

# Crear entorno virtual
python3 -m venv venv
source venv/bin/activate

# Instalar dependencias
pip3 install google-genai pytest

# Configurar API key
cp config.example.py config.py
# Edita config.py con tu API key de https://aistudio.google.com/app/apikey

# Uso

python3 test_generator.py

Esto lee app.py, genera tests con Gemini y los guarda en tests_generados.py.

# Ejecutar tests generados

bash
Copy
pytest tests_generados.py -v

# Tecnologias

Python 3.9+
Google Gemini API (google-genai)
pytest
Prompt Engineering para generacion de codigo
