from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

from scraping import scraping

#Configurando e Atualizando o webdriver
chrome = service=ChromeService(ChromeDriverManager().install())
options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument('--start-maximized')
options_chrome.add_argument('--log-level=3')
driver = webdriver.Chrome(service=chrome, options=options_chrome)

executar = scraping(driver)
executar.informacaos()