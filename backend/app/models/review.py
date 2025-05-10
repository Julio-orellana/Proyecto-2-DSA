from .base_model import BaseModel

class Review(BaseModel):
    def create(self, user_id: int, activity_id: int, rating: float, comment: str):
        query: str = """
        MATCH (u:User {id: $user_id}), (a:Actividad {id: $activity_id})
        CREATE (u)-[r:REVIEWED {rating: $rating, comment: $comment}]->(a)
        RETURN r
        """
        return self._execute_query(query, {
            "user_id": user_id,
            "activity_id": activity_id,
            "rating": rating,
            "comment": comment
        })