import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def page():
    driver = webdriver.Chrome('/Users/jorge.rios/Downloads/chromedriver')  # Optional argument, if not specified will search path.
    driver.get("http://127.0.0.1:5000/")
    texto = ""
    with open('unonuevo.txt', 'r') as f:
        texto = f.readline()
    #assert "Python" in driver.title
    elem = driver.find_element_by_name("nombre")
    elem.clear()
    elem.send_keys(texto)
    time.sleep(5)
    elem = driver.find_element_by_name("edad")
    elem.send_keys("20")
    elem = driver.find_element_by_name("submit")
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
    #driver.close()
    time.sleep(5)
    driver.quit()


if __name__ == "__main__":
    page()
