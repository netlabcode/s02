import binascii
import _thread
import time
import socket
import time
import sqlite3
from sqlite3 import Error
import datetime

#Predefined parameters
MU01 = '100.1.0.11'
MU02 = '100.1.0.12'
MU03 = '100.1.0.13'
MU04 = '100.1.0.14'
PORT1 = 991
PORT2 = 992

def funcname(self, parameter_list):
	"""
	docstring
	"""
	raise NotImplementedError

def create_connection(db_file):
	conn = None
	try:
		conn = sqlite3.connect(db_file, timeout=10)
	except Error as e:
		print(e)
	return conn


def db_connect():
	datafile="s01.db"
	con = create_connection(datafile)
	return con


# Define a function for the thread
def serverMU01():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s1:
		s1.connect((MU01, PORT1))
		x = 1
		while x < 6:
			#recive data from server
			data1 = s1.recv(1024)
			
			try: 
				#parsing data
				data1new = data1.decode("utf-8")
				datet,a,b,ce,d,e,f = data1new.split("+")

				#save db
				con = db_connect()
				c = con.cursor()
				#datet = datetime.datetime.now()
				c.execute("INSERT INTO mu01(xtime, B39_Li_01_39_CB_ctrl, B39_Li_01_39_CB_res, B39_Li_01_39_I_res, B39_Li_01_39_P_res, B39_Li_01_39_Q_res, B39_Li_01_39_V_res) VALUES (?,?,?,?,?,?,?)",(datet,int(a),int(b),float(ce),float(d),float(e),float(f)))
				#c.execute("INSERT INTO mu01(xtime, B23_Li_23_24_CB_ctrl) VALUES (?,?)",(datet,int(a)))
				con.commit()
				con.close()
			except Exception:
				print("mu01")
				pass



def serverMU02():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s2:
		s2.connect((MU02, PORT1))
		x = 1
		while x < 6:
			#recive data from server
			data2 = s2.recv(1024)
			#print('MU02:',data2)

			#parsing data
			data1new = data2.decode("utf-8")

			try:
				datet,a,b,ce,d,e,f = data1new.split("+")
				#save db
				con = db_connect()
				c = con.cursor()
				#datet = datetime.datetime.now()
				c.execute("INSERT INTO mu02(xtime, B39_Li_09_39_V_res, B39_Li_09_39_CB_ctrl, B39_Li_09_39_CB_res, B39_Li_09_39_I_res, B39_Li_09_39_P_res, B39_Li_09_39_Q_res) VALUES (?,?,?,?,?,?,?)",(datet,float(a),int(b),int(ce),float(d),float(e),float(f)))
				#c.execute("INSERT INTO mu01(xtime, B23_Li_23_24_CB_ctrl) VALUES (?,?)",(datet,int(a)))
				con.commit()
				con.close()
			except Exception:
				print("mu02")
				pass


def serverMU03():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s2:
		s2.connect((MU03, PORT1))
		x = 1
		while x < 6:
			#recive data from server
			data2 = s2.recv(1024)

			#parsing data
			data1new = data2.decode("utf-8")

			try:
				datet,a,b,ce,d,e = data1new.split("+")
				#save db
				con = db_connect()
				c = con.cursor()
				#datet = datetime.datetime.now()
				c.execute("INSERT INTO mu03(xtime, B39_Ld39_CB_ctrl, B39_Ld39_CB_res, B39_Ld39_P_res, B39_Ld39_Q_res, B39_Ld39_V_res) VALUES (?,?,?,?,?,?)",(datet,int(a),int(b),float(ce),float(d),float(e)))
				#c.execute("INSERT INTO mu01(xtime, B23_Li_23_24_CB_ctrl) VALUES (?,?)",(datet,int(a)))
				con.commit()
				con.close()
			except Exception:
				print("mu03")
				pass


def serverMU04():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s2:
		s2.connect((MU04, PORT1))
		x = 1
		while x < 6:
			#recive data from server
			data2 = s2.recv(1024)
			#print('MU02:',data2)

			#parsing data
			data1new = data2.decode("utf-8")

			try:
				datet,a,b,ce,d,e,f,g,h,i = data1new.split("+")
				#save db
				con = db_connect()
				c = con.cursor()
				#datet = datetime.datetime.now()
				c.execute("INSERT INTO mu04(xtime, B39_G1_CB_ctrl, B39_G1_CB_res, B39_G1_f_res, B39_G1_Ld_res, B39_G1_P_ctrl, B39_G1_P_res, B39_G1_Q_res, B39_G1_V_ctrl, B39_G1_V_res) VALUES (?,?,?,?,?,?,?,?,?,?)",(datet,int(a),int(b),float(ce),float(d),float(e),float(f), float(g), float(h), float(i)))
				#c.execute("INSERT INTO mu01(xtime, B23_Li_23_24_CB_ctrl) VALUES (?,?)",(datet,int(a)))
				con.commit()
				con.close()
			except Exception:
				print("mu04")
				pass

#def serverMU05():
#	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s2:
#		s2.connect((MU05, PORT1))
#		x = 1
#		while x < 6:
#			data2 = s2.recv(1024)
			#print('MU02:',data2)

			#parsing data
#			data1new = data2.decode("utf-8")

#			try:
#				datet,a,b = data1new.split("+")
				#save db
#				con = db_connect()
#				c = con.cursor()
				#datet = datetime.datetime.now()
#				c.execute("INSERT INTO mu05(xtime, B30_TR_CB_ctrl, B30_TR_CB_res) VALUES (?,?,?)",(datet,int(a),int(b)))
				#c.execute("INSERT INTO mu01(xtime, B23_Li_23_24_CB_ctrl) VALUES (?,?)",(datet,int(a)))
#				con.commit()
#				con.close()
#			except Exception:
#				print("mu05")
#				pass


#def serverMU06():
#	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s2:
#		s2.connect((MU06, PORT1))
#		x = 1
#		while x < 6:
#			#recive data from server
#			data2 = s2.recv(1024)
#
#			#parsing data
#			data1new = data2.decode("utf-8")
#
#			try:
#				datet,a,b,ce,d,e,f,g,h,i = data1new.split("+")
#				#save db
#				con = db_connect()
#				c = con.cursor()
				#datet = datetime.datetime.now()
#				c.execute("INSERT INTO mu06(xtime, B30_G10_CB_ctrl, B30_G10_CB_res, B30_G10_f_res, B30_G10_Ld_res, B30_G10_P_ctrl, B30_G10_P_res, B30_G10_Q_res, B30_G10_V_ctrl, B30_G10_V_res) VALUES (?,?,?,?,?,?,?,?,?,?)",(datet,int(a),int(b),float(ce),float(d),float(e),float(f),float(g),float(h),float(i)))
				#c.execute("INSERT INTO mu01(xtime, B23_Li_23_24_CB_ctrl) VALUES (?,?)",(datet,int(a)))
#				con.commit()
#				con.close()
#			except Exception:
#				print("mu06")
#				pass


# Create two threads as follows
try:
   _thread.start_new_thread( serverMU01, ( ) )
   _thread.start_new_thread( serverMU02, ( ) )
   _thread.start_new_thread( serverMU03, ( ) )
   _thread.start_new_thread( serverMU04, ( ) )
except:
   print ("Error: unable to start thread")

while 1:
   pass
