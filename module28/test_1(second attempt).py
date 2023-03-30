import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
service = Service(executable_path="/chromedriver/chromedriver.exe")


def test_correct_number():
    with webdriver.Chrome(service=service) as driver:
        driver.get("https://b2c.passport.rt.ru")

        time.sleep(5)

        # add number
        field_username = driver.find_element(By.ID, "username")
        field_username.clear()
        field_username.send_keys("+79853612807")

        # add password
        field_pass = driver.find_element(By.ID, "password")
        field_pass.clear()
        field_pass.send_keys("Skillfactory29")

        # click submit button
        btn_submit = driver.find_element(By.ID, "kc-login")
        btn_submit.click()

        time.sleep(5)

        url_after = driver.current_url
        if "https://b2c.passport.rt.ru/auth/" in url_after:
            raise Exception("number error")


def test_correct_email():
    with webdriver.Chrome(service=service) as driver:
        driver.get("https://b2c.passport.rt.ru")

        time.sleep(5)

        # click button email
        btn_email = driver.find_element(By.ID, "t-btn-tab-mail")
        btn_email.click()

        # add email
        field_username = driver.find_element(By.ID, "username")
        field_username.clear()
        field_username.send_keys("dimapisarev2019@mail.ru")

        # add password
        field_pass = driver.find_element(By.ID, "password")
        field_pass.clear()
        field_pass.send_keys("Skillfactory29")

        # click submit button
        btn_submit = driver.find_element(By.ID, "kc-login")
        btn_submit.click()

        time.sleep(5)

        url_after = driver.current_url
        if "https://b2c.passport.rt.ru/auth/" in url_after:
            raise Exception("email error")


def test_correct_login():
    with webdriver.Chrome(service=service) as driver:
        driver.get("https://b2c.passport.rt.ru")

        time.sleep(5)

        # click button login
        btn_email = driver.find_element(By.ID, "t-btn-tab-login")
        btn_email.click()

        # add login
        field_username = driver.find_element(By.ID, "username")
        field_username.clear()
        field_username.send_keys("dimapisarev2019@mail.ru")

        # add password
        field_pass = driver.find_element(By.ID, "password")
        field_pass.clear()
        field_pass.send_keys("Skillfactory29")

        # click submit button
        btn_submit = driver.find_element(By.ID, "kc-login")
        btn_submit.click()

        time.sleep(5)

        url_after = driver.current_url
        if "https://b2c.passport.rt.ru/auth/" in url_after:
            raise Exception("login error")


def test_correct_ls():
    with webdriver.Chrome(service=service) as driver:
        driver.get("https://b2c.passport.rt.ru")

        time.sleep(5)

        # click button ls
        btn_email = driver.find_element(By.ID, "t-btn-tab-ls")
        btn_email.click()

        # add ls
        field_username = driver.find_element(By.ID, "username")
        field_username.clear()
        field_username.send_keys("dimapisarev2019@mail.ru")

        # add password
        field_pass = driver.find_element(By.ID, "password")
        field_pass.clear()
        field_pass.send_keys("Skillfactory29")

        # click submit button
        btn_submit = driver.find_element(By.ID, "kc-login")
        btn_submit.click()

        time.sleep(5)

        url_after = driver.current_url
        if "https://b2c.passport.rt.ru/auth/" in url_after:
            raise Exception("ls error")


def test_wrong_number():
    with webdriver.Chrome(service=service) as driver:
        driver.get("https://b2c.passport.rt.ru")

        time.sleep(5)

        # add number
        field_username = driver.find_element(By.ID, "username")
        field_username.clear()
        field_username.send_keys("+79876543210")

        # add password
        field_pass = driver.find_element(By.ID, "password")
        field_pass.clear()
        field_pass.send_keys("Skillfactory29")

        # click submit button
        btn_submit = driver.find_element(By.ID, "kc-login")
        btn_submit.click()

        time.sleep(5)

        url_after = driver.current_url
        if "https://b2c.passport.rt.ru/auth/" in url_after:
            raise Exception("number error")


def test_wrong_email():
    with webdriver.Chrome(service=service) as driver:
        driver.get("https://b2c.passport.rt.ru")

        time.sleep(5)

        # click button email
        btn_email = driver.find_element(By.ID, "t-btn-tab-mail")
        btn_email.click()

        # add email
        field_username = driver.find_element(By.ID, "username")
        field_username.clear()
        field_username.send_keys("dimapisarev2019@mail.com")

        # add password
        field_pass = driver.find_element(By.ID, "password")
        field_pass.clear()
        field_pass.send_keys("Skillfactory29")

        # click submit button
        btn_submit = driver.find_element(By.ID, "kc-login")
        btn_submit.click()

        time.sleep(5)

        url_after = driver.current_url
        if "https://b2c.passport.rt.ru/auth/" in url_after:
            raise Exception("email error")


def test_wrong_login():
    with webdriver.Chrome(service=service) as driver:
        driver.get("https://b2c.passport.rt.ru")

        time.sleep(5)

        # click button login
        btn_login = driver.find_element(By.ID, "t-btn-tab-login")
        btn_login.click()

        # add login
        field_username = driver.find_element(By.ID, "username")
        field_username.clear()
        field_username.send_keys("wronglogin")

        # add password
        field_pass = driver.find_element(By.ID, "password")
        field_pass.clear()
        field_pass.send_keys("Skillfactory29")

        # click submit button
        btn_submit = driver.find_element(By.ID, "kc-login")
        btn_submit.click()

        time.sleep(5)

        url_after = driver.current_url
        if "https://b2c.passport.rt.ru/auth/" in url_after:
            raise Exception("login error")


def test_wrong_ls():
    with webdriver.Chrome(service=service) as driver:
        driver.get("https://b2c.passport.rt.ru")

        time.sleep(5)

        # click button login
        btn_ls = driver.find_element(By.ID, "t-btn-tab-ls")
        btn_ls.click()

        # add login
        field_username = driver.find_element(By.ID, "username")
        field_username.clear()
        field_username.send_keys("123456789012")

        # add password
        field_pass = driver.find_element(By.ID, "password")
        field_pass.clear()
        field_pass.send_keys("Skillfactory29")

        # click submit button
        btn_submit = driver.find_element(By.ID, "kc-login")
        btn_submit.click()

        time.sleep(5)

        url_after = driver.current_url
        if "https://b2c.passport.rt.ru/auth/" in url_after:
            raise Exception("ls error")


def test_restore_password_number():
    with webdriver.Chrome(service=service) as driver:
        driver.get("https://b2c.passport.rt.ru")

        time.sleep(5)

        # click button forgot password
        btn_forgot = driver.find_element(By.ID, "forgot_password")
        btn_forgot.click()

        time.sleep(5)

        # add number
        field_username = driver.find_element(By.ID, "username")
        field_username.clear()
        field_username.send_keys("+79853612807")

        time.sleep(5)

        # click button forgot password
        btn_number = driver.find_element(By.CSS_SELECTOR, "#page-right > div > div > div > form > div > label:nth-child(1) > span")
        btn_number.click()

        # click submit button
        btn_submit = driver.find_element(By.ID, "kc-login")
        btn_submit.click()

        time.sleep(5)

        url_after = driver.current_url
        if "https://b2c.passport.rt.ru/auth/" in url_after:
            raise Exception("number error")


def test_restore_password_email():
    with webdriver.Chrome(service=service) as driver:
        driver.get("https://b2c.passport.rt.ru")

        time.sleep(5)

        # click button forgot password
        btn_forgot = driver.find_element(By.ID, "forgot_password")
        btn_forgot.click()

        time.sleep(5)

        # click button email
        btn_email = driver.find_element(By.ID, "t-btn-tab-mail")
        btn_email.click()

        # add email
        field_username = driver.find_element(By.ID, "username")
        field_username.clear()
        field_username.send_keys("dimapisarev2019@mail.ru")

        time.sleep(5)

        # click button forgot password
        btn_email = driver.find_element(By.CSS_SELECTOR, "#page-right > div > div > div > form > div > label:nth-child(2)")
        btn_email.click()

        # click submit button
        btn_submit = driver.find_element(By.ID, "kc-login")
        btn_submit.click()

        time.sleep(5)

        url_after = driver.current_url
        if "https://b2c.passport.rt.ru/auth/" in url_after:
            raise Exception("email error")

