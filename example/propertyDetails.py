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
    driver.get("https://www.hyatt.com/shop/lishr?checkinDate=2023-01-06&checkoutDate=2023-01-07&rooms=1&adults=1&kids=0&rate=Standard&rateFilter=standard")
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".m-rate-plan-header")))
    
    sleep(5)
    
    creditPoints = driver.execute_script('var items = document.getElementsByTagName("span");for (var i = 0; i < items.length; ++i) {if (items[i].textContent.includes("Standard Rate")) {console.log("success"); return items[i].closest("div").getElementsByClassName("rate-pricing")[0].getElementsByTagName("span")[0].innerHTML;break;}}');
    print("Reward Points "+creditPoints);
    sleep(100)
    
    return 

if __name__ == "__main__":
    import argparse

    p = argparse.ArgumentParser()
    p.add_argument("--no-sleeps", "-ns", action="store_false")
    a = p.parse_args()
    main(a)
