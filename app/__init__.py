from flask import Flask
from app.services.db_connector import DBConnector

db = DBConnector()  # Instancia única de la conexión

def create_app():
    app = Flask(__name__)
    
    # Cerrar conexión al finalizar
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db.close()

    return app