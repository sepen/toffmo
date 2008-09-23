#!/usr/bin/env python
#
# Toffmo: The Office Motivator

import ConfigParser
import pygtk
pygtk.require('2.0')
import gtk
import datetime

class Toffmo:
	
	CONFIG_FILE='/home/sepen/devel/toffmo/src/toffmo.conf'
	MONEY_PER_HOUR='10'
	MONEY_SUFFIX='EUR'
	TIME_WORK_START='08:00'
	TIME_WORK_STOP='17:30'
	TIME_PAUSE_START='13:30'
	TIME_PAUSE_STOP='14:30'
	
	def parse_config_file(self):
		cfg = ConfigParser.ConfigParser()
		cfg.readfp(file(self.CONFIG_FILE))
		self.TIME_WORK_START = cfg.get('userconf', 'TIME_WORK_START'.lower())
		self.TIME_WORK_STOP = cfg.get('userconf', 'TIME_WORK_STOP'.lower())
		self.TIME_PAUSE_START = cfg.get('userconf', 'TIME_PAUSE_START'.lower())
		self.TIME_PAUSE_STOP = cfg.get('userconf', 'TIME_PAUSE_STOP'.lower())
		return
		
	def get_today_date(self):
		return datetime.datetime.now().strftime("%A %B %d %I:%M:%S %p %Y")
	
	def get_today_money(self):
		# TODO: calculate money
		return "XX"
		
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
		label = gtk.Label(self.get_today_date() + "\nEarned today: " + self.get_today_money() + " " + self.MONEY_SUFFIX + "\n" )
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

