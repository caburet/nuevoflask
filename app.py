from flask import Flask, jsonify, request
from modelo.usuario import crear_usuario, obtener_usuario_por_id, obtener_usuarios,inicializar_usuarios
import json

app = Flask(__name__) #creamos una instancia de la clase Flask
listadeejemplos = ["algoritmos", "programacion", "python"]
inicializar_usuarios()

@app.route('/')
def index():
    return '<h1>Hola!</h1>'


@app.route('/ejemplos/', methods=["GET"])
def create_user_route():
    
    return jsonify(obtener_usuarios())
@app.route('/ejemplos/', methods=["POST"])
def index3():
    # Handles POST requests to /ejemplos/ route
    # Retrieves name, email, password from request form 
    # Returns greeting with name, email, password
    crear_usuario("juan", "1234")
    return "algo",200