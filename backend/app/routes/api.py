from flask import Blueprint, jsonify
from app import db  

bp = Blueprint('api', __name__)

@bp.route('/data')
def get_data():
    with db.driver.session() as session:
        result = session.run("MATCH (n) RETURN n LIMIT 10")
        data = [dict(record["n"]) for record in result]
    return jsonify(data)