import pytest
from _pytest import python
from selenium import webdriver


@pytest.fixture(scope="class")

def setup(request):
    driver = webdriver.Chrome()
    driver.get("http://automationpractice.com/index.php")
    driver.implicitly_wait(5)
    request.cls.driver=driver#assinging local driver of this fixture to the class driver
    yield
    driver.close()

