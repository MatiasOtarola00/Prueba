import _mysql_connector
from models.db import conectar

def crear_empleado(nombre, direccion, telefono, email, fecha_inicio, salario):
    """Función para crear un nuevo empleado."""
    conn = conectar()
    if conn is None:
        return
    cursor = conn.cursor()
    cursor.execute("INSERT INTO empleados (nombre, direccion, telefono, email, fecha_inicio, salario) VALUES (%s, %s, %s, %s, %s, %s)", (nombre, direccion, telefono, email, fecha_inicio, salario))
    conn.commit()
    cursor.close()
    conn.close()
    print("Empleado creado exitosamente.")

def obtener_empleados():
    """Función para obtener todos los empleados."""
    conn = conectar()
    if conn is None:
        return []
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM empleados")
    empleados = cursor.fetchall()
    cursor.close()
    conn.close()
    return empleados

def buscar_empleado_por_id(empleado_id):
    """Función para buscar un empleado por su ID."""
    conn = conectar()
    if conn is None:
        return None
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM empleados WHERE id = %s", (empleado_id,))
    empleado = cursor.fetchone()
    cursor.close()
    conn.close()
    return empleado

def actualizar_empleado(empleado_id, nombre, direccion, telefono, email, fecha_inicio, salario):
    """Función para actualizar la información de un empleado."""
    conn = conectar()
    if conn is None:
        return
    cursor = conn.cursor()
    consulta = """
        UPDATE empleados
        SET nombre = %s, direccion = %s, telefono = %s, email = %s, fecha_inicio = %s, salario = %s
        WHERE id = %s
    """
    cursor.execute(consulta, (nombre, direccion, telefono, email, fecha_inicio, salario, empleado_id))
    conn.commit()
    cursor.close()
    conn.close()
    print("Empleado actualizado exitosamente.")

def eliminar_empleado(empleado_id):
    """Función para eliminar un empleado por su ID."""
    conn = conectar()
    if conn is None:
        return
    cursor = conn.cursor()
    cursor.execute("DELETE FROM empleados WHERE id = %s", (empleado_id,))
    conn.commit()
    cursor.close()
    conn.close()
    print("Empleado eliminado exitosamente.")
