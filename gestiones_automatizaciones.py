def crear_automatizacion(nombre, dispositivo, hora):
    return {
        "nombre": nombre,
        "dispositivo": dispositivo,
        "hora": hora,
        "activa": False
    }

def activar_automatizacion(automatizacion):
    automatizacion["activa"] = True
    print(f"Automatización '{automatizacion['nombre']}' activada para {automatizacion['dispositivo']} a las {automatizacion['hora']}")

def consultar_automatizacion(automatizacion):
    estado = "activa" if automatizacion["activa"] else "inactiva"
    print(f"Automatización '{automatizacion['nombre']}' para {automatizacion['dispositivo']} a las {automatizacion['hora']} está {estado}")
