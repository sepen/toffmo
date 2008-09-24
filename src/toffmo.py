#!/usr/bin/env python
#
# Toffmo: The Office Motivator

import ConfigParser
import pygtk
pygtk.require('2.0')
import gtk
import time
import datetime

class Toffmo:
	
	CONFIG_FILE='toffmo.conf'
	MONEY_PER_HOUR='10'
	MONEY_SUFFIX='EUR'
	TIME_WORK_START='08:00'
	TIME_WORK_STOP='17:30'
	TIME_PAUSE_START='13:30'
	TIME_PAUSE_STOP='14:30'
	
	def parse_config_file(self):
		cfg = ConfigParser.ConfigParser()
		cfg.readfp(file(self.CONFIG_FILE))
		self.MONEY_PER_HOUR = cfg.get('userconf', 'MONEY_PER_HOUR'.lower())
		self.MONEY_SUFFIX = cfg.get('userconf', 'MONEY_SUFFIX'.lower())
		self.TIME_WORK_START = cfg.get('userconf', 'TIME_WORK_START'.lower())
		self.TIME_WORK_STOP = cfg.get('userconf', 'TIME_WORK_STOP'.lower())
		self.TIME_PAUSE_START = cfg.get('userconf', 'TIME_PAUSE_START'.lower())
		self.TIME_PAUSE_STOP = cfg.get('userconf', 'TIME_PAUSE_STOP'.lower())
		return
	
	def get_today_date(self):
		return datetime.datetime.now().strftime("%A %B %d %I:%M:%S %p %Y")
	
	def get_today_money(self):
		money = ""
		date_now = datetime.datetime.now()
		time_now = datetime.time(date_now.hour, date_now.minute, date_now.second)
		time_work_start_list = self.TIME_WORK_START.split(':')
		time_work_start = datetime.time(int(time_work_start_list[0]), int(time_work_start_list[1]))
		time_work_stop_list = self.TIME_WORK_STOP.split(':')
		time_work_stop = datetime.time(int(time_work_stop_list[0]), int(time_work_stop_list[1]))
		time_pause_start_list = self.TIME_PAUSE_START.split(':')
		time_pause_start = datetime.time(int(time_pause_start_list[0]), int(time_pause_start_list[1]))
		time_pause_stop_list = self.TIME_WORK_START.split(':')
		time_pause_stop = datetime.time(int(time_pause_stop_list[0]), int(time_pause_stop_list[1]))
		if time_work_start < time_now < time_pause_start:
			print "DEBUG> de manyanas y cobro"
			money = ""
		elif time_pause_start < time_now < time_pause_stop:
			print "DEBUG> comiendo y no cobro"
			money = ""
		elif time_pause_stop < time_now < time_work_stop:
			print "DEBUG> de tardes y cobro"
			money = ""
		else:
			print "DEBUG> fuera de hora y no cobro"
			money = ""
		return money
	
	def get_text_message(self):
		message = self.get_today_date() + "\nEarned today: " \
			+ self.get_today_money() + " " + self.MONEY_SUFFIX + "\n"
		return message
	
	def close_application(self, widget, event, data=None):
		gtk.main_quit()
		return False
	
	def __init__(self):
		# get values from config file
		self.parse_config_file()
		# create the main window
		window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		window.connect("delete_event", self.close_application)
		window.set_border_width(10)
		window.set_size_request(300, 420)
		window.set_resizable(False)
		window.set_title("toffmo 0.1-beta1")
		# create vbox
		vbox = gtk.VBox(False, 0)
		window.add(vbox)
		vbox.show()
		# add image to vbox
		image = gtk.Image()
		image.set_from_file("image.jpg")
		vbox.add(image)
		image.show()
		# add frame and label to vbox
		frame = gtk.Frame()
		label = gtk.Label(self.get_text_message())
		frame.add(label)
		label.show()
		vbox.add(frame)
		frame.show()
		# finally show the main window
		window.show()
		
def main():
    gtk.main()
    return 0
  
if __name__ == "__main__":
  Toffmo()
  main()

