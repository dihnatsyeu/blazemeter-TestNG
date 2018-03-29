import pytest


@pytest.fixture
def driver(request):
    from selenium import webdriver
    web_driver = webdriver.Firefox()
    request.addfinalizer(web_driver.close)
    return web_driver


