# tests/backend/conftest.py
import pytest
from ..app import create_app
from neo4j import GraphDatabase
from unittest.mock import Mock

# Fixtures de Flask
@pytest.fixture(scope="module")
def app():
    ...

@pytest.fixture(scope="module")
def client(app):
    ...

# Fixtures de Neo4j
@pytest.fixture(scope="module")
def neo4j_driver():
    ...

@pytest.fixture(scope="function")
def init_neo4j_data(neo4j_driver):
    ...

# Fixtures de Mocks
@pytest.fixture
def mock_external_api():
    ...

# Hooks
def pytest_collection_modifyitems(items):
    ...