#!/usr/bin/env python
"""
main.py application
"""

import updater
u=updater.Updater()
kon=u.opendb()
apppath = raw_input("PATH : ")
sqlget = "select * from T_APPS where PATH = '"+apppath+"'"
res = u.query(sqlget)
u.printdata(res)
version = raw_input("LATEST_VERSION : ")
sqlu = "update T_APPS set LATEST_VERSION = '"+version+"' where PATH = '"+apppath+"'"
u.query(sqlu)
res = u.query(sqlget)
u.printdata(res)
u.commit()
u.closedb()



