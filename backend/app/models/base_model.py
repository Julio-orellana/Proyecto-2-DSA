from neo4j import GraphDatabase
from pydantic import BaseModel as PydanticBaseModel

class BaseModel(PydanticBaseModel):
    def __init__(self, driver):
        self.driver: GraphDatabase.driver = driver 

    def _execute_query(self, query, parameters=None):
        with self.driver.session() as session:
            return session.run(query, parameters)