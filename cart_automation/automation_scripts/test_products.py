# Import necessary libraries for web scraping, captcha solving, and logging
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from amazoncaptcha import AmazonCaptcha
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import warnings

from cart_automation.configs.tunnel import get_chrome_driver
from cart_automation.configs.logs_config import get_logger

warnings.filterwarnings("ignore", category=UserWarning)
logger = get_logger(__name__)

# Handles Amazon captcha if encountered during navigation
def handle_captcha(driver, wait):
    try:
        captcha_img = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class = 'a-row a-text-center']//img")))
        captcha_link = captcha_img.get_attribute("src")
        captcha = AmazonCaptcha.fromlink(captcha_link)
        captcha_value = AmazonCaptcha.solve(captcha)
        driver.find_element(By.ID, "captchacharacters").send_keys(captcha_value)
        driver.find_element(By.CLASS_NAME, "a-button-text").click()
        wait.until(EC.presence_of_element_located((By.ID, "nav-global-location-popover-link")))
        logger.info("Captcha solved.")
    except (NoSuchElementException, TimeoutException):
        logger.info("No captcha found. Proceeding...")

# Sets the ZIP code via location popover to ensure regional product availability and pricing.
def set_location(driver, wait, zip_code="31217"):
    try:
        location_button = wait.until(EC.element_to_be_clickable((By.ID, "nav-global-location-popover-link")))
        location_button.click()
        postal_input = wait.until(EC.presence_of_element_located((By.ID, "GLUXZipUpdateInput")))
        postal_input.send_keys(zip_code)
        postal_input.send_keys(Keys.ENTER)
        try:
            done_button = wait.until(EC.element_to_be_clickable((
                By.XPATH, "//div[contains(@class, 'a-popover-footer')]//input[contains(@class, 'a-button-input')]")))
            done_button.click()
            logger.info("Clicked Done.")
        except TimeoutException:
            logger.info("Done button not found.")
    except (NoSuchElementException, TimeoutException):
        logger.info("Could not set location.")

# Searches for the product name in Amazon's search bar with retries for stale or unresponsive elements.
def search_product(driver, wait, product_name):
    try:
        wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
        search_box = driver.find_element(By.ID, "twotabsearchtextbox")
        search_box.clear()
        search_box.send_keys(product_name)
        search_box.send_keys(Keys.RETURN)
        logger.info(f"Searched for {product_name}.")
    except (StaleElementReferenceException, TimeoutException):
        logger.warning("Search box failed. Retrying...")
        search_box = driver.find_element(By.ID, "twotabsearchtextbox")
        search_box.clear()
        search_box.send_keys(product_name)
        search_box.send_keys(Keys.RETURN)

# Clicks the product link matching the specified product_id to open the correct product page.
def select_product(driver, wait, product_id):
    try:
        product_link = wait.until(EC.element_to_be_clickable((By.XPATH, f"//a[contains(@href,'{product_id}')]")))
        product_link.click()
        logger.info(f"Clicked product with ID {product_id}.")
    except TimeoutException:
        logger.warning(f"Product {product_id} not found.")
        driver.quit()

# Clicks the "Add to Cart" button and logs the action or handles timeout if the button is unresponsive.
def add_to_cart(driver, wait):
    try:
        add_button = wait.until(EC.element_to_be_clickable((By.ID, "submit.add-to-cart")))
        add_button.click()
        logger.info("Clicked Add to Cart.")
    except TimeoutException:
        logger.warning("Add to Cart button not found.")
        driver.quit()

# Clicks on the 'No Thanks' button if Amazon shows a protection plan popup
def skip_protection_plan(wait):
    try:
        no_thanks = wait.until(EC.element_to_be_clickable((By.ID, "attachSiNoCoverage")))
        no_thanks.click()
        logger.info("Clicked 'No Thanks'.")
    except (TimeoutException, NoSuchElementException):
        logger.info("'No Thanks' button not found.")

# Fetches the price from the product page.
def fetch_price(wait, label):
    try:
        price_element = wait.until(EC.presence_of_element_located((By.ID, "sw-subtotal")))
        value = price_element.get_attribute("data-price")
        logger.info(f"{label} PRICE: {value}")
    except TimeoutException:
        logger.warning(f"{label} price not found.")

# Executes the complete automation workflow for a product: opens Amazon, handles captcha, sets location, searches, adds to cart, and logs the price.
def process_product(product_name, product_id, label):
    driver = get_chrome_driver()
    driver.delete_all_cookies()
    wait = WebDriverWait(driver, 30)
    driver.get("https://www.amazon.com/")

    handle_captcha(driver, wait)
    set_location(driver, wait)
    search_product(driver, wait, product_name)
    select_product(driver, wait, product_id)
    add_to_cart(driver, wait)
    skip_protection_plan(wait)
    fetch_price(wait, label)
    driver.quit()

# Calls process_product for specific products like Galaxy or iPhone independently.
def process_samsung():
    process_product("galaxy", "B0DP3G4GVQ", "GALAXY")

def process_iphone():
    process_product("iphone", "B09LNW3CY2", "IPHONE")
