import logging

logging.basicConfig(
    level=logging.INFO,
    filename="C://Users//TUL//Desktop//selenium_things//selenium_framework//logs&Repos//Uninist-Logs//city-Forms.log",
    filemode="w",
    format="%(asctime)s %(levelname)s %(message)s",
)

logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")


logging.warning("This will get logged to a file")
