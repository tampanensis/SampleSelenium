import allure

class TestSelenium:

    @allure.title("Sample")
    def test_first(self, driver):
        driver.get('https://github.com/')
        assert 'GitHub' in driver.title
