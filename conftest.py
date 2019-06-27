from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ChromeOptions
import pytest


@pytest.fixture(scope='function', autouse=True)
def driver():
    """Create driver object"""
    options = ChromeOptions()
    options.add_argument("no-sandbox")
    options.accept_untrusted_certs = True
    options.assume_untrusted_cert_issuer = True
    options.add_argument("--disable-infobars")
    options.add_argument("--headless")
    driver_ = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    yield driver_
    driver_.quit()

