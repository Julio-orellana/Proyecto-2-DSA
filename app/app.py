from flask import Flask, render_template, jsonify
from services.db_connector import DBConnector

app = Flask(__name__)
db = DBConnector()

# Ruta para página principal
@app.route("/")
def home():
    return render_template("index.html")

# Ruta de prueba
@app.route("/api/data")
def get_data():
    return jsonify({"message": "Hola desde Flask!"})

if __name__ == "__main__":
    app.run(debug=True)