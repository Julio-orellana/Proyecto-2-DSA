from flask import Flask, jsonify, send_from_directory
from app.services.db_connector import DBConnector
import os

db = DBConnector()

def create_app():
    app = Flask(__name__)
    
    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def serve_react(path):
        if path.startswith('api/'):  # Ignora rutas API
            return jsonify({"error": "Ruta no encontrada"}), 404
        if not os.path.exists(os.path.join('..', 'frontend', 'dist', 'index.html')):
            return "Frontend no construido. Ejecuta 'npm run build' en /frontend.", 404
        return send_from_directory(os.path.join('..', 'frontend', 'dist'), 'index.html')

    # Cerrar conexión al finalizar
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db.close()

    # Registra las rutas API (ejemplo)
    from app.routes import api
    app.register_blueprint(api.bp, url_prefix='/api')

    return app