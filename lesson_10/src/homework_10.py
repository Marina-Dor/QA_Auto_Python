"""
You and your team are developing a login system for a web application,
and you need to implement function tests to log events in the login system.
Given a function, write a set of tests for it.
"""

import logging
import logging.config
logging.config.fileConfig('lesson_10/log_config.ini')


def log_event(username: str, status: str):
    """
    Logs the login event.

    username: Username that is logged in to the system.

    status: Login event status:

    * success - successful, logged at info level
    * expired - the password is out of date and should be replaced, logged at the warning level
    * failed - the password is incorrect, it is logged at the error level
    """
    log_message = f"Login event - Username: {username}, Status: {status}"

    logger = logging.getLogger("log_event")

    # Logging event
    if status == "success":
        logger.info(log_message)
    elif status == "expired":
        logger.warning(log_message)
    else:
        logger.error(log_message)
