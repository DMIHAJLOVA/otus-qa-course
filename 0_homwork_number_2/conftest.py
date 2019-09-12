import pytest
import random

@pytest.fixture(scope = "module")
def module_fixture():
    print(f"\nНачало теста")

@pytest.fixture(scope="function")
def function_fixture():
    print(f"\nТест завершен успешно!")

@pytest.fixture(scope="session")
def session_fixture(request):
    print(f"\n Завершение ({request.scope}) тестов!")

@pytest.fixture()
def random_fixture():
    return random.randint(1, 1200)


