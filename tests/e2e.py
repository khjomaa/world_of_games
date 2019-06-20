from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep


def test_scores_service(app_url):
    driver = webdriver.Remote(
        command_executor='http://selenium-hub:4444/wd/hub',
        desired_capabilities=DesiredCapabilities.CHROME
    )

    try:
        driver.get(app_url)
        elem = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "score")))
        score = int(elem.text)
        sleep(2)
        driver.quit()
        return True if 1 <= score <= 1000 else False
    except Exception as ex:
        print(ex.args[0])
        driver.quit()
        return False


def main_function():
    result = test_scores_service('http://web:5000')
    if result:
        return 0
    return -1


if __name__ == '__main__':
    res = main_function()
    print(res)
