from neo4j import GraphDatabase
import os
from dotenv import load_dotenv

load_dotenv()

driver = GraphDatabase.driver(os.environ.get("NEO4J_URI"), auth=(os.environ.get("NEO4J_USERNAME"), os.environ.get("NEO4J_PASSWORD")))

def run_query(query):
    with driver.session() as session:
        result = session.run(query)
        records = list(result)
        return records
    
query = "MATCH (u:User {nombre: 'Juan'})-[:INTERESADO_EN]->(c:Categoria)<-[:PERTENECE_A]-(a:Actividad) RETURN a.nombre AS ActividadRecomendada, c.nombre AS Categoria ORDER BY a.nombre"
activities = run_query(query)

print("**** ACTIVIDADES RECOMENDADAS PARA TI ****")
for record in activities:
    print(record["ActividadRecomendada"], "-", record["Categoria"])

query = "MATCH (u1:User {nombre: 'Juan'})-[:INTERESADO_EN]->(c:Categoria)<-[:INTERESADO_EN]-(u2:Usuario), (u2)-[:PARTICIPO_EN]->(a:Actividad) WHERE u1 <> u2 RETURN a.nombre AS ActividadPopular, COUNT(*) AS ParticipantesSimilares ORDER BY ParticipantesSimilares DESC LIMIT 5"
popular_activities = run_query(query)

print("**** ACTIVIDADES POPULARES ****")

for record in popular_activities:
    print(record["n.name"])