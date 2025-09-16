class Gestor:
    def __init__(self):
        self.usuarios = {}
        self.dispositivos = {}

    def agregar_usuario(self, usuario):
        self.usuarios[usuario.user_id] = usuario

    def agregar_dispositivo(self, dispositivo):
        self.dispositivos[dispositivo.device_id] = dispositivo

    def asignar_dispositivo(self, usuario_id, device_id, fecha=None):
        usuario = self.usuarios[usuario_id]
        dispositivo = self.dispositivos[device_id]
        asociación = UsuarioDispositivo(usuario, dispositivo, fecha)
        return asociación

    def eliminar_usuario(self, user_id):
        usuario = self.usuarios.pop(user_id, None)
        if usuario:
            usuario.eliminar_automatizaciones()
        return usuario

