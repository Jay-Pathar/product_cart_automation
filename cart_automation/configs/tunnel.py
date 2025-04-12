import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.safari.options import Options as SafariOptions

# Function to get a Chrome WebDriver instance
def get_chrome_driver():
    # LambdaTest credentials from environment variables
    username = os.getenv("LT_USERNAME")
    access_token = os.getenv("LT_ACCESS_KEY")

    # LambdaTest hub URL
    grid_url = "hub.lambdatest.com/wd/hub"
    url = f"https://{username}:{access_token}@{grid_url}"

    # Set ChromeOptions and desired capabilities - set more options to include terminal logs, network logs etc.
    options = Options()
    options.platform_name = "Windows 10"
    options.browser_version = "latest"
    options.set_capability("build", "Amazon Cart Automation Build #1")
    options.set_capability("name", "Phone Add to Cart Test")
    options.set_capability("project", "Cart Automation Suite")
    options.set_capability("browserName", "Chrome")

    # Initialize and return the driver
    return webdriver.Remote(
        command_executor=url,
        options=options
    )

# Function to get a Safari WebDriver instance
def get_safari_driver():
    # LambdaTest credentials from environment variables
    username = os.getenv("LT_USERNAME")
    access_token = os.getenv("LT_ACCESS_KEY")

    # LambdaTest hub URL
    grid_url = "hub.lambdatest.com/wd/hub"
    url = f"https://{username}:{access_token}@{grid_url}"

    options = SafariOptions()
    options.platform_name = "macOS Ventura"
    options.browser_version = "latest"
    options.set_capability("build", "Safari Build")
    options.set_capability("name", "Test on Safari")
    options.set_capability("browserName", "Safari")

    # Initialize and return the driver
    return webdriver.Remote(
        command_executor=url,
        options=options
    )