from controllers.empleado_controller import crear_empleado, obtener_empleados
from controllers.departamento_controller import crear_departamento, obtener_departamentos, actualizar_departamento, eliminar_departamento
from controllers.proyecto_controller import crear_proyecto, obtener_proyectos, actualizar_proyecto, eliminar_proyecto, asignar_empleado_a_proyecto, obtener_empleados_por_proyecto
from models.db import crear_tablas

def mostrar_menu():
    crear_tablas()
    
    while True:
        print("\n=== Menú Principal ===")
        print("1. Registrar empleado")
        print("2. Ver empleados")
        print("3. Registrar departamento")
        print("4. Ver departamentos")
        print("5. Actualizar departamento")
        print("6. Eliminar departamento")
        print("7. Registrar proyecto")
        print("8. Ver proyectos")
        print("9. Actualizar proyecto")
        print("10. Eliminar proyecto")
        print("11. Asignar empleado a proyecto")
        print("12. Ver empleados asignados a un proyecto")
        print("13. Salir")

        opcion = input("Seleccione una opción: ")

        # Opciones para empleados
        if opcion == '1':
            nombre = input("Nombre: ")
            direccion = input("Dirección: ")
            telefono = input("Teléfono: ")
            email = input("Email: ")
            fecha_inicio = input("Fecha de inicio (YYYY-MM-DD): ")
            salario = input("Salario: ")
            crear_empleado(nombre, direccion, telefono, email, fecha_inicio, salario)
        elif opcion == '2':
            empleados = obtener_empleados()
            for emp in empleados:
                print(emp)

        # Opciones para departamentos
        elif opcion == '3':
            nombre = input("Nombre del departamento: ")
            nombre_gerente = input("Gerente: ")
            crear_departamento(nombre, nombre_gerente)
        elif opcion == '4':
            departamentos = obtener_departamentos()
            for dep in departamentos:
                print(dep)
        elif opcion == '5':
            nombre = input("Nuevo nombre de Departamento: ")
            gerente = input("Nuevo gerente: ")
            actualizar_departamento(nombre, gerente)
        elif opcion == '6':
            nombre = input("Departamento a eliminar: ")
            eliminar_departamento(nombre)
        # Opciones para proyectos
        elif opcion == '7':
            nombre = input("Nombre del proyecto: ")
            descripcion = input("Descripción: ")
            fecha_inicio = input("Fecha de inicio (YYYY-MM-DD): ")
            crear_proyecto(nombre, descripcion, fecha_inicio)
        elif opcion == '8':
            proyectos = obtener_proyectos()
            for proyecto in proyectos:
                print(proyecto)
        elif opcion == '9':
            nombre = input("Nombre del proyecto a actualizar: ")
            nuevo_nombre = input("Nuevo nombre del proyecto: ")
            descripcion = input("Nueva descripción: ")
            fecha_inicio = input("Nueva fecha de inicio (YYYY-MM-DD): ")
            actualizar_proyecto(nombre, nuevo_nombre, descripcion, fecha_inicio)
        elif opcion == '10':
            nombre = input("Nombre del proyecto a eliminar: ")
            eliminar_proyecto(nombre)

        # Asignación de empleados a proyectos
        elif opcion == '11':
            empleado_id = input("ID del empleado: ")
            proyecto_id = input("ID del proyecto: ")
            asignar_empleado_a_proyecto(empleado_id, proyecto_id)
        elif opcion == '12':
            proyecto_id = input("ID del proyecto: ")
            empleados_asignados = obtener_empleados_por_proyecto(proyecto_id)
            for emp in empleados_asignados:
                print(emp)

        # Salida
        elif opcion == '13':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")
