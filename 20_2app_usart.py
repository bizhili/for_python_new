
import tkinter as tk
from tkinter import ttk
import serial
import threading
import time
class GUI:
    def __init__(self):
        window = tk.Tk()
        window.title("GUI Serial")
        def quit():
        	window.destroy()
        	exit("quit")
        self.uartState = False # is uart open or not

        # a frame contains COM's information, and start/stop button
        frame_COMinf = tk.Frame(window)
        frame_COMinf.grid(row = 1, column = 1)

        labelCOM = tk.Label(frame_COMinf,text="COMx: ")
        self.COM = tk.StringVar(value = "COM2")
        ertryCOM = tk.Entry(frame_COMinf, textvariable = self.COM)
        labelCOM.grid(row = 1, column = 1, padx = 5, pady = 3)
        ertryCOM.grid(row = 1, column = 2, padx = 5, pady = 3)

        labelBaudrate = tk.Label(frame_COMinf,text="Baudrate: ")
        self.Baudrate = tk.IntVar(value = 9600)
        ertryBaudrate = tk.Entry(frame_COMinf, textvariable = self.Baudrate)
        labelBaudrate.grid(row = 1, column = 3, padx = 5, pady = 3)
        ertryBaudrate.grid(row = 1, column = 4, padx = 5, pady = 3)

        labelParity = tk.Label(frame_COMinf,text="Parity: ")
        self.Parity = tk.StringVar(value ="NONE")
        comboParity = ttk.Combobox(frame_COMinf, width = 17, textvariable=self.Parity)
        comboParity["values"] = ("NONE","ODD","EVEN","MARK","SPACE")
        comboParity["state"] = "readonly"
        labelParity.grid(row = 2, column = 1, padx = 5, pady = 3)
        comboParity.grid(row = 2, column = 2, padx = 5, pady = 3)

        labelStopbits = tk.Label(frame_COMinf,text="Stopbits: ")
        self.Stopbits = tk.StringVar(value ="1")
        comboStopbits = ttk.Combobox(frame_COMinf, width = 17, textvariable=self.Stopbits)
        comboStopbits["values"] = ("1","1.5","2")
        comboStopbits["state"] = "readonly"
        labelStopbits.grid(row = 2, column = 3, padx = 5, pady = 3)
        comboStopbits.grid(row = 2, column = 4, padx = 5, pady = 3)
        
        self.buttonSS = tk.Button(frame_COMinf, text = "Start", command = self.processButtonSS)
        self.buttonSS.grid(row = 3, column = 4, padx = 5, pady = 3, sticky = tk.E)
        # serial object
        self.ser = serial.Serial()
        # serial read threading
        self.ReadUARTThread = threading.Thread(target=self.ReadUART)
        self.ReadUARTThread.start()

        self.buttonSS1 = tk.Button(frame_COMinf, text = "quit", command = quit)
        self.buttonSS1.grid(row = 4, column = 3, padx = 5, pady = 3, sticky = tk.E)
        # serial object
        self.ser = serial.Serial()
        # serial read threading
        self.ReadUARTThread = threading.Thread(target=self.ReadUART)
        self.ReadUARTThread.start()

        frameRecv = tk.Frame(window)
        frameRecv.grid(row = 2, column = 1)
        labelOutText = tk.Label(frameRecv,text="Received Data:")
        labelOutText.grid(row = 1, column = 1, padx = 3, pady = 2, sticky = tk.W)
        frameRecvSon = tk.Frame(frameRecv)
        frameRecvSon.grid(row = 2, column =1)
        scrollbarRecv = tk.Scrollbar(frameRecvSon)
        scrollbarRecv.pack(side = tk.RIGHT, fill = tk.Y)
        self.OutputText = tk.Text(frameRecvSon, wrap = tk.WORD, width = 60, height = 5, yscrollcommand = scrollbarRecv.set)
        self.OutputText.pack()

        frameRecv = tk.Frame(window)
        frameRecv.grid(row = 1, column = 2)
        labelOutText = tk.Label(frameRecv,text="1 Data:")
        labelOutText.grid(row = 1, column = 1, padx = 3, pady = 2, sticky = tk.W)
        frameRecvSon = tk.Frame(frameRecv)
        frameRecvSon.grid(row = 2, column =1)
        self.OutputText1 = tk.Text(frameRecvSon, wrap = tk.WORD, width = 10, height = 2, yscrollcommand = scrollbarRecv.set)
        self.OutputText1.pack()

        frameRecv = tk.Frame(window)
        frameRecv.grid(row = 2, column = 2)
        labelOutText = tk.Label(frameRecv,text="2 Data:")
        labelOutText.grid(row = 1, column = 1, padx = 3, pady = 2, sticky = tk.W)
        frameRecvSon = tk.Frame(frameRecv)
        frameRecvSon.grid(row = 2, column =1)
        self.OutputText2 = tk.Text(frameRecvSon, wrap = tk.WORD, width = 10, height = 2, yscrollcommand = scrollbarRecv.set)
        self.OutputText2.pack()

        frameRecv = tk.Frame(window)
        frameRecv.grid(row = 3, column = 2)
        labelOutText = tk.Label(frameRecv,text="3 Data:")
        labelOutText.grid(row = 1, column = 1, padx = 3, pady = 2, sticky = tk.W)
        frameRecvSon = tk.Frame(frameRecv)
        frameRecvSon.grid(row = 2, column =1)
        self.OutputText3 = tk.Text(frameRecvSon, wrap = tk.WORD, width = 10, height = 2, yscrollcommand = scrollbarRecv.set)
        self.OutputText3.pack()


        frameRecv = tk.Frame(window)
        frameRecv.grid(row = 1, column = 3)
        labelOutText = tk.Label(frameRecv,text="4 Data:")
        labelOutText.grid(row = 1, column = 1, padx = 3, pady = 2, sticky = tk.W)
        frameRecvSon = tk.Frame(frameRecv)
        frameRecvSon.grid(row = 2, column =1)
        self.OutputText4 = tk.Text(frameRecvSon, wrap = tk.WORD, width = 10, height = 2, yscrollcommand = scrollbarRecv.set)
        self.OutputText4.pack()

        frameRecv = tk.Frame(window)
        frameRecv.grid(row = 2, column = 3)
        labelOutText = tk.Label(frameRecv,text="5 Data:")
        labelOutText.grid(row = 1, column = 1, padx = 3, pady = 2, sticky = tk.W)
        frameRecvSon = tk.Frame(frameRecv)
        frameRecvSon.grid(row = 2, column =1)
        self.OutputText5 = tk.Text(frameRecvSon, wrap = tk.WORD, width = 10, height = 2, yscrollcommand = scrollbarRecv.set)
        self.OutputText5.pack()

        frameRecv = tk.Frame(window)
        frameRecv.grid(row = 3, column = 3)
        labelOutText = tk.Label(frameRecv,text="6 Data:")
        labelOutText.grid(row = 1, column = 1, padx = 3, pady = 2, sticky = tk.W)
        frameRecvSon = tk.Frame(frameRecv)
        frameRecvSon.grid(row = 2, column =1)
        self.OutputText6 = tk.Text(frameRecvSon, wrap = tk.WORD, width = 10, height = 2, yscrollcommand = scrollbarRecv.set)
        self.OutputText6.pack()

        frameRecv = tk.Frame(window)
        frameRecv.grid(row = 1, column = 4)
        labelOutText = tk.Label(frameRecv,text="7 Data:")
        labelOutText.grid(row = 1, column = 1, padx = 3, pady = 2, sticky = tk.W)
        frameRecvSon = tk.Frame(frameRecv)
        frameRecvSon.grid(row = 2, column =1)
        self.OutputText7 = tk.Text(frameRecvSon, wrap = tk.WORD, width = 10, height = 2, yscrollcommand = scrollbarRecv.set)
        self.OutputText7.pack()

        frameRecv = tk.Frame(window)
        frameRecv.grid(row = 2, column = 4)
        labelOutText = tk.Label(frameRecv,text="8 Data:")
        labelOutText.grid(row = 1, column = 1, padx = 3, pady = 2, sticky = tk.W)
        frameRecvSon = tk.Frame(frameRecv)
        frameRecvSon.grid(row = 2, column =1)
        self.OutputText8 = tk.Text(frameRecvSon, wrap = tk.WORD, width = 10, height = 2, yscrollcommand = scrollbarRecv.set)
        self.OutputText8.pack()

        frameRecv = tk.Frame(window)
        frameRecv.grid(row = 3, column = 4)
        labelOutText = tk.Label(frameRecv,text="9 Data:")
        labelOutText.grid(row = 1, column = 1, padx = 3, pady = 2, sticky = tk.W)
        frameRecvSon = tk.Frame(frameRecv)
        frameRecvSon.grid(row = 2, column =1)
        self.OutputText9 = tk.Text(frameRecvSon, wrap = tk.WORD, width = 10, height = 2, yscrollcommand = scrollbarRecv.set)
        self.OutputText9.pack()



        frameTrans = tk.Frame(window)
        frameTrans.grid(row = 3, column = 1)
        labelInText = tk.Label(frameTrans,text="To Transmit Data:")
        labelInText.grid(row = 1, column = 1, padx = 3, pady = 2, sticky = tk.W)
        frameTransSon = tk.Frame(frameTrans)
        frameTransSon.grid(row = 2, column =1)
        scrollbarTrans = tk.Scrollbar(frameTransSon)
        scrollbarTrans.pack(side = tk.RIGHT, fill = tk.Y)
        self.InputText = tk.Text(frameTransSon, wrap = tk.WORD, width = 60, height = 5, yscrollcommand = scrollbarTrans.set)
        self.InputText.pack()
        self.buttonSend = tk.Button(frameTrans, text = "Send", command = self.processButtonSend)
        self.buttonSend.grid(row = 3, column = 1, padx = 5, pady = 3, sticky = tk.E)
        
        window.mainloop()
        

    def processButtonSS(self):
        # print(self.Parity.get())
        if (self.uartState):
            self.ser.close()
            self.buttonSS["text"] = "Start"
            self.uartState = False
        else:
            # restart serial port
            self.ser.port = self.COM.get()
            self.ser.baudrate = self.Baudrate.get()
            
            strParity = self.Parity.get()
            if (strParity=="NONE"):
                self.ser.parity = serial.PARITY_NONE;
            elif(strParity=="ODD"):
                self.ser.parity = serial.PARITY_ODD;
            elif(strParity=="EVEN"):
                self.ser.parity = serial.PARITY_EVEN;
            elif(strParity=="MARK"):
                self.ser.parity = serial.PARITY_MARK;
            elif(strParity=="SPACE"):
                self.ser.parity = serial.PARITY_SPACE;
                
            strStopbits = self.Stopbits.get()
            if (strStopbits == "1"):
                self.ser.stopbits = serial.STOPBITS_ONE;
            elif (strStopbits == "1.5"):
                self.ser.stopbits = serial.STOPBITS_ONE_POINT_FIVE;
            elif (strStopbits == "2"):
                self.ser.stopbits = serial.STOPBITS_TWO;
            
            self.ser.open()
            if (self.ser.isOpen()): # open success
                self.buttonSS["text"] = "Stop"
                self.uartState = True

    def processButtonSend(self):
        if (self.uartState):
            strToSend = self.InputText.get(1.0,tk.END)
            bytesToSend = strToSend[0:-1].encode(encoding='ascii')
            self.ser.write(bytesToSend)
            print(bytesToSend)
        else:
            print("Not In Connect!")

    def ReadUART(self):
        nowtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        while True:
            if (self.uartState):
                ch = self.ser.read().decode(encoding="utf-8")
                ch=str(ch)
                print(ch)
                self.OutputText2.insert(0.0,ch)


GUI()










