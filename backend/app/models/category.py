from .base_model import BaseModel

class Category(BaseModel):
    def get_all(self):
        query: str = "MATCH (c:Categoria) RETURN c"
        return self._execute_query(query)

    def add_user_interest(self, user_id: int, category_id: int):
        query: str = """
        MATCH (u:User {id: $user_id}), (c:Categoria {id: $category_id})
        MERGE (u)-[:INTERESADO_EN]->(c)
        """
        return self._execute_query(query, {"user_id": user_id, "category_id": category_id})