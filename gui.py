
import sys
import gtk
import gtk.glade
sys.path.append( "/home/john/Fine_contacts" )
from logic import *
#import easygui

class load_gui:
	company_name = "Precision Press"
	def __init__(self):
		self.builder = gtk.Builder()
		self.builder.add_from_file("/home/john/Fine_contacts/gui.glade")
		self.main_window = self.builder.get_object("main_window")
		self.add_item_name = self.builder.get_object("add_item_name")
		self.item_delet = self.builder.get_object("item_delet")
		self.item_delet1 = self.builder.get_object("item_delet1")
		self.item_detail = self.builder.get_object("item_detail")
		self.new_bill_window = self.builder.get_object("new_bill_window")
		self.purchase_window = self.builder.get_object("purchase_window")
		self.search_window = self.builder.get_object("search_window")
		self.view_record_window = self.builder.get_object("view_record_window")
		self.ynbox = self.builder.get_object("ynbox")
		self.a_i_t_b = self.builder.get_object("add_item_to_bill")
		self.search_result_window = self.builder.get_object("search_result_window")
		self.vbox20 = self.builder.get_object("window_bill_no")
		self.add_purchase_window = self.builder.get_object("add_purchase_window")
		self.window1 = self.builder.get_object("window1")
		self.window2 = self.builder.get_object("window2")
		self.window3 = self.builder.get_object("window3")
		self.window4 = self.builder.get_object("window4")
		self.window5 = self.builder.get_object("window5")
		self.window6 = self.builder.get_object("window6")
		self.delwindel = self.builder.get_object("delwindel")
		
		dic = {
		"on_quit_clicked" : self.quit,
		"on_new_bill_clicked" : self.n_bill,
		"on_search_bill_clicked" : self.s_bill,
		"on_records_clicked" : self.vr_bill,
		"on_items_clicked" : self.it_details,
		"on_purchase_clicked" : self.purchase,
		"on_ynboxyes_clicked" : self.ynboxyes,
		"on_ynboxno_clicked" : self.ynboxno,
		"on_item_back_clicked" : self.itemback,
		"on_back_bill_clicked" : self.backbill,
		"on_purchase_back_clicked" : self.purchaseback,
		"on_search_back_clicked" : self.searchback,
		"on_back_view_clicked" : self.backview,
		"on_add_item_add_clicked" : self.add_item,
		"on_item_add_clicked" : self.itemadd,
		"on_add_item_cancel_clicked" : self.itemcancel,
		"on_item_delete_clicked" : self.delitem,
		"on_item_delete_delete_clicked" : self.delit,
		"on_item_delete_cancel_clicked" : self.backdel,
		"on_add_bill_clicked" : self.ad_bil,
		"on_item_bac_clicked" : self.ad_back,
		"on_item_ad_clicked" : self.add_to_bill,
		"on_delete_bill_clicked" : self.i_del,
		"on_button1_cancel_clicked" : self.i_cancel,
		"on_button2_clicked" : self.i_delete,
		"on_save_clicked" : self.sav_bill,
		"on_search_find_clicked" : self.find,
		"on_button1_clicked" : self.but_back,
		"on_open_bill_clicked" : self.show_bll,
		"on_open_clicked" : self.openb,
		"on_pur_add_clicked" : self.pur_add,
		"on_cancel_clicked" : self.pur_sav_cancel,
		"on_save_pur_clicked" : self.pur_sav,
		"on_pur_delete_clicked" : self.purdel,
		"on_button3_clicked" : self.purdel_hide,
		"on_button4_clicked" : self.delpurclick,
		"on_record_view_clicked" : self.recordview,
		"on_button5_clicked" : self.okie,
		"on_button6_clicked" : self.closeabout,
		"on_about_clicked" : self.about,
		"on_print_bill_clicked" : self.printbill,
		"on_view_purchased_clicked" : self.viewpurchased,
		"on_viewback_clicked" : self.hidepurchase,
		"on_viewfind_clicked" : self.viewfind,
		"on_button8_clicked" : self.window5ok,
		"on_adres_clicked" : self.adreswindow5,
		"on_button7_clicked" : self.addkk,
		"on_button9_clicked" : self.hidekk,
		"on_button10_clicked" : self.adadres,
		"on_button11_clicked" : self.deladres,
		"on_button12_clicked" : self.delbck,
		"on_button13_clicked" : self.deldbadd
		}
		
		self.builder.connect_signals( dic )
	
	def deldbadd(self, widget):
		name = self.builder.get_object("entry15").get_text().lower()
		db = database()
		con = db.crsr()
		crsr = con.cursor()
		crsr.execute("DELETE FROM address WHERE name = ?",(name, ))
		con.commit()
		self.showadres()
		self.delwindel.hide()
		
	def delbck(self, widget):
		self.delwindel.hide()
	
	def deladres(self, widget):
		self.delwindel.show()
		
	def adadres(self, widget):
		name = self.builder.get_object("entry13").get_text().lower()
		address = self.builder.get_object("entry14").get_text()
		db = database()
		con = db.crsr()
		crsr = con.cursor()
		crsr.execute("INSERT INTO address VALUES(?,?)",(name, address))
		con.commit()
		self.showadres()
		self.window6.hide()
	
	def showadres(self):
		db = database()
		con = db.crsr()
		crsr = con.cursor()
		arr = crsr.execute("SELECT * FROM address")
		a = ()
		for i in arr:
			a = a + i
		temp1 = ''
		temp2 = ''
		count = 0
		for i in range(len(a)/2):
			countall = count * 2
			temp1 = temp1 + a[countall] + '\n'
			temp2 = temp2 + a[countall + 1] + '\n'			
			count = count + 1
		self.builder.get_object("label95").set_text(temp1)
		self.builder.get_object("label96").set_text(temp2)
			
	def hidekk(self, widget):
		self.window6.hide()
		
	def addkk(self, widget):
		self.window6.show()
		
	
	def adreswindow5(self, widget):
		self.showadres()
		self.window5.show()
		
	def window5ok(self, widget):
		self.window5.hide()
		
	def viewfind(self, widget):
		l = logic()
		l.viewrecord(self.builder)
	
	def viewpurchased(self, widget):
		self.window4.show()
		self.builder.get_object("purdate").set_text('')
		self.builder.get_object("billpur").set_text('')
		
	def hidepurchase(self, widget):
		self.window4.hide()
		
	def printbill(self, widget):
		import export
		prnt = export.pod()
		prnt.tablechallan(self.builder)
	
	def about(self, widget):
		self.window3.show()
		self.main_window.hide()
		
	def closeabout(self, widget):
		self.window3.hide()
		self.main_window.show()
		
	def okie(self, widget):
		self.window2.hide()
		self.main_window.show()
	
	def recordview(self, widget):
		self.window2.show()
		l = logic()
		self.view_record_window.hide()
		l.showrecord(self.builder)
	
	
	def delpurclick(self, widget):
		l =logic()
		no = int(self.builder.get_object("entry11").get_text())
		l.delpurclick1(no)
		self.window1.hide()
		l.show_purchase(self.builder)
	
	def purdel_hide(self, widget):
		self.window1.hide()
		
	def purdel(self, widget):
		self.window1.show()
		self.builder.get_object("entry11").set_text("")
			
	def pur_sav(self, widget):
		l = logic()
		l.purchase(self.builder)
		l.show_purchase(self.builder)
		self.add_purchase_window.hide()
		
	def pur_sav_cancel(self, widget):
		self.add_purchase_window.hide()
		
	def pur_add(self, widget):
		self.add_purchase_window.show()
		l = logic()
		self.builder.get_object("entry4").set_text(l.datenow)
	
	
	def openb(self, widget):
		l = logic()
		l.show(self.builder, 0)
		l.show_bi(self.builder)
		self.new_bill_window.show()
		self.vbox20.hide()
		self.search_result_window.hide()
		self.search_window.hide()
		
	def show_bll(self, widget):
		self.vbox20.show()
						
		
	def but_back(self, widget):
		self.search_result_window.hide()
		
	def find(self, widget):
		self.search_result_window.show()
		l = logic()
		l.find_search(self.builder)
		
		
	def i_delete(self, widget):
		self.item_delet1.hide()
		no = self.builder.get_object("entry1").get_text()
		no = int(no)
		l = logic()
		l.del_description(no, self.builder)
		
	def quit(self, widget):
		self.main_window.hide()
		self.ynbox.show()
		
	def i_del(self, widget):
		self.item_delet1.show()
		self.builder.get_object("entry1").set_text("")
	
	def i_cancel(self, widget):
		self.item_delet1.hide()
		
	def ynbox():
		self.ynbox.show()
		self.main_window.hide()
		
	def ynboxyes(self, widget):
		exit(0)
		
	def ynboxno(self, widget):
		self.ynbox.hide()
		self.main_window.show()
		
	def n_bill(self, widget):
		self.new_bill_window.show()
		l = logic()
		dateset = l.dates()
		num = l.invoice_num()
		num = str(num)
		self.builder.get_object("sell_date").set_text(dateset)
		self.builder.get_object("challan_no").set_text(num)
		self.builder.get_object("invoice_no").set_text(num)
		self.builder.get_object("weight").set_text('')
		self.main_window.hide()
		
	def s_bill(self, widget):
		self.main_window.hide()
		self.search_window.show()
		
	def vr_bill(self, widget):
		self.main_window.hide()
		self.view_record_window.show()
		
	def it_details(self, widget):
		self.item_detail.show()
		l = logic()
		l.itad(self.builder)
	
	
	def purchase(self, widget):
		self.main_window.hide()
		l = logic()
		l.show_purchase(self.builder)
		self.purchase_window.show()
		
		
	def itemback(self, widget):
		self.item_detail.hide()
		self.main_window.show()
		
	def backbill(self, widget):
		self.new_bill_window.hide()
		self.main_window.show()
		l = logic()
		l.clear_n_bill(self.builder)
		
	def purchaseback(self, widget):
		self.purchase_window.hide()
		self.main_window.show()
		
	def searchback(self, widget):
		self.search_window.hide()
		self.main_window.show()
		
	def backview(self, widget):
		self.view_record_window.hide()
		self.main_window.show()
		
		
	def itemadd(self, widget):
		self.add_item_name.show()
		l = logic()
		item_ne = l.i_num()
		item_ne = str(item_ne)
		self.builder.get_object("item_na").set_text("")
		self.builder.get_object("item_rat").set_text("")
		self.builder.get_object("item_num").set_text(item_ne)
		
	def itemcancel(self, widget):
		self.add_item_name.hide()
		
		
	def add_item(self, widget):
		item_name = self.builder.get_object("item_na").get_text()
		item_rate = self.builder.get_object("item_rat").get_text()
		item_re = self.builder.get_object("item_num").get_text()
		item_name = str(item_name)
		item_rate = float(item_rate)
		item_re  = int(item_re)
		l = logic()
		l.item_add(item_re, item_name, item_rate)
		self.add_item_name.hide()
		l.itad(self.builder)
		
	def delitem(self, widget):
		self.item_delet.show()
		
	def delit(self, widget):
		l = logic()
		no = self.builder.get_object("item_delete_text").get_text()
		#no = int(no)
		l.deletelogic(no)
		self.item_delet.hide()
		l.itad(self.builder)
		
	def backdel(self, widget):
		self.item_delet.hide()
		l = logic()
		l.itad(self.builder)
		
	def ad_bil(self, widget):
		self.a_i_t_b.show()
		self.builder.get_object("sr_no").set_text("")
		self.builder.get_object("add_i_no").set_text("")
		self.builder.get_object("add_quantity").set_text("")
		self.builder.get_object("item_weight").set_text("")
		l = logic()
		
		
	def ad_back(self, widget):
		self.a_i_t_b.hide()
		
		
	def add_to_bill(self, widget):
		self.a_i_t_b.hide()
		l = logic()
		l.add_to_bill(self.builder)
		l.show(self.builder, 0)
		
	def sav_bill(self, widget):
		l = logic()
		l.checkupdate(self.builder)
		

