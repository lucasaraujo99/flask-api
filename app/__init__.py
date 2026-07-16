from flask import Flask
from pymongo import MongoClient

db = None

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    global db # modificar uma variável global dentro de uma função

    try:
        client = MongoClient(app.config['MONGO_URI']) # representa a conexão com o servidor MongoDB
        db = client.get_default_database() # recupera o database padrão definido no URI
        # alternativamente: db = client.get_database("stylesync")

    except Exception as e:
        print(f"Erro ao realizar a conexao com o banco de dados: {e}")

    from .routes.main import main_bp
    app.register_blueprint(main_bp)

    return app