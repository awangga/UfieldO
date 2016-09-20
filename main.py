#!/usr/bin/env python
"""
main.py application
"""

import updater
import config

u=updater.Updater()
kon=u.opendb()

key = raw_input(config.keyfield+" : ")
res = u.getdata(key)
u.printdata(res)

set = raw_input(config.setfield+" : ")
u.updatedata(key,set)

u.commit()

res = u.getdata(key)
u.printdata(res)

u.closedb()



