#!/usr/bin/env python
"""
main.py application
"""

import updater
u=updater.Updater()
kon=u.opendb()
sqlget = "select * from T_APPS where PATH = 'simpon.eo'"
sqlu = "update T_APPS set LATEST_VERSION = '1.1' where PATH = 'simpon.eo'"
res = u.query(sqlget)
print res
res = u.query(sqlu)
print res
res = u.query(sqlget)
print res
u.closedb()



