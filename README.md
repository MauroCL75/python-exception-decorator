# python-exception-decorator
Extensible python3+ exception decorator

# What
Once upon a while, a dev had python script crashing silently on a cronjob. Someone complained about this and he was right, hence the need of log all the exceptions on something like a file, mail or message queue.
I couldn't find anything usable so I started this.

# Usage
You have to define an output type. Currently available are:
* File: output errors to a file
* Mail: send errors to a mail (WIP)
* Queue: send errors to a message queue (WIP)

You have to create a configuration file with these sections:
* Default: tell the output type (file, mail or queue). This is mandatory. Also specify a console log level for the decorator,
* SPECIFIC: configuration specific to the plugin. Not mandatory.
* EXTRA: configuration modification. Currently not in use yet,
Each plugin has a default.cfg file to have an idea of what is needed.
Here is an example for the file plugin:
```
[Default]
type = file
loglevel = DEBUG

[SPECIFIC]
path = ./logs

[EXTRA]
extension = .log
```
You can just use the decorator on the main or a specific function. Here is the dumb example:
```
from exception_decorator.main.decorator import *
import os
cfg="%s/default.cfg"%(os.getcwd()) #Decorator config

@excDecorator(configFile=cfg) #
def main():
    print(1/0)

if __name__ == "__main__":
    main()
```
# Plugins


# Configuration
You should write a main config where you define the way to handle the exceptions. Each plugin has a specific set of requirements. You can read the default.cfg to have an idea on what is needed.



Mauricio Zambrano 2022
