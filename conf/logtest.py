import logging.config

logging.config.fileConfig("logging.conf")

# #create logger
# loggerInfo = logging.getLogger("errorLogger")
#
# #"application" code
# loggerInfo.debug("debug message")
# loggerInfo.info("info message")
# loggerInfo.warn("warn message")
# loggerInfo.error("error message")
# loggerInfo.critical("critical message")


loggerError = logging.getLogger("logger_root")
loggerError.debug("debug")

loggerError.info("info")
loggerError.warn("warn")
loggerError.error("error")
loggerError.critical("critical")