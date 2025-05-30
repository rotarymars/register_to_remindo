from selenium import webdriver
from selenium.webdriver.chrome import service as fs
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
import time
from urllib.parse import quote

driver_path = "/home/rotarymars/bin/chromedriver"

def initialize_browser():
    global driver, driver_path
    chrome_driver = fs.Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=chrome_driver)
    driver.get("https://remindo.co/start")
    with open("username.txt", "r") as f:
        username = f.read().strip()
    with open("password.txt", "r") as f:
        password = f.read().strip()
    element = driver.find_element(By.NAME, "id")
    element.send_keys(username)
    element = driver.find_element(By.NAME, "pw")
    element.send_keys(password)
    element = driver.find_element(By.ID, "btn-login")
    element.click()
    try:
        Alert(driver).dismiss()
    except Exception:
        pass
def destruct_browser():
    try:
        Alert(driver).dismiss()
    except Exception:
        pass
    driver.close()

def registrate(a: [str], b: [str]):
    global driver
    try:
        Alert(driver).dismiss()
    except Exception:
        pass
    for front, back in zip(a, b):
        print(front, back)
        time.sleep(1)
        try:
            Alert(driver).dismiss()
        except Exception:
            pass
        encoded_front = quote(front)
        encoded_back = quote(back)
        driver.get(f"https://remindo.co/create/text?message={encoded_front}&memo={encoded_back}")
        print(f"https://remindo.co/create/text?message={encoded_front}&memo={encoded_back}")
        time.sleep(1)
        try:
            Alert(driver).dismiss()
        except Exception:
            pass
        time.sleep(1)
        element = driver.find_element(By.CSS_SELECTOR, ".btn.btn-default.btn-success")
        element.click()
        time.sleep(1)
        try:
            Alert(driver).dismiss()
        except Exception:
            pass
        time.sleep(1)
def main():
    front_elements = []
    back_elements = []
    current_front = []
    current_back = []
    is_front = True
    
    while True:
        try:
            line = input()
            if not line.strip():
                if is_front and current_front:
                    front_elements.append("\n".join(current_front))
                    current_front = []
                    is_front = False
                elif not is_front and current_back:
                    back_elements.append("\n".join(current_back))
                    current_back = []
                    is_front = True
            else:
                if is_front:
                    current_front.append(line)
                else:
                    current_back.append(line)
        except EOFError:
            if current_front:
                front_elements.append("\n".join(current_front))
            if current_back:
                back_elements.append("\n".join(current_back))
            break
    for a,b in zip(front_elements, back_elements):
        print(a)
        print(b)
        print()
    initialize_browser()
    registrate(front_elements, back_elements)
    destruct_browser()

if __name__ == "__main__":
    main()