from app.main import suma  
# Importamos la función a probar
# Función de prueba con pytest
def test_suma():
    assert suma(2, 3) == 5  # Esperamos que 2 + 3 sea 5
