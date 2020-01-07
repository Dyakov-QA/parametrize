import pytest
import time
import math
from selenium import webdriver
final = ""


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    browser.quit()
    print("\n" + final)


@pytest.mark.parametrize('parameter', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, parameter):
    global final
    link = f"https://stepik.org/lesson/{parameter}/step/1/"
    browser.implicitly_wait(10)
    browser.get(link)
    answer = str(math.log(int(time.time())))
    browser.find_element_by_css_selector('textarea').send_keys(str(answer))
    browser.find_element_by_css_selector('.submit-submission ').click()
    feedback = browser.find_element_by_css_selector('.smart-hints__hint').text
    try:
        assert 'Correct!' == feedback
    except AssertionError:
        final += feedback  # собираем ответ про Сов с каждой ошибкой
