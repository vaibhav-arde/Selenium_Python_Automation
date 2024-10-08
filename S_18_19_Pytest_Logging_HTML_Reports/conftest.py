import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield
    print(" I will execute last")


@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["VaibhaV","Arde","vaibhavardeacademy.com"]


@pytest.fixture(params=[("chrome","VaibhaV","Arde"), ("Firefox","VaibhaV"), ("IE","VA")])
def crossBrowser(request):
    return request.param
