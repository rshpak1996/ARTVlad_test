import pytest
from selenium import webdriver


link = "https://demoqa.com/"


@pytest.fixture
def driver():

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('start-maximized')
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--log-level=DEBUG')
    # chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # chrome_options.add_argument('--headless')

    prefs = {'download.prompt_for_download': False,
             'download.directory_upgrade': True,
             'safebrowsing.enabled': False,
             }
    chrome_options.add_experimental_option("prefs", prefs)

    browser = webdriver.Chrome(options=chrome_options)
    browser.get(link)

    yield browser
    browser.close()
    browser.quit()