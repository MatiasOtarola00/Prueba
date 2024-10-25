import mysql.connector
from mysql.connector import Error

def conectar():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            database='gestion_empleados',  
            user='root',                   
            password=''                    
        )
        return conn
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def crear_tablas():
    conn = conectar()
    if conn is None:
        print("No se pudo establecer la conexión para crear tablas.")
        return

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS empleados (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(100),
        direccion VARCHAR(255),
        telefono VARCHAR(15),
        email VARCHAR(100),
        fecha_inicio DATE,
        salario INT(100)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS departamentos (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(100),
        gerente_id INT,
        nombre_gerente VARCHAR(100),
        FOREIGN KEY (gerente_id) REFERENCES empleados(id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS proyectos (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(100),
        descripcion TEXT,
        fecha_inicio DATE
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS empleados_proyectos (
        empleado_id INT,
        proyecto_id INT,
        horas_trabajadas DECIMAL(5, 2),
        fecha DATE,
        descripcion TEXT,
        PRIMARY KEY (empleado_id, proyecto_id),
        FOREIGN KEY (empleado_id) REFERENCES empleados(id),
        FOREIGN KEY (proyecto_id) REFERENCES proyectos(id)
    )
    """)

    conn.commit()
    cursor.close()
    conn.close()
    print("Tablas creadas exitosamente")


if __name__ == "__main__":
    crear_tablas()
