import inspect
import logging
def getLogger(self):
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    fileHandler = logging.FileHandler("logFile.log")
    fileFormatter = logging.Formatter('%(asctime)s: -%(name)s - %(levelname)s: %(message)s')
    fileHandler.setFormatter(fileFormatter)
    logger.addHandler(fileHandler)
    logger.setLevel(logging.DEBUG)
    return logger
