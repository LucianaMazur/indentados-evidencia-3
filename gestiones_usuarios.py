def registrar_usuario(id, nombre, mail, contraseña, rol="estandar"):
    return {
        "id": id,
        "nombre": nombre,
        "mail": mail,
        "contraseña": contraseña,
        "rol": rol
    }

def agregar_usuario(lista_usuarios, usuario):
    lista_usuarios.append(usuario)
    return lista_usuarios

def inicio_sesion(lista_usuarios, mail, contraseña):
    for u in lista_usuarios:
        if u["mail"] == mail and u["contraseña"] == contraseña:
            return u
    return None

def modificar_rol(lista_usuarios, mail, nuevo_rol):
    for u in lista_usuarios:
        if u["mail"] == mail:
            u["rol"] = nuevo_rol
            return True
    return False

