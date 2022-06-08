import sys
import os
import configparser
import logging
import importlib

logging.basicConfig()
module_logger = logging.getLogger("excDecorator")

class myConfig:
    """
    Class to keep configuration
    """

    def __init__(self, name=None, config=None, logging=None):
        self.name = name
        self.config = config
        self.logging = logging

class excDecorator:
    """
    The main class
    """

    def __init__(self, configFile="default.cfg", debug=False):
        """init reads a configuration file"""
        self.logger = logging.getLogger("excDecorator.class")
        self.logger.info("initializing excDecorator")
        self.configFile=configFile
        self.config = configparser.ConfigParser()
        self.config.read_file(open(configFile))
        inLevel = "logging.%s"%(self.config["Default"]["loglevel"])
        logLevel = eval(inLevel)
        self.logger.setLevel(logLevel)
        self.logger.debug("%s config read", configFile)
        self.me = sys.argv[0]
        plugin = ".plugin.%s.helper"%(self.config["Default"]["type"])
        self.logger.debug("using this plugin: %s",plugin)
        self.myfx = importlib.import_module(plugin, ".exception_decorator")
        self.myfx.testme()
        self.logger.debug("initialization is ok")
        #print(myfx)

    def __call__(self, fn):
        def wrapper(*args, **kwargs):

            self.logger.debug("call %s",fn.__name__)
            result = None
            try:
                result = fn(*args, **kwargs)
                self.logger.debug("called %s",fn )
            except:
                msg = "error %s"%(self.me)
                self.logger.error(msg, exc_info=True)
                theErr = sys.exc_info()
                self.logger.error("%s %s %s %s",msg, theErr[1], theErr[0], theErr[2])
                self.myfx.send(self.me, fn.__name__, theErr)
            return result
        return wrapper

    