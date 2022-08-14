#logging.config.fileConfig('logging.conf')

# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                     datefmt='%m/%d/%Y %H:%M:%S')

# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('this is a warning message')
# logging.error('this is an error message')
# logging.critical('this is a critical message')


# logger = logging.getLogger('simpleExample')
# logger.debug('This is a debug message')


import logging

try:
    a =  [1,3,4]
    val = a[5]
except IndexError as e:
    logging.error(e)
    
try:
    a = [2,3,4]
    val = a[22]
except IndexError as e:
    logging.error(e, exc_info=True)


import traceback

try:
    a = [1,3,4]
    val = a[22]
except:
    logging.error('the error is %s', traceback.format_exc())


