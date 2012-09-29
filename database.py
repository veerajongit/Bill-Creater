# -*- coding: utf-8 -*-
#
#  database.py
#  
#  Copyright 2012 Veeraj <veeraj@draigoon>

import sqlite3

class database:
	
	def crsr(self):
		conn = sqlite3.connect("/home/john/Fine_contacts/fine_company.db", timeout = 10)
		return conn
		
