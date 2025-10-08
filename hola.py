# Registro de Claves Seguras
user_key = input("Ingresa tu clave personal: ")
with open("user_key.txt", "w") as file:
    file.write(user_key)
print(f"Clave '{user_key}' guardada exitosamente en user_key.txt")