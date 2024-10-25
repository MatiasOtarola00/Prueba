class RegistroTiempo:
    def __init__(self, empleado_id, proyecto_id, horas_trabajadas, fecha, descripcion):
        self.empleado_id = empleado_id         # ID del empleado asociado
        self.proyecto_id = proyecto_id         # ID del proyecto asociado
        self.horas_trabajadas = horas_trabajadas
        self.fecha = fecha
        self.descripcion = descripcion