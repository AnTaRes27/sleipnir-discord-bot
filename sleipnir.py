#!/usr/bin/env python3.7
"""/// SLEIPNIR v0.0.1 ////////////////////////////////////////////////////////
""/                                                                           /
"/                                                                            /
/
/
/                                                                            /"
/                                                                           /""
////////////////////////////////////////////////////////////////////////////"""

import os

os.system('cls' if os.name == 'nt' else 'clear')    #clear screen
print('// Starting bot. Please wait. . .')

config = Config(config_filename='config.toml', \
                ori_config_filename='default_config.toml')  #load config