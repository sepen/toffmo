#!/usr/bin/env python
#
# Toffmo: The Office Motivator
# by Jose V Beneyto, sepen at users dot sourceforge dot net

import ConfigParser
import pygtk
pygtk.require('2.0')
import gtk
import time
import datetime

class Toffmo:
	
	APP_NAME='toffmo'
	APP_VERSION='0.1-rc1'
	
	CONFIG_DIR=''
	CONFIG_FILE='toffmo.conf'
	
	DATA_DIR=''
	
	MONEY_PER_HOUR=10
	MONEY_SUFFIX='EUR'
	TIME_WORK_START='08:00'
	TIME_WORK_STOP='17:30'
	TIME_PAUSE_START='13:30'
	TIME_PAUSE_STOP='14:30'
	
	def parse_config_file(self):
		cfg = ConfigParser.ConfigParser()
		cfg.readfp(file(self.CONFIG_DIR + self.CONFIG_FILE))
		
		self.MONEY_PER_HOUR = cfg.get('userconf', 'MONEY_PER_HOUR'.lower())
		self.MONEY_SUFFIX = cfg.get('userconf', 'MONEY_SUFFIX'.lower())
		self.TIME_WORK_START = cfg.get('userconf', 'TIME_WORK_START'.lower())
		self.TIME_WORK_STOP = cfg.get('userconf', 'TIME_WORK_STOP'.lower())
		self.TIME_PAUSE_START = cfg.get('userconf', 'TIME_PAUSE_START'.lower())
		self.TIME_PAUSE_STOP = cfg.get('userconf', 'TIME_PAUSE_STOP'.lower())
		
		return True
	
	def get_today_date(self):
		return datetime.datetime.now().strftime("%H:%M - %d/%m/%Y")
	
	def get_elapsed_time(self):
		date_now = datetime.datetime.now()
		time_now = datetime.time(date_now.hour, date_now.minute, date_now.second)
		
		time_work_start_list = self.TIME_WORK_START.split(':')
		time_work_start = datetime.time(int(time_work_start_list[0]), int(time_work_start_list[1]))
		time_work_stop_list = self.TIME_WORK_STOP.split(':')
		time_work_stop = datetime.time(int(time_work_stop_list[0]), int(time_work_stop_list[1]))
		time_pause_start_list = self.TIME_PAUSE_START.split(':')
		time_pause_start = datetime.time(int(time_pause_start_list[0]), int(time_pause_start_list[1]))
		time_pause_stop_list = self.TIME_PAUSE_STOP.split(':')
		time_pause_stop = datetime.time(int(time_pause_stop_list[0]), int(time_pause_stop_list[1]))
		
		t_now = datetime.timedelta(hours=time_now.hour, minutes=time_now.minute, seconds=time_now.second)
		t_work_start = datetime.timedelta(hours=time_work_start.hour, minutes=time_work_start.minute, seconds=time_work_start.second)
		t_pause_start = datetime.timedelta(hours=time_pause_start.hour, minutes=time_pause_start.minute, seconds=time_pause_start.second)
		t_pause_stop = datetime.timedelta(hours=time_pause_stop.hour, minutes=time_pause_stop.minute, seconds=time_pause_stop.second)
		
		if time_work_start < time_now < time_pause_start:
			#print "DEBUG> de manyanas y cobro"
			t = t_now - t_work_start
		elif time_pause_start < time_now < time_pause_stop:
			#print "DEBUG> comiendo y no cobro"
			t = t_pause_start - t_work_start
		elif time_pause_stop < time_now < time_work_stop:
			#print "DEBUG> de tardes y cobro"
			t = (t_now - t_pause_stop) + (t_pause_start - t_work_start)
		else:
			#print "DEBUG> fuera de hora y no cobro"
			t = t_now - t_now
		return t

	def get_today_money(self):
		time = self.get_elapsed_time()
		money_per_second = float(self.MONEY_PER_HOUR) / 3600
		money = int(time.seconds * money_per_second)
		return money
	
	def get_text_message(self):
		message = "\n" + self.get_today_date() + "\n\n" \
			+ "Hours: " + str(self.get_elapsed_time()) + " (" \
			+ self.MONEY_PER_HOUR + self.MONEY_SUFFIX + "/hour)\n" \
			+ "Earned: " + str(self.get_today_money()) +  " " \
			+ self.MONEY_SUFFIX + "\n"
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
		window.set_size_request(205, 370) # width x height
		window.set_resizable(False)
		window.set_title("toffmo")
		# create vbox
		vbox = gtk.VBox(False, 0)
		window.add(vbox)
		vbox.show()
		# add image to vbox
		image = gtk.Image()
		image.set_from_file(self.DATA_DIR + "earn.jpg")
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
    return True
  
if __name__ == "__main__":
  Toffmo()
  main()

