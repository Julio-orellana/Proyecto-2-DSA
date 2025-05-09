from neo4j import GraphDatabase
from app.config import Config 

class DBConnector:
    def __init__(self):
        self.driver = GraphDatabase.driver(
            Config.NEO4J_URI,
            auth=(Config.NEO4J_USERNAME, Config.NEO4J_PASSWORD)
        )

    def close(self):
        self.driver.close()