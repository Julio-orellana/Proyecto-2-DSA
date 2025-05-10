from flask import Flask, jsonify, send_from_directory
from services.db_connector import DBConnector
import os

# Inicialización de la app y la base de datos
app = Flask(__name__, static_folder=None) 
db = DBConnector()

# Ruta principal que sirve el frontend React
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_react(path):
    # Si la ruta comienza con /api se ignora y se devuelve un error 404
    if path.startswith('api/'):
        return jsonify({"error": "Ruta API no encontrada"}), 404
    
    # Verificar si existe el archivo solicitado para evitar errores en producción
    file_path = os.path.join('..', 'frontend', 'dist', path)
    if os.path.exists(file_path) and path != '':
        return send_from_directory(os.path.join('..', 'frontend', 'dist'), path)
    
    # Servir index.html para todas las demás rutas (para React Router)
    return send_from_directory(os.path.join('..', 'frontend', 'dist'), 'index.html')

# Rutas de API
@app.route("/api/data")
def get_data():
    return jsonify({"message": "Hola desde Flask!"})

@app.route("/api/recommend")
def get_recommendations():
    try:
        with db.driver.session() as session:
            result = session.run("""
                MATCH (u:User)-[:INTERESADO_EN]->(c:Categoria)<-[:PERTENECE_A]-(a:Actividad)
                WHERE u.id = $user_id  
                RETURN  a.nombre AS actividad, 
                        a.duracion AS duracion,
                        c.nombre AS categoria
                        a.distancia AS distancia,
                ORDER BY a.puntuacion DESC
                LIMIT 5
            """, user_id="user_123")  # Reemplaza con parámetro real
            recommendations = [{
                "actividad": record["actividad"],
                "duracion": record["duracion"],
                "categoria": record["categoria"],
                "distancia": record["distancia"]
            } for record in result]
            return jsonify(recommendations)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Cerrar conexión a la base de datos al finalizar
@app.teardown_appcontext
def shutdown_session(exception=None):
    db.close()

if __name__ == "__main__":
    app.run(debug=True)