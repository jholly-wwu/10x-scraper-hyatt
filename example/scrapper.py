import time

from selenium.common.exceptions import WebDriverException
from selenium.webdriver.remote.webdriver import By
import selenium.webdriver.support.expected_conditions as EC  # noqa
from selenium.webdriver.support.wait import WebDriverWait

import undetected_chromedriver as uc


def main(args=None):

    TAKE_IT_EASY = True

    if args:
        TAKE_IT_EASY = (
            args.no_sleeps
        )

    if TAKE_IT_EASY:
        sleep = time.sleep
    else:
        sleep = lambda n: print(
            "we could be sleeping %d seconds here, but we don't" % n
        )

    driver = uc.Chrome()
    driver.get("https://www.hyatt.com/en-US/explore-hotels?regionGroup=0-All&categories=0")
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".properties")))

    propertyList = driver.execute_script(
        "var properties = document.getElementsByClassName('property');var propertyList = [];for (var i = 0; i < properties.length; i++) {propertyList[i] = {'name' : properties.item(i).querySelector('a').textContent,'link' : properties.item(i).querySelector('a').href,}}console.log(propertyList);return propertyList;"
    )
    
    # Once data is fetched from the url, then we make api hit here to store in our DB 
    print(type(propertyList));
    sleep(100)
    
    return 

if __name__ == "__main__":
    import argparse

    p = argparse.ArgumentParser()
    p.add_argument("--no-sleeps", "-ns", action="store_false")
    a = p.parse_args()
    main(a)
