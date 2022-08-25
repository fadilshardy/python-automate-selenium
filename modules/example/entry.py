from operator import concat
import time

from utils.webdriver import elements
from utils import helper


def entry_data(user: list, driver: object, window: object):
    """
    call webdriver to open "https://mytestingthoughts.com/Sample/home.html", input mock data from excel.

    :return: driver instance
    """

    WEBSITE_URL = 'https://mytestingthoughts.com/Sample/home.html'

    driver.get(WEBSITE_URL)

    user_data = helper.get_user_by_email_from_excel(window, user)

    elements.wait_text_to_be_present(driver, window, path="/html/body/div/form/fieldset/legend/center/h2/b",
                                     text="Registration Form")  # wait until the website is fully loaded

    # start input automation
    first_name_input = elements.find_element(driver, window,
                                             path="//input[@name='first_name']")

    first_name_input.send_keys(user_data["first_name"])

    last__name_input = elements.find_element(driver, window,
                                             path="//input[@name='last_name']")

    last__name_input.send_keys(user_data["last_name"])

    if(user_data["gender"][0] == "Male"):
        radio_male_select = elements.find_element(driver, window,
                                                  path="inlineRadioMale", selector="id")

        radio_male_select.click()

    else:
        radio_female_select = elements.find_element(driver, window,
                                                    path="inlineRadioFemale", selector="id")

        radio_female_select.click()

    hobby_select = elements.select_input_element(
        driver=driver, window=window, text=user_data["hobbies"][0],  path="exampleFormControlSelect2", selector="id")

    username_input = elements.find_element(driver, window,
                                           path="//input[@name='user_name']")

    username_input.send_keys(user_data["username"])

    password_input = elements.find_element(driver, window,
                                           path="//input[@name='user_password']")

    password_input.send_keys(user_data["password"])

    confirm_password_input = elements.find_element(driver, window,
                                                   path="//input[@name='confirm_password']")

    confirm_password_input.send_keys(user_data["password"])

    email_input = elements.find_element(driver, window,
                                        path="//input[@name='email']")

    email_input.send_keys(user_data["email"])

    contact_input = elements.find_element(driver, window,
                                          path="//input[@name='contact_no']")

    contact_input.send_keys(user_data["contact_number"])

    errors = elements.find_elements(
        driver, window, "//div[contains(@class, 'has-error')]//label")

    if errors:
        error_list = []

        for error in errors:
            error_list.append(error.text)

        error_message = f"{', '.join(error_list)} are not valid"

        window.write_event_value(
            "-UPDATE_TABLE-", {"status": {"success": "FAILED", "message": error_message}, "driver": driver, "user": user})
        return

    time.sleep(1)

    submit_btn = elements.find_element(
        driver, window, path="glyphicon-send", selector="class")
    submit_btn.click()

    window.write_event_value(
        "-UPDATE_TABLE-", {"status": {"success": "SUCCEED", "message": None}, "driver": driver, "user": user})
