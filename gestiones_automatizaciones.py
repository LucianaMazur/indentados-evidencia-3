def modo_ahorro(dispositivos, estados_anteriores, activo):
    print("\n" + "="*30)
    print("          MODO AHORRO           ")
    print("="*30)

    if not activo:
        estados_anteriores.clear()
        for d in dispositivos:
            if not d.get("esencial", False) and d["estado"] == "encendido":
                estados_anteriores[d["nombre"]] = d["estado"]
                d["estado"] = "apagado"
        print("💡 Modo Ahorro ACTIVADO.")
        print("➡️ Dispositivos no esenciales apagados.")
    else:
        for d in dispositivos:
            if d["nombre"] in estados_anteriores:
                d["estado"] = estados_anteriores[d["nombre"]]
        estados_anteriores.clear()
        print("🔋 Modo Ahorro DESACTIVADO.")
        print("➡️ Estados previos restaurados.")

    print("="*30)
    return not activo


def programar_cafetera(dispositivos):
    print("\n" + "-"*30)
    print("       Programar Cafetera       ")
    print("-"*30)

    for d in dispositivos:
        if d["nombre"].lower() == "cafetera":
            d["estado"] = "encendido"
            print("☕ Cafetera encendida (simulado 7:00 am).")
            print("-"*30)
            return

    print("⚠️ No hay cafetera registrada.")
    print("-"*30)


def control_parental(dispositivos):
    for d in dispositivos:
        if "tv" in d["nombre"].lower() or "play" in d["nombre"].lower():
            d["estado"] = "apagado"
    print("🔒 Control parental aplicado. Dispositivos de entretenimiento apagados.")


def automatizaciones_usuario_estandar(dispositivos, estados_anteriores, modo_ahorro_activo):
    while True:
        print("\n" + "-"*30)
        print("      Automatizaciones Usuario      ")
        print("-"*30)
        print("1. Activar/Desactivar Modo Ahorro")
        print("2. Programar cafetera")
        print("3. Volver")
        opcion = input("Seleccione una opción: ")

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
        print("\n" + "="*35)
        print("         Automatizaciones Admin         ")
        print("="*35)
        print("1. Activar/Desactivar Modo Ahorro")
        print("2. Programar cafetera")
        print("3. Activar control parental")
        print("4. Volver")
        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                modo_ahorro_activo = modo_ahorro(
                    dispositivos, estados_anteriores, modo_ahorro_activo)
            case "2":
                programar_cafetera(dispositivos)
            case "3":
                control_parental(dispositivos)
            case "4":
                return modo_ahorro_activo
            case _:
                print("❌ Opción inválida.")
