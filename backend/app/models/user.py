from .base_model import BaseModel

class User(BaseModel):
    def create(self, user_id: int, name: str, email: str):
        query: str = """
        CREATE (u:User {id: $user_id, name: $name, email: $email})
        RETURN u
        """
        return self._execute_query(query, {"user_id": user_id, "name": name, "email": email})

    def get_interests(self, user_id: int):
        query: str = """
        MATCH (u:User {id: $user_id})-[:INTERESADO_EN]->(c:Categoria)
        RETURN c
        """
        return self._execute_query(query, {"user_id": user_id})