# Lista de usuarios
import csv
import os


usuarios = []
id_usuario = 1  # Variable para asignar IDs únicos a los usuarios

# Crea un nuevo usuario
def inicializar_usuarios():
    global id_usuario
    if os.path.exists('usuarios.csv'):
        id_usuario=importar_desde_csv()
    else:
        # Agrega un usuario a la lista con un ID único
        usuarios.append({
            "id": id_usuario,
            "nombre de usuario": "juan",
            "contraseña": "12343",
        })
        id_usuario += 1
        # Agrega un usuario a la lista con un ID único
        usuarios.append({
            "id": id_usuario,
            "nombre de usuario": "pedro",
            "contraseña": "sads122",
        })
        id_usuario += 1

# Crea un nuevo usuario
def crear_usuario(nombre_usuario, contraseña):
    global id_usuario
    # Agrega el usuario a la lista con un ID único
    usuarios.append({
        "id": id_usuario,
        "nombre de usuario": nombre_usuario,
        "contraseña": contraseña,
    })
    id_usuario += 1
    exportar_a_csv()
    # Devuelve el usuario recién creado
    return usuarios[-1]

# Obtiene un usuario por ID
def obtener_usuario_por_id(id_usuario):
    # Recorre la lista de usuarios
    for usuario in usuarios:
        # Si el ID de usuario coincide, devuelve el usuario
        if usuario["id"] == id_usuario:
            return usuario
    # Devuelve None si no se encuentra el usuario
    return None

# Obtiene todos los usuarios
def obtener_usuarios():
    # Devuelve la lista de usuarios
    return usuarios

def editar_usuario_por_id(id_usuario, nuevo_nombre_usuario, nueva_contraseña):
    # Recorre la lista de usuarios
    for usuario in usuarios:
        # Si el ID de usuario coincide, actualiza el nombre de usuario y la contraseña
        if usuario["id"] == id_usuario:
            usuario["nombre de usuario"] = nuevo_nombre_usuario
            usuario["contraseña"] = nueva_contraseña
            exportar_a_csv()
            return usuario
    # Devuelve None si no se encuentra el usuario
    return None

# Elimina un usuario por ID
def eliminar_usuario_por_id(id_usuario):
    global usuarios
    # Crea una nueva lista sin el usuario a eliminar
    usuarios = [usuario for usuario in usuarios if usuario["id"] != id_usuario]
    exportar_a_csv()
# Exportar datos a un archivo CSV
def exportar_a_csv():
    with open('usuarios.csv', 'w', newline='') as csvfile:
        campo_nombres = ['id', 'nombre de usuario', 'contraseña']
        writer = csv.DictWriter(csvfile, fieldnames=campo_nombres)
        writer.writeheader()
        for usuario in usuarios:
            writer.writerow(usuario)

# Importar datos desde un archivo CSV
def importar_desde_csv():
    global usuarios
    usuarios = []  # Limpiamos la lista de usuarios antes de importar desde el archivo CSV
    with open('usuarios.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Convertimos el ID de cadena a entero
            row['id'] = int(row['id'])
            usuarios.append(row) 
    if len(usuarios)>0:
        return usuarios[-1]["id"]+1
    else:
        return 1