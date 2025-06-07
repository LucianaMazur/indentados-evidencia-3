def modo_ahorro(dispositivos, estados_anteriores, activo):
    if not activo:
        estados_anteriores.clear()
        for d in dispositivos:
            if not d.get("esencial", False) and d["estado"] == "encendido":
                estados_anteriores[d["nombre"]] = d["estado"]
                d["estado"] = "apagado"
        print("💡 Modo Ahorro ACTIVADO.")
        return True
    else:
        for d in dispositivos:
            if d["nombre"] in estados_anteriores:
                d["estado"] = estados_anteriores[d["nombre"]]
        estados_anteriores.clear()
        print("🔋 Modo Ahorro DESACTIVADO.")
        return False

def programar_cafetera(dispositivos):
    for d in dispositivos:
        if d["nombre"].lower() == "cafetera":
            d["estado"] = "encendido"
            print("☕ Cafetera encendida (simulado 7:00 am).")
            return
    print("⚠️ No hay cafetera registrada.")

def control_parental(dispositivos):
    for d in dispositivos:
        if "tv" in d["nombre"].lower() or "play" in d["nombre"].lower():
            d["estado"] = "apagado"
    print("🔒 Control parental aplicado. Dispositivos de entretenimiento apagados.")

def automatizaciones_usuario_estandar(dispositivos, estados_anteriores, modo_ahorro_activo):
    while True:
        print("\n--- Automatizaciones Usuario ---")
        print("1. Activar/Desactivar Modo Ahorro")
        print("2. Programar cafetera")
        print("3. Volver")
        opcion = input("Opción: ")

        match opcion:
            case "1":
                return modo_ahorro(dispositivos, estados_anteriores, modo_ahorro_activo)
            case "2":
                programar_cafetera(dispositivos)
            case "3":
                return modo_ahorro_activo
            case _:
                print("❌ Opción inválida.")

def automatizaciones_admin(dispositivos, usuario, estados_anteriores, modo_ahorro_activo):
    while True:
        print("\n--- Automatizaciones Admin ---")
        print("1. Activar/Desactivar Modo Ahorro")
        print("2. Programar cafetera")
        print("3. Activar control parental")
        print("4. Volver")
        opcion = input("Opción: ")

        match opcion:
            case "1":
                modo_ahorro_activo = modo_ahorro(dispositivos, estados_anteriores, modo_ahorro_activo)
            case "2":
                programar_cafetera(dispositivos)
            case "3":
                control_parental(dispositivos)
            case "4":
                return modo_ahorro_activo
            case _:
                print("❌ Opción inválida.")
