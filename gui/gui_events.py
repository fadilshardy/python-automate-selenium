def write_event(event: str, driver: object, window: object, message: str) -> None:
    """
    call write_event_value method from pysimplegui to call event route with the given name

    :return: none
    """

    window.write_event_value(event, {
        'driver': driver,
        'message': message
    })
