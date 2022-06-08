
VERSION = (0,1,0, "alpha", 0)

from exception_decorator.main import *
from exception_decorator.utils.version import get_version
#from utils import get_version

__version__ = get_version(VERSION)
