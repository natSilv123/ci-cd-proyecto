import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.main import suma

# Función de prueba con pytest
def test_suma():
    assert suma(2, 3) == 5  # Esperamos que 2 + 3 sea 5
