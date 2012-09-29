#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  officexport.py
#  
#  Copyright 2012 Veeraj <veeraj@veeraj-VirtualBox>
#  
#  
#  This file exports odt document

import sys
sys.path.append( "/home/john/precision_final" )
from appy.pod.renderer import Renderer
from database import *
import datetime
import test

class pod:
	def tablechallan(self, b):
		
		global custname
		global custadd
		global billno
		global date
		custname = b.get_object("name").get_text()		
		custadd = b.get_object("address").get_text()
		billno = b.get_object("invoice_no").get_text()
		date = b.get_object("sell_date").get_text()
		global sr1
		sr1 = ''
		global sr2
		sr2 = ''
		global sr3
		sr3 = ''
		global sr4
		sr4 = ''
		global sr5
		sr5 = ''
		global sr6
		sr6 = ''
		global sr7
		sr7 = ''
		global sr8
		sr8 = ''
		global sr9
		sr9 = ''
		global sr10
		sr10 = ''
		db = database()
		con = db.crsr()
		crsr = con.cursor()
		#arra = crsr.execute('SELECT sr_no from description where bill_no = ? ORDER BY sr_no',(int(billno),))
		splitemp = b.get_object('item_no').get_text()
		arr = splitemp.split('\n')
		#for i in arra:
			#arr = arr + i
		try:
			if arr[0] is not None:
				sr1 = str(arr[0])
			if arr[1] is not None:
				sr2 = str(arr[1])
			if arr[2] is not None:
				sr3 = str(arr[2])
			if arr[3] is not None:
				sr4 = str(arr[3])
			if arr[4] is not None:
				sr5 = str(arr[4])
			if arr[5] is not None:
				sr6 = str(arr[5])
			if arr[6] is not None:
				sr7 = str(arr[6])
			if arr[7] is not None:
				sr8 = str(arr[7])
			if arr[8] is not None:
				sr9 = str(arr[8])
			if arr[9] is not None:
				sr10 = str(arr[9])
		except:
			 a =0 		
			 
		global par1
		par1 = ''
		global par2
		par2 = ''
		global par3
		par3 = ''
		global par4
		par4 = ''
		global par5
		par5 = ''
		global par6
		par6 = ''
		global par7
		par7 = ''
		global par8
		par8 = ''
		global par9
		par9 = ''
		global par10
		par10 = ''
		
		#arra = crsr.execute('SELECT item_name FROM item_list WHERE item_no IN (SELECT item_no FROM description WHERE bill_no = ? ORDER BY sr_no)',(int(billno),))
		splitemp = b.get_object('item_name').get_text()
		arr = splitemp.split('\n')
		#for i in arra:
			#arr = arr + i
		try:
			if arr[0] is not None:
				par1 = str(arr[0])
			if arr[1] is not None:
				par2 = str(arr[1])
			if arr[2] is not None:
				par3 = str(arr[2])
			if arr[3] is not None:
				par4 = str(arr[3])
			if arr[4] is not None:
				par5 = str(arr[4])
			if arr[5] is not None:
				par6 = str(arr[5])
			if arr[6] is not None:
				par7 = str(arr[6])
			if arr[7] is not None:
				par8 = str(arr[7])
			if arr[8] is not None:
				par9 = str(arr[8])
			if arr[9] is not None:
				par10 = str(arr[9])
		except:
			a = 0
			
		global no1
		no1 = ''
		global no2
		no2 = ''
		global no3
		no3 = ''
		global no4
		no4 = ''
		global no5
		no5 = ''
		global no6
		no6 = ''
		global no7
		no7 = ''
		global no8
		no8 = ''
		global no9
		no9 = ''
		global no10
		no10 =''
		global w1
		w1 = ''
		global w2
		w2 = ''
		global w3
		w3 = ''
		global w4
		w4 = ''
		global w5
		w5 = ''
		global w6
		w6 = ''
		global w7
		w7 = ''
		global w8
		w8 = ''
		global w9
		w9 = ''
		global w10
		w10 = ''
		arra = crsr.execute('SELECT quantity, weight FROM description WHERE bill_no = ? ORDER BY sr_no',(int(billno),))
		arr = ()
		for i in arra:
			arr = arr + i
			
		try:
			if arr[0] is not None:
				no1 = str(arr[0])
			if arr[1] is not None:
				w1 = str(arr[1])
			if arr[2] is not None:
				no2 = str(arr[2])
			if arr[3] is not None:
				w2 = str(arr[3])
			if arr[4] is not None:
				no3 = str(arr[4])
			if arr[5] is not None:
				w3 = str(arr[5])
			if arr[6] is not None:
				no4 = str(arr[6])
			if arr[7] is not None:
				w4 = str(arr[7])
			if arr[8] is not None:
				no5 = str(arr[8])
			if arr[9] is not None:
				w5 = str(arr[9])
			if arr[10] is not None:
				no6 = str(arr[10])
			if arr[11] is not None:
				w6 = str(arr[11])
			if arr[12] is not None:
				no7 = str(arr[12])
			if arr[13] is not None:
				w7 = str(arr[13])
			if arr[14] is not None:
				no8 = str(arr[14])
			if arr[15] is not None:
				w8 = str(arr[15])
			if arr[16] is not None:
				no9 = str(arr[16])
			if arr[17] is not None:
				w9 = str(arr[17])
			if arr[18] is not None:
				no10 = str(arr[18])
			if arr[19] is not None:
				w10 = str(arr[19])
		except:
			a = 0
			
		#arra = crsr.execute('SELECT item_rate FROM item_list WHERE item_no IN (SELECT item_no FROM description WHERE bill_no = ? ORDER BY sr_no)',(int(billno),))
		arr = ()
		arra = crsr.execute('SELECT item_list.item_rate FROM item_list,description WHERE item_list.item_no = description.item_no AND description.bill_no = ? ORDER BY description.sr_no',(int(billno),))
		for i in arra:
			arr = arr + i
		global ra1
		ra1 = ''
		global ra2
		ra2= ''
		global ra3
		ra3 = ''
		global ra4
		ra4 = ''
		global ra5
		ra5 = ''
		global ra6
		ra6 = ''
		global ra7
		ra7 = ''
		global ra8
		ra8 = ''
		global ra9
		ra9 = ''
		global ra10
		ra10 = ''
		try:
			if arr[0] is not None:
				ra1 = str(arr[0])
			if arr[1] is not None:
				ra2 = str(arr[1])
			if arr[2] is not None:
				ra3 = str(arr[2])
			if arr[3] is not None:
				ra4 = str(arr[3])
			if arr[4] is not None:
				ra5 = str(arr[4])
			if arr[5] is not None:
				ra6 = str(arr[5])
			if arr[6] is not None:
				ra7 = str(arr[6])
			if arr[7] is not None:
				ra8 = str(arr[7])
			if arr[8] is not None:
				ra9 = str(arr[8])
			if arr[9] is not None:
				ra10 = str(arr[9])
		except:
			a = 0
			
		arra = crsr.execute('SELECT quantity FROM description WHERE bill_no = ? ORDER BY sr_no',(int(billno),))
		q = ()
		for i in arra:
			q = q + i
		global rs1, rp1
		rs1 = ''
		rp1 = ''
		global rs2, rp2
		rs2 = ''
		rp2 = ''
		global rs3, rp3
		rs3 = ''
		rp3 = ''
		global rs4, rp4
		rs4 = ''
		rp4 = ''
		global rs5, rp5
		rs5 = ''
		rp5 = ''
		global rs6, rp6
		rs6 = ''
		rp6 = ''
		global rs7, rp7
		rs7 = ''
		rp7 = ''
		global rs8, rp8
		rs8 = ''
		rp8 = ''
		global rs9, rp9
		rs9 = ''
		rp9 = ''
		global rs10, rp10
		rs10 = ''
		rp10 = ''
		
		amrp = 0.0
		try:
			temp = str(float(arr[0]) * int(q[0]))
			if ra1 is not None:
				amrp = amrp + float(temp)
				rs1 = temp.split('.')[0]
				if temp.split('.')[1] == '0':
					rp1 = '00'
				else:
					rp1 = temp.split('.')[1]
			temp = str(float(arr[1]) * int(q[1]))
			if ra2 is not None:
				amrp = amrp + float(temp)
				rs2 = temp.split('.')[0]
				if temp.split('.')[1] == '0':
					rp2 = '00'
				else:
					rp2 = temp.split('.')[1]
			temp = str(float(arr[2]) * int(q[2]))
			if ra3 is not None:
				amrp = amrp + float(temp)
				rs3 = temp.split('.')[0]
				if temp.split('.')[1] == '0':
					rp3 = '00'
				else:
					rp3 = temp.split('.')[1]
			temp = str(float(arr[3]) * int(q[3]))
			if ra4 is not None:
				amrp = amrp + float(temp)
				rs4 = temp.split('.')[0]
				if temp.split('.')[1] == '0':
					rp4 = '00'
				else:
					rp4 = temp.split('.')[1]
			temp = str(float(arr[4]) * int(q[4]))
			if ra5 is not None:
				amrp = amrp + float(temp)
				rs5 = temp.split('.')[0]
				if temp.split('.')[1] == '0':
					rp5 = '00'
				else:
					rp5 = temp.split('.')[1]
			temp = str(float(arr[5]) * int(q[5]))
			if ra6 is not None:
				amrp = amrp + float(temp)
				rs6 = temp.split('.')[0]
				if temp.split('.')[1] == '0':
					rp6 = '00'
				else:
					rp6 = temp.split('.')[1]
			temp = str(float(arr[6]) * int(q[6]))
			if ra7 is not None:
				amrp = amrp + float(temp)
				rs7 = temp.split('.')[0]
				if temp.split('.')[1] == '0':
					rp7 = '00'
				else:
					rp7 = temp.split('.')[1]
			temp = str(float(arr[7]) * int(q[7]))
			if ra8 is not None:
				amrp = amrp + float(temp)
				rs8 = temp.split('.')[0]
				if temp.split('.')[1] == '0':
					rp8 = '00'
				else:
					rp8 = temp.split('.')[1]
			temp = str(float(arr[8]) * int(q[8]))
			if ra9 is not None:
				amrp = amrp + float(temp)
				rs9 = temp.split('.')[0]
				if temp.split('.')[1] == '0':
					rp9 = '00'
				else:
					rp9 = temp.split('.')[1]
			temp = str(float(arr[9]) * int(q[9]))
			if ra10 is not None:
				amrp = amrp + float(temp)
				rs10 = temp.split('.')[0]
				if temp.split('.')[1] == '0':
					rp10 = '00'
				else:
					rp10 = temp.split('.')[1]
		
		except:
			a = 0
		
				
		
		global challanno
		challanno = b.get_object("invoice_no").get_text()
		global datech
		datech = b.get_object("sell_date").get_text()
		global rate
		rate = b.get_object("price").get_text()
		global grdtotal
		temp = b.get_object("grand_total").get_text()
		a = temp.split('.')
		grdtotal = a[0]
		import logic
		l = logic.logic()
		amntrp = amrp
		amnrp = str(amntrp)	
		global vat
		vat = b.get_object("vat").get_text()
		global totalrs
		totalrs = amnrp.split('.')[0]
		global totalps
		if amnrp.split('.')[1] == '0':
			totalps = '00'
		else:
			totalps = amnrp.split('.')[1]
		vatrp = b.get_object("grand_total").get_text()
		temp = (float(vat) * float(amnrp))/float(100)
		temp = str(temp)
		temp = temp.split('.')
		global vatrs
		vatrs = temp[0]
		global vatps
		if temp[1] == '0':
			vatps = '00'
		else:
			vatps = temp[1]
		tmp1 = b.get_object("other_charges").get_text()
		if tmp1.find('.') == -1:
			tmp1 = tmp1 +'.0'
		temp = tmp1.split('.')
		global roundoffrs
		roundoffrs = temp[0]
		global roundofps
		if temp[0] == '0' :
			roundofps = '00'
		else:
			roundofps = temp[1]
		
		
		
		global word
		word = test.number_to_words(int(grdtotal)) + 'Only'
		
		flnm =  '/home/john/fine_bill/' + billno + "challan.odt"
		renderer = Renderer('/home/john/Fine_contacts/fchallan.odt', globals(), flnm)
		renderer.run()
		flnm = '/home/john/fine_bill/' + billno +'invoice.odt'
		renderer = Renderer('/home/john/Fine_contacts/finvoice.odt', globals(), flnm)
		renderer.run()

		
