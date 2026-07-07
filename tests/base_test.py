import allure
from allure_commons.types import Severity

class BaseTest:
    """Parent class for all test classes. Handel Allure setup automatically.
    mo need to add @allure.story or @allure.severity in every test"""
    # Default severity - override in child class
    severity = Severity.NORMAL

    def setup_method(self, method):
        """Runs automatically before every test. Sets story and severity dynamically"""
        # Auto severity from class variable
        allure.dynamic.severity(self.severity)
        # Auto story from test method name
        # test_valid_login-> "Valid Login"
        story = method.__name__ \
            .replace("test_", "") \
            .replace("_", " ") \
            .title()
        allure.dynamic.story(story)
