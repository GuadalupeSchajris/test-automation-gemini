from google import genai
from config import API_KEY, MODEL_NAME

# Crear cliente nuevo
client = genai.Client(api_key=API_KEY)

def generar_tests(codigo_python: str) -> str:
    """
    Recibe código Python y devuelve tests unitarios generados por Gemini.
    """
    # Construimos el prompt por fuera para evitar problemas con llaves
    instrucciones = """Eres un experto en testing de software. Genera tests unitarios en Python 
usando pytest para el siguiente código. 

REGLAS:
- Usa pytest
- Incluye casos normales, edge cases y manejo de errores
- Agrega docstrings descriptivos
- Nombra las funciones de test claramente
- No modifiques el código original, solo genera los tests

Devuelve SOLO el código de los tests, sin explicaciones adicionales.

CÓDIGO A TESTEAR:
"""
    
    prompt = instrucciones + "```python\n" + codigo_python + "\n```"
    
    respuesta = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )
    return respuesta.text

def guardar_tests(tests_generados: str, nombre_archivo: str = "tests_generados.py"):
    """
    Guarda los tests en un archivo .py
    """
    # Limpiar markdown si Gemini lo agrega
    codigo_limpio = tests_generados.replace("```python", "").replace("```", "").strip()
    
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write(codigo_limpio)
    
    print(f"✅ Tests guardados en: {nombre_archivo}")
    return nombre_archivo

if __name__ == "__main__":
    # Leer el código de app.py
    with open("app.py", "r", encoding="utf-8") as f:
        codigo = f.read()
    
    print("🤖 Generando tests con Gemini...")
    tests = generar_tests(codigo)
    guardar_tests(tests)