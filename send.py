#coding=utf-8
import RPi.GPIO as GPIO
import Tkinter as tk
import time
import tkMessageBox
    
def chineseToBin(chinese):
	"""
	chinese：输入框单个字符
	"""
	hexCode=chinese.encode('unicode_escape')[2:] #汉字转unicode，4个16进制
	binCode = list("0"*16)
	code=str(bin(int(hexCode,16))[2:])#16进制转2进制
	binCode[-len(code):]=code	#补充二进制前面被去掉的0
	return binCode
	
def on_click():
	info_uni=out_entry.get()#获得输入的内容
	codeExtend=[]
	for chinese in info_uni :
		binCode = chineseToBin(chinese)
		codeExtend=codeExtend+binCode
	codeExtend=list('1')+codeExtend+list('0')
	for info in codeExtend:
		GPIO.output(12, int(info))
		time.sleep(INTERVAL) #发送频率，间隔0.1s

root=tk.Tk()
root.geometry('800x480')
root.wm_title("发送信号")
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
INTERVAL=0.05

line1=tk.Frame(root)
line1.pack(pady=40)
btn = tk.Button(root ,text=u'发射信号',width=10,height=3, font =('Helvetica', '14'),command=on_click)
btn.pack()
label=tk.Label(line1,text=u"发出信号：" ,font =(u"宋体", 14, "normal"))
label.pack(side='left')
out_text = tk.StringVar()
out_entry =tk.Entry(line1, textvariable = out_text,width=60,font = ('Helvetica', '14'))
out_text.set("")
out_entry.pack(side='left')

root.mainloop()
