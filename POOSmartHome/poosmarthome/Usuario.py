    def __init__(self, user_id: str, nombre: str, mail: str, rol: str = "estandar"):
        self.user_id = user_id
        self.nombre = nombre
        self.mail = mail
        self.rol = rol
        self.automatizaciones: List[Automatizacion] = []
        self.registros: List[RegistroActividad] = []

    def crear_automatizacion(self, automatizacion):
        automatizacion.propietario = self
        self.automatizaciones.append(automatizacion)

    def eliminar_automatizaciones(self):
        self.automatizaciones.clear()

    def agregar_registro(self, registro):
        registro.usuario = self
        self.registros.append(registro)

    def __repr__(self):
        return f"Usuario({self.user_id}, {self.nombre})"
