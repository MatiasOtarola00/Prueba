import mysql.connector
from models.db import conectar

def crear_proyecto(nombre, descripcion, fecha_inicio):
    conn = conectar()
    if conn is None:
        return
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO proyectos (nombre, descripcion, fecha_inicio)
        VALUES (%s, %s, %s)
    """, (nombre, descripcion, fecha_inicio))
    conn.commit()
    cursor.close()
    conn.close()

def obtener_proyectos():
    conn = conectar()
    if conn is None:
        return []
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM proyectos")
    proyectos = cursor.fetchall()
    cursor.close()
    conn.close()
    return proyectos

def buscar_proyecto_por_nombre(nombre):
    conn = conectar()
    if conn is None:
        return None
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM proyectos WHERE nombre = %s", (nombre,))
    proyecto = cursor.fetchone()
    cursor.close()
    conn.close()
    return proyecto

def actualizar_proyecto(nombre, nuevo_nombre, descripcion, fecha_inicio):
    conn = conectar()
    if conn is None:
        return
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE proyectos
        SET nombre = %s, descripcion = %s, fecha_inicio = %s
        WHERE nombre = %s
    """, (nuevo_nombre, descripcion, fecha_inicio, nombre))
    conn.commit()
    cursor.close()
    conn.close()

def eliminar_proyecto(nombre):
    conn = conectar()
    if conn is None:
        return
    cursor = conn.cursor()
    cursor.execute("DELETE FROM proyectos WHERE nombre = %s", (nombre,))
    conn.commit()
    cursor.close()
    conn.close()

def asignar_empleado_a_proyecto(empleado_id, proyecto_id):
    conn = conectar()
    if conn is None:
        return
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO empleado_proyecto (empleado_id, proyecto_id)
        VALUES (%s, %s)
    """, (empleado_id, proyecto_id))
    conn.commit()
    cursor.close()
    conn.close()

def eliminar_asignacion_empleado_proyecto(empleado_id, proyecto_id):
    conn = conectar()
    if conn is None:
        return
    cursor = conn.cursor()
    cursor.execute("""
        DELETE FROM empleado_proyecto
        WHERE empleado_id = %s AND proyecto_id = %s
    """, (empleado_id, proyecto_id))
    conn.commit()
    cursor.close()
    conn.close()

def obtener_empleados_por_proyecto(proyecto_id):
    conn = conectar()
    if conn is None:
        return []
    cursor = conn.cursor()
    cursor.execute("""
        SELECT e.* FROM empleados e
        INNER JOIN empleado_proyecto ep ON e.id = ep.empleado_id
        WHERE ep.proyecto_id = %s
    """, (proyecto_id,))
    empleados = cursor.fetchall()
    cursor.close()
    conn.close()
    return empleados
