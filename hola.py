# # Registro de Claves Seguras
import os
user_key = os.getenv('USER_KEY', 'default_clave')
with open("user_key.txt", "w") as file:
    file.write(user_key)
print(f"Clave '{user_key}' guardada exitosamente en user_key.txt")
print("Prueba de GitHub Actions")print('Nueva prueba')
