from flask import Flask, jsonify, request
from modelo.usuario import crear_usuario, obtener_usuario_por_id, obtener_usuarios,inicializar_usuarios
import json

app = Flask(__name__) #creamos una instancia de la clase Flask
inicializar_usuarios()

@app.route('/usuarios/', methods=["GET"])
def obtener_usuarios_json():
    return jsonify(obtener_usuarios())

@app.route('/usuarios/', methods=["POST"])
def crear_usuario_json():
    usuario = json.loads(request.data)
    usuario_creado=crear_usuario(usuario["nombre_de_usuario"], usuario["contraseña"])
    return jsonify(usuario_creado),200