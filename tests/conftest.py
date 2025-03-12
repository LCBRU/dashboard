import pytest
from faker import AcademicProvider, Faker, ProjectProvider
from lbrc_flask.pytest.fixtures import *
from phage_catalogue.config import TestConfig
from phage_catalogue import create_app
from lbrc_flask.pytest.faker import LbrcFlaskFakerProvider, LbrcFileProvider
from lbrc_flask.pytest.helpers import login
from tests.faker import LookupProvider


@pytest.fixture(scope="function")
def standard_lookups(client, faker):
    faker.create_standard_lookups()


@pytest.fixture(scope="function")
def loggedin_user(client, faker):
    return login(client, faker)


@pytest.fixture(scope="function")
def app():
    return create_app(TestConfig)


@pytest.fixture(scope="function")
def faker():
    result = Faker("en_GB")
    result.add_provider(LbrcFlaskFakerProvider)
    result.add_provider(LbrcFileProvider)
    result.add_provider(LookupProvider)
    result.add_provider(AcademicProvider)
    result.add_provider(ProjectProvider)

    yield result
