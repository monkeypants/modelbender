import pytest

from modelbender.app import create_app
from modelbender.flask_settings import TestConfig

@pytest.yield_fixture(scope="function")
def app():
    return create_app(TestConfig)
