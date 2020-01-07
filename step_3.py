from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time
import math
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    time.sleep(10)
    browser.quit()


@pytest.mark.parametrize('parameter', ["236895", "236896"])
def test_guest_should_see_login_link(browser, parameter):
    link = f"https://stepik.org/lesson/{parameter}/step/1/"
    browser.get(link)
    answer = str(math.log(int(time.time())))
    print(answer)
    # time.sleep(10)
    text_area = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".textarea"))
    )
    text_area.send_keys(answer)
