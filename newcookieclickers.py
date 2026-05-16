import logging

import pytest

from selenium import webdriver
from selenium.common.exceptions import (
    TimeoutException,
    WebDriverException
)
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager



'CONFIGURATION'

BASE_URL = "https://orteil.dashnet.org/cookieclicker/"

WAIT_TIME = 10

COOKIE_ID = "bigCookie"
COOKIES_COUNT_ID = "cookies"

PRODUCT_PRICE_PREFIX = "productPrice"
PRODUCT_PREFIX = "product"



'LOGGER SETUP'

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger()



'DRIVER SETUP'

def initialize_browser():

    service = Service(
        ChromeDriverManager().install()
    )

    driver = webdriver.Chrome(
        service=service
    )

    driver.maximize_window()

    return driver



'PAGE OBJECT MODEL CLASS'

class CookieClickerPage:

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(
            driver,
            WAIT_TIME
        )

    def open_website(self):

        self.driver.get(BASE_URL)

        logger.info(
            "Cookie Clicker webpage opened successfully."
        )

    def select_language(self):

        language_button = self.wait.until(
            ec.element_to_be_clickable(
                (
                    By.XPATH,
                    "//*[contains(text(), 'English')]"
                )
            )
        )

        language_button.click()

        logger.info(
            "English language selected successfully."
        )

    def get_cookie_button(self):

        return self.wait.until(
            ec.element_to_be_clickable(
                (
                    By.ID,
                    COOKIE_ID
                )
            )
        )

    def get_cookie_count(self):

        cookies_text = self.driver.find_element(
            By.ID,
            COOKIES_COUNT_ID
        ).text

        cookies_count = cookies_text.split(" ")[0]

        return int(
            cookies_count.replace(",", "")
        )

    def buy_available_product(self, cookies_count):

        for index in range(4):

            try:

                product_price_text = self.driver.find_element(
                    By.ID,
                    PRODUCT_PRICE_PREFIX + str(index)
                ).text

                product_price = int(
                    product_price_text.replace(",", "")
                )

                if cookies_count >= product_price:

                    product = self.wait.until(
                        ec.element_to_be_clickable(
                            (
                                By.ID,
                                PRODUCT_PREFIX + str(index)
                            )
                        )
                    )

                    product.click()

                    logger.info(
                        "Product %s purchased successfully.",
                        index
                    )

                    return True

            except ValueError:
                continue

        return False

    def play_game(self):

        cookie_button = self.get_cookie_button()

        while True:

            cookie_button.click()

            cookies_count = self.get_cookie_count()

            self.buy_available_product(
                cookies_count
            )



'PYTEST FIXTURE'

@pytest.fixture
def driver():

    driver_instance = initialize_browser()

    yield driver_instance

    driver_instance.quit()

    logger.info(
        "Browser closed successfully."
    )



'TEST CASE'

def test_cookie_clicker(driver):

    game = CookieClickerPage(driver)

    try:

        game.open_website()

        game.select_language()

        game.play_game()

    except TimeoutException as error:

        logger.error(
            "Timeout occurred: %s",
            error
        )

    except WebDriverException as error:

        logger.error(
            "WebDriver issue occurred: %s",
            error
        )

    except Exception as error:

        logger.error(
            "Unexpected error occurred: %s",
            error
        )



'MAIN EXECUTION'

if __name__ == "__main__":

    driver = initialize_browser()

    game = CookieClickerPage(driver)

    try:

        game.open_website()

        game.select_language()

        game.play_game()

    except Exception as error:

        logger.error(
            "Execution failed: %s",
            error
        )

    finally:

        driver.quit()

        logger.info(
            "Browser closed successfully."
        )
