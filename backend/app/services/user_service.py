from app.models.user import User

class UserService:
    def __init__(self, driver):
        self.model = User(driver)

    def register_user(self, user_data):
        return self.model.create(
            user_id=user_data["id"],
            name=user_data["name"],
            email=user_data["email"]
        )
    
    def get_user_interests(self, user_id):
        return self.model.get_interests(user_id)
    
    