from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from time import sleep

from selenium.webdriver.support.ui import Select

def get_one(num):
    opciones=Options()
    opciones.add_experimental_option('excludeSwitches', ['enable-automation'])
    opciones.add_experimental_option('useAutomationExtension', False)
    opciones.headless=False    # si True, no aperece la ventana (headless=no visible)
    opciones.add_argument('--start-maximized')         # comienza maximizado
    opciones.add_argument('user-data-dir=selenium')    # mantiene las cookies
    opciones.add_argument('--incognito')

    
    receipes = []
    nutricionals = []
    ingredients = []
    for i in range(1,13):
        driver = webdriver.Chrome(ChromeDriverManager().install(), options = opciones)

        driver.get(f"https://www.diabetes.org.uk/guide-to-diabetes/recipes?_wrapper_format=html&page={num}")
        sleep(5)
        driver.find_element_by_css_selector("body > div.optanon-alert-box-wrapper > div.optanon-alert-box-bg > div.optanon-alert-box-button-container > div.optanon-alert-box-button.optanon-button-allow > div").click() # aceptar cookies
        sleep(5)
        driver.execute_script("window.scrollTo(0, 300)")
        sleep(5)
        driver.find_element_by_css_selector("#fe-popup-close").click() #acepto el popup
            
        driver.find_element_by_css_selector(f"#block-diabetes-content > div > div > div.recipes-listing > div > div.views-view-grid.horizontal.cols-12.clearfix > div > div:nth-child({i}) > article > div.card__title > h3 > a > span").click() # acceder a la primera receta
        sleep(2)
        receipe = driver.find_element_by_css_selector("#block-diabetes-content > div > div > div:nth-child(1) > h1").text
        receipes.append(receipe)
        nutricional = driver.find_element_by_css_selector("#block-diabetes-content > article > div > div:nth-child(1) > div:nth-child(2) > section").text
        nutricionals.append(nutricional)
        ingredient = driver.find_element_by_css_selector("#edit-group-ingredients > div > div.wrapper").text
        ingredients.append(ingredient)
        driver.quit()
    return receipes, nutricionals, ingredients