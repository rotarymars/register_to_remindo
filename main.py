from selenium import webdriver
from selenium.webdriver.chrome import service as fs
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
import time

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
        time.sleep(1)
        try:
            Alert(driver).dismiss()
        except Exception:
            pass
        driver.get(f"https://remindo.co/create/text?message={front}&memo={back}")
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
    pending_input = ""
    while True:
        user_input = ""
        try:
            user_input = input()
        except EOFError:
            pending_input += user_input
            break
        if not user_input.strip():
            if len(front_elements) == len(back_elements):
                front_elements.append(pending_input)
                pending_input = ""
            else:
                back_elements.append(pending_input)
                pending_input = ""
        else:
            pending_input += user_input
    if pending_input:
        if len(front_elements) == len(back_elements):
            front_elements.append(pending_input)
        else:
            back_elements.append(pending_input)
    for a,b in zip(front_elements, back_elements):
        print(a)
        print(b)
        print()
    initialize_browser()
    registrate(front_elements, back_elements)
    destruct_browser()

if __name__ == "__main__":
    main()