from selenium.webdriver.common.by import By
import time

class scraping:
    def __init__(self, driver):
        self.driver = driver
        
        self.folders = By.XPATH, "*//div[@class='Box-row Box-row--focus-gray py-2 d-flex position-relative js-navigation-item ']"
        self.acessar = By.XPATH, "*//a[@class='js-navigation-open Link--primary']"

    def verificar_folder(self):
        '''self.veri = self.driver.find_elements(*self.folders)[x].get_attribute('innerHTML')
        while 'Directory' in self.veri: 
            self.driver.find_elements(*self.acessar)[x].click()
            time.sleep(3)
            quantFolders = len(self.driver.find_elements(*self.folders))
            print(f"quantidade de subfolders no repositorio: {quantFolders}")
            self.veri = self.driver.find_elements(*self.folders)[x].get_attribute('innerHTML')'''

    def informacaos(self):
        global x
        link = '/twbs/bootstrap'
        self.driver.get(f'https://github.com{link}')
        quantArquivos = len(self.driver.find_elements(*self.folders))

        print(f"quantidade de folders no repositorio: {quantArquivos}")
        for i in range(quantArquivos):
            print(quantArquivos)
            print(i)
            self.verificar = self.driver.find_elements(*self.folders)[i].get_attribute('innerHTML')
            while 'Directory' in self.verificar:
                self.driver.find_elements(*self.acessar)[i].click()
                time.sleep(3)
                quantFolders = len(self.driver.find_elements(*self.folders))
                print(f"quantidade de subfolders no repositorio: {quantFolders}")
                self.veri = self.driver.find_elements(*self.folders)[i].get_attribute('innerHTML')
            else:
                self.driver.find_elements(*self.acessar)[i].click()
            input('continuar')

        input("parar")
