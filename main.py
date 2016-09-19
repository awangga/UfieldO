#!/usr/bin/env python
"""
main.py application
"""

import updater
u=updater.Updater()
kon=u.opendb()
sql = "select * from T_APPS"
u.query(sql)
u.closedb()



