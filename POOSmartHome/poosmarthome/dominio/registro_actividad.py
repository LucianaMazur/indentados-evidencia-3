class RegistroActividad:
    def __init__(self, id=0, usuario='', accion='', detalle='', fecha=None):
        self.id = id
        self.usuario = usuario
        self.accion = accion
        self.detalle = detalle
        self.fecha = fecha

    @staticmethod
    def from_row(row):
        if not row:
            return None
        return RegistroActividad(id=row[0], fecha=row[1], usuario=row[2], accion=row[3], detalle=row[4])