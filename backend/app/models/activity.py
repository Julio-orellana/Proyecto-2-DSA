from .base_model import BaseModel

class Activity(BaseModel):
    def recommend_by_category(self, category_id: int, limit:int=5):
        query = """
        MATCH (a:Actividad)-[:PERTENECE_A]->(c:Categoria {id: $category_id})
        RETURN a
        ORDER BY a.puntuacion DESC
        LIMIT $limit
        """
        return self._execute_query(query, {"category_id": category_id, "limit": limit})