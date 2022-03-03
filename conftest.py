import pytest
from fixture.application import Application


# not adding scope="session" into the fixture on purpose because it causes an error when running tests
@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
