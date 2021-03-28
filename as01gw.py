import binascii
import _thread
import time
import socket
import psycopg2


HOST1 = '100.1.0.11'
HOST2 = '100.1.0.12'
HOST3 = '100.1.0.13'
HOST4 = '100.1.0.14'
PORT1 = 993
PORT2 = 994
PORTS1 = 881
PORTS2 = 883


#Database Connection
conn = psycopg2.connect(host="131.180.165.5",database="crpg", user="postgres", password="crpg")
conn.autocommit = True
cursor = conn.cursor()

# Define a function for the thread
def serverOne():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc1:
		sc1.connect((HOST1, PORT1))
		
		x = 1
		while x < 6:
			#recive data from server A
			data1 = sc1.recv(1024)

			strval1 = str(data1.decode("utf-8"))

			a,b,c,d,e,f,g = strval1.split("+")

			inserted_values = (
        		a,
        		b,
        		c,
        		d,
        		e,
        		f,
        		g
    		)

			cursor.execute(" INSERT INTO s01m1(dtime, cb_ctrl, cb_res, i_res, p_res, q_res, v_res) VALUES (%s,%s,%s,%s,%s,%s,%s)", inserted_values)

			print("1")

def serverTwo():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc1:
		sc1.connect((HOST2, PORT1))
		
		x = 1
		while x < 6:
			#recive data from server A
			data1 = sc1.recv(1024)

			strval1 = str(data1.decode("utf-8"))

			a,b,c,d,e,f,g = strval1.split("+")

			inserted_values = (
        		a,
        		b,
        		c,
        		d,
        		e,
        		f,
        		g
    		)

			cursor.execute(" INSERT INTO s01m2(dtime, v_res, cb_ctrl, cb_res, i_res, p_res, q_res) VALUES (%s,%s,%s,%s,%s,%s,%s)", inserted_values)

			print("2")


def serverThree():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc1:
		sc1.connect((HOST3, PORT1))
		
		x = 1
		while x < 6:
			#recive data from server A
			data1 = sc1.recv(1024)

			strval1 = str(data1.decode("utf-8"))

			a,b,c,d,e,f = strval1.split("+")

			inserted_values = (
        		a,
        		b,
        		c,
        		d,
        		e,
        		f
    		)

			cursor.execute(" INSERT INTO s01m3(dtime, cb_ctrl, cb_res, p_res, q_res, v_res) VALUES (%s,%s,%s,%s,%s,%s)", inserted_values)

			print("3")

def serverFour():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc1:
		sc1.connect((HOST4, PORT1))
		
		x = 1
		while x < 6:
			#recive data from server A
			data1 = sc1.recv(1024)

			strval1 = str(data1.decode("utf-8"))

			a,b,c,d,e,f,g,h,i,j = strval1.split("+")

			inserted_values = (
        		a,
        		b,
        		c,
        		d,
        		e,
        		f,
        		g,
                h,
                i,
                j
    		)

			cursor.execute(" INSERT INTO s01m4(dtime, cb_ctrl, cb_res, f_res, ld_res, p_ctrl, p_res, q_res, , v_ctrl , v_res) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", inserted_values)

			print("4")


# Create two threads as follows
try:
   _thread.start_new_thread( serverOne, ( ) )
   _thread.start_new_thread( serverTwo, ( ) )
   _thread.start_new_thread( serverThree, ( ) )
   _thread.start_new_thread( serverFour, ( ) )
   
except:
   print ("Error: unable to start thread")

while 1:
   pass
