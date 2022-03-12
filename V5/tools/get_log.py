import logging
def get_logging():
    fmt="%(asctime)s %(levelname)s [%(name)s] [%(filename)s  (%(funcName)s:%(lineno)d)] - %(message)s"
    logging.basicConfig(level=logging.INFO,filename='../log/log01.log',format=fmt)
    return logging