import logging
import logging.handlers
import time
fmt="%(asctime)s %(levelname)s [%(name)s] [%(filename)s  (%(funcName)s:%(lineno)d)] - %(message)s"
logger = logging.getLogger()
logger.setLevel(logging.INFO)
#处理器
thandler = logging.handlers.TimedRotatingFileHandler(filename="./log01.log",
                                                    when="S",
                                                    interval=1,
                                                    backupCount=3)
shandler = logging.StreamHandler()
#格式器
fm = logging.Formatter(fmt)
#处理器添加格式器
shandler.setFormatter(fm)
thandler.setFormatter(fm)
#logger添加处理器
logger.addHandler(thandler)
logger.addHandler(shandler)
while True:
    time.sleep(1)
    logger.info("info")
    logger.debug("debug")