import os
import traceback
import logging
import datetime

module_logger = logging.getLogger(__name__)
module_logger.setLevel(logging.DEBUG)


def startup(path):
    '''Initialization setup, make directory if it doesn't exists'''
    module_logger.debug("file initialization")
    if not os.path.isdir(path):
        module_logger.debug("Creating directory ", path)
        os.mkdir(path)

def send(source, function, message, path="./",extension="log",separator="|"):
    '''I send the data'''
    module_logger.debug("send to file")
    now = datetime.datetime.now()
    name = "%s%s.%s"%(path, source, extension)
    module_logger.debug("Writing log to %s",name)
    allErrors = "%s/%s/%s"%(message[0], message[1], traceback.extract_tb(message[2]))
    with open(name, "a") as fp:
        msg = "%s%s%s%s%s%s%s"%(now, separator, source, separator, function, 
            separator, allErrors)
        fp.write (msg)

def testme():
    print("im the file test")