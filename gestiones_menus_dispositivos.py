def menu_dispositivos(dispositivos):
    while True:
        print("\n--- Gestión de Dispositivos ---")
        print("1. Agregar dispositivo")
        print("2. Listar dispositivos")
        print("3. Cambiar estado de un dispositivo")
        print("4. Volver")
        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                nombre = input("Nombre del dispositivo: ")
                es_esencial = input("¿Es esencial? (s/n): ").lower() == "s"
                nuevo = {"nombre": nombre, "estado": "apagado", "esencial": es_esencial}
                dispositivos.append(nuevo)
                print("✅ Dispositivo agregado.")
            case "2":
                if not dispositivos:
                    print("⚠️ No hay dispositivos registrados.")
                for d in dispositivos:
                    print(f"- {d['nombre']} ({'esencial' if d['esencial'] else 'no esencial'}) - Estado: {d['estado']}")
            case "3":
                nombre = input("Nombre del dispositivo: ")
                for d in dispositivos:
                    if d["nombre"].lower() == nombre.lower():
                        nuevo_estado = input("Nuevo estado (encendido/apagado): ")
                        d["estado"] = nuevo_estado
                        print(f"🔄 Estado de {d['nombre']} actualizado.")
                        break
                else:
                    print("⚠️ Dispositivo no encontrado.")
            case "4":
                break
            case _:
                print("❌ Opción inválida.")

def menu_modo_ahorro(dispositivos, estados_anteriores, modo_ahorro_activo):
    if not modo_ahorro_activo:
        apagados = 0
        estados_anteriores.clear()
        for d in dispositivos:
            if not d.get("esencial", False) and d["estado"] == "encendido":
                estados_anteriores[d["nombre"]] = d["estado"]
                d["estado"] = "apagado"
                apagados += 1
        print(f"💡 Modo Ahorro ACTIVADO. Se apagaron {apagados} dispositivos no esenciales.")
        return True
    else:
        restaurados = 0
        for d in dispositivos:
            if d["nombre"] in estados_anteriores:
                d["estado"] = estados_anteriores[d["nombre"]]
                restaurados += 1
        estados_anteriores.clear()
        print(f"🔋 Modo Ahorro DESACTIVADO. Se restauraron {restaurados} dispositivos.")
        return False
