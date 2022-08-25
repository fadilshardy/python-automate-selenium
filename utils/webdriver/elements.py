from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException, TimeoutException, ElementNotInteractableException, NoSuchAttributeException, NoSuchElementException


from gui import gui_events


def get_selector(selector: str) -> By:
    """
    check if given selector matches with identifier from selenium

    :return: if matches return selenium identifier
    """

    match selector:
        case 'xpath':
            return By.XPATH
        case 'class':
            return By.CLASS_NAME
        case 'id':
            return By.ID
        case _:
            print('Selector is not valid')


def wait_element(driver: object, window: object, path: str, selector: str = 'xpath', timer: int = 3600) -> None:
    """
    wait for an element with given identifier to be visible

    :return: none
    """
    identifier = get_selector(selector)

    try:
        element = EC.presence_of_element_located((identifier, path))
        WebDriverWait(driver, timer).until(element)

    except TimeoutException:
        gui_events.write_event('-ERROR-', driver, window,
                               message='aplikasi timed out, buka kembali aplikasi')

    except WebDriverException:
        gui_events.write_event('-ERROR-', driver, window,
                               message='Browser tidak ditemukan')


def find_element(driver: object, window: object, path: str, selector: str = 'xpath') -> dict:
    """
    find an element with given identifier

    :return: webdriver element
    """
    identifier = get_selector(selector)

    try:
        wait_element(driver, window, path, selector, timer=3600)

        element = driver.find_element(identifier, path)

        return element

    except ElementNotInteractableException:
        gui_events.write_event('-ERROR-', driver, window,
                               message='element tidak bisa di klik')

    except NoSuchAttributeException:
        gui_events.write_event('-ERROR-', driver, window,
                               message='element tidak ditemukan')
    except WebDriverException:
        gui_events.write_event('-ERROR-', driver, window,
                               message='Browser tidak ditemukan')


def check_element_exists(driver: object, path: str, selector: str = 'xpath') -> bool:
    """
    check if element with given identifier exist

    :return: bool
    """

    identifier = get_selector(selector)

    try:
        driver.find_element(identifier, path)
    except NoSuchElementException:
        return False
    return True


def check_element_clickable(driver: object, window: object, path: str, selector: str = 'xpath') -> bool:
    """
    check if element with given identifier is clickable

    :return: return boolean True if clickable
    """

    identifier = get_selector(selector)

    try:
        element_clickable = EC.element_to_be_clickable(
            (identifier, path))

        WebDriverWait(driver, 3600).until(element_clickable)

        return True

    except TimeoutException:
        gui_events.write_event('-ERROR-', driver, window,
                               message='aplikasi timed out, buka kembali aplikasi')

    except WebDriverException:
        gui_events.write_event('-ERROR-', driver, window,
                               message='Browser tidak ditemukan')


def wait_text_to_be_present(driver: object,
                            window: object,
                            path: str, text: str,
                            selector: str = 'xpath') -> bool:
    """
    wait until text is present from the given element

    :return: bool
    """

    identifier = get_selector(selector)

    try:
        WebDriverWait(driver, 3600).until(
            EC.text_to_be_present_in_element((identifier, path), text))

        return True
    except WebDriverException:
        gui_events.write_event('-ERROR-', driver, window,
                               message='Browser tidak ditemukan')


def check_if_text_is_present(driver: object,
                             window: object,
                             path: str, text:
                             str, selector:
                             str = 'xpath') -> bool:
    """
    check if text is present from the given element text

    :return: bool
    """

    identifier = get_selector(selector)

    try:
        element_text = driver.find_element(identifier, path).text

        return text in element_text

    except NoSuchElementException:
        return False

    except WebDriverException:
        gui_events.write_event('-ERROR-', driver, window,
                               message='Browser tidak ditemukan')


def select_input_element(text: str,
                         driver: object,
                         window: object,
                         path: str,
                         selector: str = 'xpath') -> None:
    """
    Select the input dropdown by text

    :return: none
    """

    Select(find_element(driver, window,
                        path=path, selector=selector)).select_by_visible_text(text)


def find_elements(driver: object, window: object, path: str, selector: str = 'xpath') -> dict:
    """
    find an elements with given identifier

    :return: webdriver element
    """
    identifier = get_selector(selector)

    try:
        elements = driver.find_elements(identifier, path)

        return elements

    except ElementNotInteractableException:
        gui_events.write_event('-ERROR-', driver, window,
                               message='element tidak bisa di klik')

    except NoSuchAttributeException:
        gui_events.write_event('-ERROR-', driver, window,
                               message='element tidak ditemukan')
    except WebDriverException:
        gui_events.write_event('-ERROR-', driver, window,
                               message='Browser tidak ditemukan')
