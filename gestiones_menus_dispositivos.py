def menu_dispositivos(dispositivos):
    while True:
        print("\n" + "="*30)
        print("       Gestión de Dispositivos       ")
        print("="*30)
        print("1. Agregar dispositivo")
        print("2. Listar dispositivos")
        print("3. Cambiar estado de un dispositivo")
        print("4. Volver")
        opcion = input("Seleccione una opción: ").strip()

        match opcion:
            case "1":
                nombre = input("Nombre del dispositivo: ").strip()
                es_esencial = input(
                    "¿Es esencial? (s/n): ").strip().lower() == "s"
                nuevo = {"nombre": nombre, "estado": "apagado",
                         "esencial": es_esencial}
                dispositivos.append(nuevo)
                print(f"✅ Dispositivo '{nombre}' agregado.")
            case "2":
                if not dispositivos:
                    print("⚠️ No hay dispositivos registrados.")
                else:
                    print("\nLista de dispositivos:")
                    print(f"{'Nombre':<20} | {'Esencial':<10} | {'Estado':<10}")
                    print("-"*45)
                    for d in dispositivos:
                        esencial_text = "Sí" if d['esencial'] else "No"
                        print(
                            f"{d['nombre']:<20} | {esencial_text:<10} | {d['estado']:<10}")
            case "3":
                nombre = input("Nombre del dispositivo a modificar: ").strip()
                for d in dispositivos:
                    if d["nombre"].lower() == nombre.lower():
                        nuevo_estado = input(
                            "Nuevo estado (encendido/apagado): ").strip().lower()
                        if nuevo_estado in ["encendido", "apagado"]:
                            d["estado"] = nuevo_estado
                            print(
                                f"🔄 Estado de '{d['nombre']}' actualizado a '{nuevo_estado}'.")
                        else:
                            print(
                                "❌ Estado inválido. Debe ser 'encendido' o 'apagado'.")
                        break
                else:
                    print("⚠️ Dispositivo no encontrado.")
            case "4":
                print("↩️ Volviendo al menú anterior...")
                break
            case _:
                print("❌ Opción inválida. Por favor ingrese una opción válida.")


def menu_modo_ahorro(dispositivos, estados_anteriores, modo_ahorro_activo):
    print("\n" + "="*30)
    print("          Modo Ahorro Energía          ")
    print("="*30)

    if not modo_ahorro_activo:
        apagados = 0
        estados_anteriores.clear()
        for d in dispositivos:
            if not d.get("esencial", False) and d["estado"] == "encendido":
                estados_anteriores[d["nombre"]] = d["estado"]
                d["estado"] = "apagado"
                apagados += 1
        print(
            f"💡 Modo Ahorro ACTIVADO. Se apagaron {apagados} dispositivos no esenciales.")
        print("➡️ Los dispositivos esenciales permanecen encendidos.")
        print("="*30)
        return True
    else:
        restaurados = 0
        for d in dispositivos:
            if d["nombre"] in estados_anteriores:
                d["estado"] = estados_anteriores[d["nombre"]]
                restaurados += 1
        estados_anteriores.clear()
        print(
            f"🔋 Modo Ahorro DESACTIVADO. Se restauraron {restaurados} dispositivos.")
        print("="*30)
        return False
