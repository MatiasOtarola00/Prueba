import mysql.connector
from models.db import conectar

def crear_departamento(nombre, nombre_gerente, gerente_id=None):
    conn = conectar()
    if conn is None:
        return
    cursor = conn.cursor()

    cursor.execute ("INSERT INTO departamentos (nombre, nombre_gerente, gerente_id) VALUES (%s,%s,%s)", (nombre, nombre_gerente, gerente_id))
    conn.commit()
    cursor.close()
    conn.close()
    print("Departamento creado exitosamente.")

def obtener_departamentos():
    conn = conectar()
    if conn is None:
        return []
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM departamentos")
    departamentos = cursor.fetchall()
    cursor.close()
    conn.close()
    return departamentos

def actualizar_departamento(departamento_id, nombre, gerente_id=None):
    conn = conectar()
    if conn is None:
        return
    cursor = conn.cursor()
    consulta = """
        UPDATE departamentos
        SET nombre = %s, gerente_id = %s
        WHERE id = %s
    """
    cursor.execute(consulta, (nombre, gerente_id, departamento_id))
    conn.commit()
    cursor.close()
    conn.close()
    print("Departamento actualizado exitosamente.")

def eliminar_departamento(nombre):
    conn = conectar()
    if conn is None:
        return
    cursor = conn.cursor()
    cursor.execute("DELETE FROM departamentos WHERE id = %s", (nombre,))
    conn.commit()
    cursor.close()
    conn.close()
    print("Departamento eliminado exitosamente.")
