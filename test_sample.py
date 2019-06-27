import pytest


class TestSelenium:
    def test_first(self, driver):
        driver.get('https://github.com/')
        assert 'GitHub' in driver.title
