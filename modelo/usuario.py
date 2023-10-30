# Lista de usuarios
usuarios = []
id_usuario = 1  # Variable para asignar IDs únicos a los usuarios

# Crea un nuevo usuario
def inicializar_usuarios():
    global id_usuario
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
            return usuario
    # Devuelve None si no se encuentra el usuario
    return None

# Elimina un usuario por ID
def eliminar_usuario_por_id(id_usuario):
    global usuarios
    # Crea una nueva lista sin el usuario a eliminar
    usuarios = [usuario for usuario in usuarios if usuario["id"] != id_usuario]
