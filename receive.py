#coding=utf-8
import RPi.GPIO as GPIO
import Tkinter as tk
import time
import tkMessageBox
import threading

def Bintochinese(Bin):
	"""
	Bin:16位二进制字符串list
	"""
	Bin_str=''.join(Bin)
	print Bin_str
	Hex=hex(int(Bin_str,2))[2:]           
	s=unichr(int(str(Hex),16))
	return s
def getLight():
	time.sleep(INTERVAL)
	value=GPIO.input(in_Pin)
	if value==1:
		return "0"
	elif value==0:
		return "1"

def receive():
	while(1):
		if getLight()=="1":
			in_text.set("")
			while 1:
				code=[]
				for i in range(16):
					code.append(getLight())
				if code==list(16*"0"):
					break
				else:
					chinese=Bintochinese(code)
					print chinese
					in_text.set(in_text.get()+chinese)

root=tk.Tk()
root.geometry('800x480')
root.wm_title("接收信号")
GPIO.setmode(GPIO.BOARD)
in_Pin=18
GPIO.setup(in_Pin, GPIO.IN)
INTERVAL=0.05

line2=tk.Frame(root)
line2.pack(pady=40)
label=tk.Label(line2,text=u"接受信号：" ,font =("宋体", 14,"normal"))
label.pack(side='left')
in_text = tk.StringVar()
in_entry =tk.Entry(line2, textvariable = in_text ,width=60,font = ('Helvetica', '14'))
in_text.set("")
in_entry.pack(side='left')

t = threading.Thread(target=receive)
t.setDaemon(True)
t.start()

root.mainloop()