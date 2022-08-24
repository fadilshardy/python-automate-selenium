
from utils.webdriver import elements


def entry_data(user: list, driver: object, window: object, data: object):
    """
    call webdriver to open "https://mytestingthoughts.com/Sample/home.html", input mock data from excel.

    :return: driver instance
    """

    WEBSITE_URL = 'https://mytestingthoughts.com/Sample/home.html'

    driver.get(WEBSITE_URL)

    elements.wait_text_to_be_present(driver, window, path="/html/body/div/form/fieldset/legend/center/h2/b",
                                     text="Registration Form")  # wait until the website is fully loaded

    # start input automation
    first_name_input = elements.find_element(driver, window,
                                             path="//input[@name='first_name']")

    first_name_input.send_key(data["first_name"])

    last__name_input = elements.find_element(driver, window,
                                             path="//input[@name='last__name']")

    last__name_input.send_key(data["last_name"])

    if(data["gender"] == "Male"):
        radio_male_select = elements.find_element(driver, window,
                                                  path="inlineRadioMale", selector="id")

        radio_male_select.click()

    else:
        radio_female_select = elements.find_element(driver, window,
                                                    path="inlineRadioFemale", selector="id")

        radio_female_select.click()

    hobby_select = elements.select_input_element(
        driver, window, text=data["hobbies"],  path="exampleFormControlSelect2", selector="id")

    username_input = elements.find_element(driver, window,
                                           path="//input[@name='user_name']")

    username_input.send_key(data["last_name"])

    password_input = elements.find_element(driver, window,
                                           path="//input[@name='user_password']")

    password_input.send_key(data["password"])

    confirm_password_input = elements.find_element(driver, window,
                                                   path="//input[@name='confirm_password']")

    confirm_password_input.send_key(data["password"])

    email_input = elements.find_element(driver, window,
                                        path="//input[@name='email']")

    email_input.send_key(data["email"])

    contact_input = elements.find_element(driver, window,
                                          path="//input[@name='contact_no']")

    contact_input.send_key(data["contact_number"])

    submit_btn = elements.find_element(
        driver, window, path="glyphicon-send", selector="class")
    submit_btn.click()

    window.write_event_value(
        "-UPDATE_TABLE-", {"user": user, "status": {"success": "BERHASIL", "message": None}, "driver": driver})
