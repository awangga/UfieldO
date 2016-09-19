#!/usr/bin/env python
"""
updater.py library
"""

import cx_Oracle
import config
import os

class Updater(object):
	def __init__(self,ORACLE_HOME=config.ORACLE_HOME,LD_LIBRARY_PATH=config.LD_LIBRARY_PATH):
		os.putenv('ORACLE_HOME',ORACLE_HOME)
		os.putenv('LD_LIBRARY_PATH',LD_LIBRARY_PATH)

	def opendb(self):
		cred = config.username+'/'+config.password+'@'+config.host+':'+config.port+'/'+config.sid
		conn = cx_Oracle.connect(cred)
		return conn

	def query(self,connection,SQL):
		cursor = connection.cursor()
		cursor.execute(SQL)
		a = ''
		for row in cursor:
			a = a+row
		cursor.close()
		return a

	def closedb(self,connection):
		connection.close()

	

