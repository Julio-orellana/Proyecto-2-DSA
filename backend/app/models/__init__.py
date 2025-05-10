from neo4j import GraphDatabase 
from .user import User
from .activity import Activity
from .category import Category
from .review import Review 
from app.config import Config

# Inicialización del driver de Neo4j
driver = GraphDatabase.driver(Config.NEO4J_URI, auth=(Config.NEO4J_USERNAME, Config.NEO4J_PASSWORD))

# Inicialización de los modelos para su uso en la aplicación
user_model = User(driver)
activity_model = Activity(driver)
category_model = Category(driver)
review_model = Review(driver)

# Se exportan los modelos para su uso en otras partes de la aplicación y el driver para usos específicos.
__all__ = ['user_model', 'activity_model', 'category_model', 'review_model', 'driver']