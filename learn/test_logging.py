#
# import logging
# # #设置日志级别
# # logging.basicConfig(level=logging.DEBUG)
# #设置日志输出格式
# fmt="%(asctime)s %(levelname)s [%(name)s] [%(filename)s  (%(funcName)s:%(lineno)d)] - %(message)s"
# # logging.basicConfig(level=logging.DEBUG,format=fmt)
# #将日志信息输出到文件中
# logging.basicConfig(level=logging.DEBUG,format=fmt,filename='./log01.log')
# logging.debug("调试信息")
# logging.info("普通信息")
# logging.warning("警告信息")
# logging.error("错误信息")
# logging.critical("严重错误")
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()

logger.addHandler(handler)

logger.info("info")
logger.debug("debug")