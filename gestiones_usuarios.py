<<<<<<< HEAD
=======
def nombre_existe(usuarios, nombre):
    for usuario in usuarios:
        if usuario["nombre"] == nombre:
            return True
    return False

def email_existe(usuarios, email):
    for usuario in usuarios:
        if usuario["email"] == email:
            return True
    return False

def registrar_usuario(usuarios):
    nombre = input("Nombre: ")
    email = input("Email: ")
    if not nombre or not email:
        print("⚠️ El nombre y el email no pueden estar vacíos.")
        return
    if nombre_existe(usuarios,nombre):
        print("⚠️ El nombre ya existe, cambialo por otro")
        return
    if email_existe(usuarios,email):
        print("⚠️ El mail ya existe, cambialo por otro")
        return
    contraseña = input("Contraseña: ")
    if not contraseña.isdigit():
        print("revise de ingresar la contraseña solo con numeros")
        return
    usuarios.append({"nombre":nombre,"email":email,"contraseña":contraseña})
    return usuarios
    

    
def menu_usuarios(usuarios):
    print("\n--- Lista de Usuarios Registrados ---")
    if not usuarios:
        print("⚠️ No hay usuarios registrados.")
    for usuario in usuarios:
        print(f"- {usuario['nombre']} ({usuario['email']})")

>>>>>>> main
