#! /usr/bin/python3.12

import configparser as cp 


conf = cp.ConfigParser()
conf['DEFAULT'] = {'lending_period' : 0, 'max_value' : 0}
conf['Fred'] = {'max_value' : 200} # Fred's a bit rough with things!
conf['Anne'] = {'lending_period' : 30} # She is a bit forgetful sometimes
with open('toolhire.ini', 'w') as toolhire:
    conf.write(toolhire)