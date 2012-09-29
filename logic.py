#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  logic.py
#  
#  Copyright 2012 Veeraj <veeraj@draigoon>
import datetime
import sys
sys.path.append( "/home/john/Fine_contacts" )
from database import *
import math
#import gui
class logic:
	datenow = datetime.datetime.now().strftime("%d-%m-%Y")
	def item_add(self, re, name, rate):
		name = name
		rate = rate
		db = database()
		c = db.crsr()
		na = c.cursor().execute("SELECT item_name FROM item_list")
		
		for arr in na:
			if name in arr:
				import easygui
				easygui.msgbox("Item Exist")
				return 0
		c.cursor().execute("INSERT INTO item_list(item_no, item_name, item_rate) VALUES (?, ?, ?)", (re, name , rate))
		c.commit()

			
			
	def itad(self, b):
		db = database()
		c = db.crsr()
		i = c.cursor().execute("SELECT * FROM item_list ORDER BY item_no ")
		arra = []
		cc = 0
		for arr in i:
			if cc == 0:arra = arr; cc = cc + 1
			else:arra = arra + arr
			
		y = ""
		zee = ""
		x = ""
		i = c.cursor().execute("SELECT * FROM item_list")
		cc = 0
		for countall in i:
			count = cc * 3
			y = y + str(arra[count]) + "\n\n"
			zee = zee + str(arra[count + 1]) + "\n\n"			
			x = x + str(arra[count + 2]) + "\n\n"
			cc = cc + 1
			
		b.get_object('item_n').set_text(y)
		b.get_object('item_nam').set_text(zee)
		b.get_object('item_rate').set_text(x)
		
	def deletelogic(self, no):
		db = database()
		c = db.crsr()
		c.cursor().execute("DELETE FROM item_list WHERE item_no = ?", (no,))
		c.commit()
		
		
	def i_num(self):
		db = database()
		c = db.crsr()
		i = c.execute("SELECT item_no FROM item_list")
		array = []
		for arr in i: array = arr
		try:
			no = array[-1] + 1
		except:
			no = 1
		return no
		
		
	def dates(self):
		return self.datenow
		
	def invoice_num(self):
		db = database()
		c = db.crsr()
		i = c.execute("SELECT MAX(bill_no) FROM bill")
		array = ()
		for arr in i: array =  arr
		if array[0] is not None :
			no = array[-1] + 1
		else:
			no = 1
		return no
		
		
		
	def add_to_bill(self, b):
		item_no = b.get_object("add_i_no").get_text()
		item_quan = b.get_object("add_quantity").get_text()
		b_no = b.get_object("invoice_no").get_text()
		no = b.get_object("sr_no").get_text()
		weight = b.get_object("item_weight").get_text()
		item_no = int(item_no)
		item_quan = int(item_quan)
		b_no = int(b_no)
		no = int(no)
		weight = float(weight)
		self.insert(no, b_no, item_no ,item_quan, weight)
		
		
	def insert(self, no, b_no, item_no ,item_quan, weight):
		db = database()
		con = db.crsr()
		c = con.cursor()
		c.execute("INSERT INTO description(sr_no, bill_no, item_no, quantity, weight) VALUES(?,?,?,?,?)",(no, b_no, item_no, item_quan, weight))
		con.commit()
			

	def show_bi(self, b):
		bno = b.get_object('entry2').get_text()
		db = database()
		c = db.crsr()
		cur = c.cursor()
		arr = cur.execute("SELECT * FROM BILL WHERE bill_no = ? ORDER BY bill_no",(bno,))
		meta = ()
		

		for i in arr:
			meta = meta + i
		seldat = datetime.datetime.now().strptime(str(meta[1]),"%Y-%m-%d").strftime("%d-%m-%Y")
		b.get_object('sell_date').set_text(seldat)
		b.get_object('invoice_no').set_text(str(meta[0]))
		b.get_object('challan_no').set_text(str(meta[0]))
		b.get_object('vat').set_text(str(meta[3]))
		b.get_object('name').set_text(meta[5])
		b.get_object('address').set_text(meta[6])
		b.get_object('code').set_text(meta[7])
		b.get_object('other_charges').set_text(str(meta[4]))
		grand_total = (math.ceil(float(meta[2]) + float(meta[3])/float(100)*float(meta[2]) + float(meta[4]))) 
		b.get_object('grand_total').set_text(str(grand_total))
		
	def clear_n_bill(self, b):
		b.get_object('sell_date').set_text("")
		b.get_object('invoice_no').set_text("")
		b.get_object('challan_no').set_text("")
		b.get_object('vat').set_text("")
		b.get_object('name').set_text("")
		b.get_object('address').set_text("")
		b.get_object('code').set_text("")
		b.get_object('other_charges').set_text("")
		b.get_object('item_no').set_text("")
		b.get_object('item_name').set_text("")
		b.get_object('quantity').set_text("")
		b.get_object('price').set_text("")
		b.get_object('grand_total').set_text("")
		
	def show(self, b, x):
		db = database()
		c = db.crsr()
		bno = b.get_object('invoice_no').get_text()
		if bno == '':
			bno = b.get_object('entry2').get_text()
		bno = int(bno)
		i = c.cursor().execute("SELECT * FROM description where bill_no = ? ORDER BY sr_no",(bno,))
		arra = ()
		cc = 0
		for arr in i:
			if cc == 0:arra = arr; cc = cc + 1
			else:arra = arra + arr
		sr_no = ""
		item_name = ""
		quantity = ""
		i = c.cursor().execute("SELECT * FROM description where bill_no = ? ORDER BY sr_no",(bno,))
		cc = 0
		amt = ""
		weigh = ""
		amount_total = 0.0
		for countall in i:
			count = cc * 5
			sr_no = sr_no + str(arra[count]) + "\n"
			no = int(arra[count + 2])
			nn = c.cursor().execute("SELECT item_name FROM item_list where item_no = ?",(no,))
			amnt = c.cursor().execute("SELECT item_rate FROM item_list where item_no = ?",(no,))
			for i in nn:
				nam = i
			for i in amnt:
				amount = i
				amount = float(amount[0]) * arra[count + 3]
			item_name = item_name + str(nam[0]) + "\n"
			amt = amt + str(amount) + "\n"
			amount_total = amount_total + float(amount)		
			quantity = quantity + str(arra[count + 3]) + "\n"
			weigh = weigh + str(arra[count + 4]) + "\n"
			cc = cc + 1
		
		b.get_object('item_no').set_text(sr_no)
		b.get_object('item_name').set_text(item_name)
		b.get_object('quantity').set_text(quantity)
		b.get_object('price').set_text(amt)
		b.get_object('weight').set_text(weigh)

		if x == 1:
			return (float(amount_total))
		
		
	def del_description(self, no, b):
		db = database()
		c = db.crsr()
		cur = c.cursor()
		bno = int(b.get_object('invoice_no').get_text())
		cur.execute("DELETE FROM description where sr_no = ? AND bill_no = ?", (no, bno))
		c.commit()
		self.show(b, 0)
		
	def sav_bill_db(self, b, x):
		db = database()
		c = db.crsr()
		cur = c.cursor()
		amount = self.show(b, 1)		
		bill_no = int(b.get_object('invoice_no').get_text())
		sell_date = str(b.get_object('sell_date').get_text())
		sell_date = datetime.datetime.now().strptime(sell_date,"%d-%m-%Y").strftime("%Y-%m-%d")
		vat = float(b.get_object('vat').get_text())
		vat = amount * (vat / float(100))
		othr_chrgs = float(b.get_object('other_charges').get_text())
		round_off = ((amount + vat)*100)/100
		round_off = int(round_off)
		grand_total = round_off + othr_chrgs
		grand_total = math.ceil(grand_total)
		buyer_name = str(b.get_object("name").get_text())
		buyer_addr = str(b.get_object("address").get_text())
		buyer_code = str(b.get_object("code").get_text())
		vat = float(b.get_object('vat').get_text())
		import string; buyer_code = string.lower(buyer_code)
		if x == 1:
			cur.execute("UPDATE bill set sell_date = ?, amount = ?, vat = ?, other_charges = ?, buyer_name = ?, buyer_addr = ?, buyer_code =? WHERE bill_no = ?",(sell_date, amount, vat, othr_chrgs, buyer_name, buyer_addr, buyer_code, bill_no))
		else:
			cur.execute("INSERT INTO bill VALUES (?,?,?,?,?,?,?,?)",(bill_no, sell_date, amount, vat, othr_chrgs, buyer_name, buyer_addr, buyer_code))
		c.commit()
		grand_total = str(grand_total)
		b.get_object("grand_total").set_text(grand_total)
		
		
	def find_search(self, b):
		#try:
			date = b.get_object("search_date").get_text()
			if date != '':
				date = datetime.datetime.now().strptime(date,"%d-%m-%Y").strftime("%Y-%m-%d")
			code = b.get_object("search_cust_name").get_text()
			bill_no = b.get_object("search_bill_no").get_text()
			import string;code = string.lower(code)
			try:bill_no = int(bill_no)
			except ValueError: bill_no = 0
			db = database()
			c = db.crsr()
			cur = c.cursor()
			arr = cur.execute("SELECT bill_no, buyer_name FROM bill where bill_no = ? OR sell_date = ? OR buyer_code = ? ORDER BY bill_no",(bill_no, date, code))
			ab = ""
			i = ()
			for a in arr:
				i = i + a
			cc = 0
			k = len(i)/2
			for j in range(k):
				count = cc * 2
				ab = ab + str(i[count])  + "\t " + str(i[count + 1])  + "\n"
				cc = cc + 1
			b.get_object("search_result").set_text(ab)
			del ab
			c.commit()
		#except:
			#return
				
				
				
	def checkupdate(self, b):
		no = b.get_object("challan_no").get_text()
		no = int(no)
		db = database()
		con = db.crsr()
		cur = con.cursor()
		ar = cur.execute("SELECT bill_no FROM BILL WHERE bill_no = ?",(no,))
		if b.get_object("address").get_text() == '':
			naam = b.get_object("name").get_text().lower()
			tmpa = cur.execute("SELECT address FROM address WHERE name = ?",(naam,))
			for tp in tmpa:
				btp = tp
			b.get_object("address").set_text(btp[0])
		cc = ""
		for i in ar:
			cc = cc + str(i[0])
		if cc == "":
			self.sav_bill_db(b ,0)
		else:
			self.sav_bill_db(b ,1)



	def purchase(self, b):
		srno = b.get_object("entry3").get_text()
		srno = int(srno)
		date = b.get_object("entry4").get_text()
		name = b.get_object("entry5").get_text()
		total = float(b.get_object("entry6").get_text())
		tax = float(b.get_object("entry7").get_text())
		othrcharges = float(b.get_object("entry8").get_text())
		paid = float(b.get_object("entry9").get_text())
		cheque = b.get_object("entry10").get_text()
		date = datetime.datetime.now().strptime(date,"%d-%m-%Y").strftime("%Y-%m-%d")
		amnt = total + tax + othrcharges
		db = database()
		con = db.crsr()
		cur = con.cursor()
		arr = cur.execute("SELECT bill_no from purchase where bill_no = ?",(srno,))
		at = ""
		for i in arr:
			at = at + str(i)
		if at == "":
			x = 0
		else:
			x = 1
		if x == 0:
			cur.execute("INSERT INTO purchase VALUES (?,?,?,?,?,?,?,?,?)",(srno, date, name, total, tax, othrcharges, amnt, paid, cheque))
		if x == 1:
			cur.execute("UPDATE purchase set pur_date = ?, party_name = ?, total = ?, tax = ?, othercharges = ?, grand_total = ?, paid = ?, cheque_no = ? WHERE bill_no = ?",(date, name, total, tax, othrcharges, amnt, paid, cheque, srno))
		con.commit()
		
		
	def show_purchase(self ,b):
		db = database()
		con = db.crsr()
		cur = con.cursor()
		arr = cur.execute("SELECT * FROM purchase ORDER BY pur_date")
		pur = ()
		for i in arr:
			pur = pur + i
		
		srno = ""
		date = ""
		name = "" 
		total = ""
		tax = ""
		othrcharges = ""
		amnt = ""
		paid = ""
		cheque = ""
		count = len(pur)/9
		cc = 0
		for i in range(count):
			countall = cc * 9
			srno = srno + str(pur[countall]) + "\n"
			date = date + (datetime.datetime.now().strptime(str(pur[countall + 1]),"%Y-%m-%d").strftime("%d-%m-%Y")) + "\n"
			name = name + str(pur[countall + 2]) + "\n"
			total = total + str(pur[countall + 3]) + "\n"
			tax = tax + str(pur[countall + 4]) + "\n"
			othrcharges = othrcharges + str(pur[countall + 5]) + "\n"
			amnt = amnt + str(pur[countall + 6]) + "\n"
			paid = paid + str(pur[countall + 7]) + "\n"
			cheque = cheque + str(pur[countall + 8]) + "\n"
			cc = cc + 1
		b.get_object("label40").set_text(srno)
		b.get_object("label41").set_text(date)
		b.get_object("label42").set_text(name)
		b.get_object("label43").set_text(total)
		b.get_object("label44").set_text(tax)
		b.get_object("label45").set_text(othrcharges)
		b.get_object("label46").set_text(amnt)
		b.get_object("label47").set_text(paid)
		b.get_object("label48").set_text(cheque)
		
		
	def delpurclick1(self, no):
		db = database()
		con = db.crsr()
		cur = con.cursor()
		cur.execute("DELETE FROM purchase where bill_no = ?",(no,))
		con.commit()
		
		
	def showrecord(self, b):
		db = database()
		con = db.crsr()
		cur = con.cursor()
		fromdate = b.get_object("from_record").get_text()
		todate = b.get_object("to_record").get_text()
		fromdate = datetime.datetime.now().strptime(str(fromdate),"%d-%m-%Y").strftime("%Y-%m-%d")
		todate = datetime.datetime.now().strptime(str(todate),"%d-%m-%Y").strftime("%Y-%m-%d")
		array = cur.execute("SELECT bill_no, pur_date, party_name, grand_total, paid FROM purchase WHERE pur_date BETWEEN ? AND ? ORDER BY pur_date",(fromdate, todate))
		bill_no = ""
		date = ""
		name = ""
		grd_total = ""
		arr = ()
		for i in array:
			arr = arr + i
		count = len(arr)/4
		cc = 0
		totalamt = 0.0
		totalbal = 0.0
		for j in range(count):
			countall = cc * 4
			bill_no = bill_no + str(arr[countall]) + "\n"
			d = datetime.datetime.now().strptime(str(arr[countall + 1]),"%Y-%m-%d").strftime("%d-%m-%Y")
			date = date + d + "\n"			
			name = name + str(arr[countall + 2]) + "\n"
			grd_total = grd_total + str(arr[countall + 3]) + "\n"
			totalamt = totalamt + float(arr[countall + 3])
			totalbal = totalamt - (totalbal + float(arr[countall + 4]))
			cc = cc + 1
			
		b.get_object("label78").set_text(bill_no)
		b.get_object("label79").set_text(date)
		b.get_object("label80").set_text(name)
		b.get_object("label81").set_text(grd_total)
		totalamt = str(totalamt)
		b.get_object("itempurchased").set_text(totalamt)
		b.get_object("label69").set_text(str(totalbal))
		
		array = cur.execute("SELECT bill_no, sell_date, buyer_name, amount, vat, other_charges FROM bill WHERE sell_date BETWEEN ? AND ? ORDER BY sell_date",(fromdate, todate))
		bill_no = ""
		date = ""
		name = ""
		grd_total = ""
		arr = ()
		for i in array:
			arr = arr + i
		count = len(arr)/6
		cc = 0
		totalamnt = 0.0
		total = 0.0
		for j in range(count):
			countall = cc * 6
			bill_no = bill_no + str(arr[countall]) + "\n"
			d = datetime.datetime.now().strptime(str(arr[countall + 1]),"%Y-%m-%d").strftime("%d-%m-%Y")
			date = date + d + "\n"
			name = name + str(arr[countall + 2]) + "\n"
			total = float(arr[countall + 3]) + float(arr[countall + 4]) + float(arr[countall + 5])
			totalamnt = totalamnt + total
			grd_total = grd_total + str(total) + "\n"
			total = 0.0
			cc = cc + 1
			
		b.get_object("label82").set_text(bill_no)
		b.get_object("label83").set_text(date)
		b.get_object("label84").set_text(name)
		b.get_object("label85").set_text(grd_total)
		b.get_object("itemsold").set_text(str(totalamnt))
		
		
		
	def viewrecord(self, b):
		strtemp = b.get_object("entry12").get_text()
		db = database()
		con = db.crsr()
		cur = con.cursor()
		
		arra = cur.execute("SELECT pur_date, grand_total, paid FROM purchase where party_name = ?",(strtemp,))
		date = ''
		grndtotal = ''
		gt = 0.0
		paid = 0.0
		arr = ()
		for n in arra:
			arr = arr + n 
		count = len(arr)/3
		i = 0
		for n in range(count):
			i = i * 3
			date = date + str(arr[i]) + '\n'
			grndtotal = grndtotal + str(arr[i+1]) + '\n'
			gt = gt + float(arr[i+1])
			paid = paid + float(arr[i+2])
			
		gt= str(gt)
		paid = str(paid)
		b.get_object("purdate").set_text(str(date))
		b.get_object("billpur").set_text(str(grndtotal))
		b.get_object("label91").set_text(str(gt))
		b.get_object("label93").set_text(str(paid))

