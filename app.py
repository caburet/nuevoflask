from flask import Flask, jsonify, request
from modelo.usuario import crear_usuario, obtener_usuario_por_id, obtener_usuarios,inicializar_usuarios
import json

app = Flask(__name__) #creamos una instancia de la clase Flask
inicializar_usuarios()

@app.route('/usuarios/', methods=["GET"])
def create_user_route():
    return jsonify(obtener_usuarios())

@app.route('/usuarios/', methods=["POST"])
def index3():
    # Handles POST requests to /ejemplos/ route
    # Retrieves name, email, password from request form 
    # Returns greeting with name, email, password
    crear_usuario("juan", "1234")
    return "algo",200