def registrar_dispositivo(id_dispositivo, nombre, tipo, estado, es_esencial):
    return {
        "id": id_dispositivo,
        "nombre": nombre,
        "tipo": tipo,
        "estado": estado,
        "es_esencial": es_esencial
    }

def agregar_dispositivo(lista_dispositivos, dispositivo):
    lista_dispositivos.append(dispositivo)
    return lista_dispositivos

def listar_dispositivos(lista_dispositivos):
    if not lista_dispositivos:
        print("No hay dispositivos registrados.")
        return
    for d in lista_dispositivos:
        print(f"{d['nombre']} | Estado: {d['estado']} | Esencial: {d['es_esencial']}")

def editar_dispositivo(lista_dispositivos, nombre, campo, nuevo_valor):
    for d in lista_dispositivos:
        if d["nombre"] == nombre:
            d[campo] = nuevo_valor
            return True
    return False

def eliminar_dispositivo(lista_dispositivos, nombre):
    for d in lista_dispositivos:
        if d["nombre"] == nombre:
            lista_dispositivos.remove(d)
            return True
    return False
