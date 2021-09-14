from java.lang import String
#import serial
import re
import time
import os, sys


class Dexarm:
    """[summary]
    """

    def __init__(self, name, port):

        #self.ser1 = serial.Serial(port, 115200, timeout=None)
        #self.is_open = self.ser1.isOpen()
        self.ser1 = Runtime.start(name,"Serial")
        self.ser1.connect(port, 115200, 8, 1, 0)
        self.is_open = self.ser1.isConnected()
        if self.is_open:
            print('pydexarm: %s connected' % self.ser1.name)
        else:
            print('failed to connect to serial port')

    def _send_cmd1(self, data, wait=True):

        self.ser1.write(data.encode())
        if not wait:
            self.ser1.reset()
            return
        while True:
            serial_str = self.ser1.readString().decode("utf-8")
            if len(serial_str) > 0:
                if serial_str.find("ok") > -1:
                    print("read ok")
                    break
                else:
                    print("read:", serial_str)

    def send_gcode1(self, wait=True):
        ####This is a personal test.
        self.ser1.writeFile('test1.gcode')
        if not wait:
            self.ser1.reset()
            return
        while True:
            serial_str = self.ser1.readString().decode("utf-8")
            if len(serial_str) > 0:
                if serial_str.find("ok") > -1:
                    print("read ok")
                    break
                else:
                    print("read:", serial_str)                

    def go_home1(self):
        """
        Go to home position and enable the motors. Should be called each time when power on.
        """
        self._send_cmd1("M1112\r")

    #def move_down1(self):
        #This is a personal test.
        #self._send_cmd1("X0 Y0 Z-10 E0\r")

    def set_relativeDown1(self):
        #This is a personal test.
        self._send_cmd1("G91\r")
        self._send_cmd1("G0 Z-5\n")
        self._send_cmd1("G90\r")

    def set_relativeUp1(self):
        #This is a personal test.
        self._send_cmd1("G91\r")
        self._send_cmd1("G0 Z5\n")
        self._send_cmd1("G90\r")    

    def set_absolute1(self):
        #This is a personal test.
        self._send_cmd1("G90\r")

    def read_test1(self):
        #This is a personal test.
        self._send_cmd1("G0 X-80.33 Y338.19\n")
        self._send_cmd1("G0 Z0\n")
        self._send_cmd1("G0 X80.33 Y338.19\n")
        self._send_cmd1("G0 X80.33 Y300.19\n")
        self._send_cmd1("G0 X-80.33 Y300.19\n")
        self._send_cmd1("G0 X-80.33 Y338.19\n")
        self._send_cmd1("G0 X0 Y338.19\n")
        self._send_cmd1("G0 Z20\n")
        #self._send_cmd1("G0 X0 Y300\n")
        #self._send_cmd1("G0 X-25 Y-25\n")
        #self._send_cmd1("G0 X25 Y-25\n")
        #self._send_cmd1("G0 X25 Y25\n")
        #self._send_cmd1("G0 X0 Y50\n")
        #self._send_cmd1("G0 X-25 Y25\n")
        #self._send_cmd1("G0 X-25 Y-25\n")
        #self._send_cmd1("G0 X25 Y25\n")
        #self._send_cmd1("G0 X-25 Y25\n")
        #self._send_cmd1("G0 X25 Y-25\n")
        #This is a personal test.
        
    ##Remix of test1.gcode worky!    
    def remix(self):
        self._send_cmd1("M2000\n")
        self._send_cmd1("M888 P0\n")
        self._send_cmd1("G0 X-80.33 Y337.72\n")
        self._send_cmd1("G0 Z0\n")
        self._send_cmd1("G0 X-80.02 Y338.19\n")
        self._send_cmd1("G0 X-79.70 Y338.35\n")
        self._send_cmd1("G0 X-79.55 Y338.19\n")
        self._send_cmd1("G0 X-79.55 Y338.03\n")
        self._send_cmd1("G0 X-79.70 Y337.40\n")
        self._send_cmd1("G0 X-79.86 Y336.93\n")
        self._send_cmd1("G0 Z5\n")
        self._send_cmd1("G0 X-79.70 Y337.40\n")
        self._send_cmd1("G0 Z0\n")
        self._send_cmd1("G0 X-79.55 Y337.72\n")
        self._send_cmd1("G0 X-79.23 Y338.19\n")
        self._send_cmd1("G0 X-78.92 Y338.35\n")
        self._send_cmd1("G0 X-78.60 Y338.35\n")
        self._send_cmd1("G0 X-78.44 Y338.19\n")
        self._send_cmd1("G0 X-78.44 Y338.03\n")
        self._send_cmd1("G0 X-78.60 Y337.40\n")
        self._send_cmd1("G0 X-78.76 Y336.93\n")

        self._send_cmd1("G0 Z80\n")
        self._send_cmd1("G0 X0 Y190\n")
        #self._send_cmd1("M601\n")
    
    ##Remix of letter1.gcode worky!
    def remix2(self):
        self._send_cmd1("M2000\n")
        self._send_cmd1("M888 P0\n")
        self._send_cmd1("F2000\n")
        self._send_cmd1("G0 Z5\n")
        self._send_cmd1("G0 X-80.33 Y337.72\n")
        self._send_cmd1("G0 Z0\n")
        self._send_cmd1("G0 X-80.02 Y338.19\n")
        self._send_cmd1("G0 X-79.70 Y338.35\n")
        self._send_cmd1("G0 X-79.55 Y338.19\n")
        self._send_cmd1("G0 X-79.55 Y338.03\n")
        self._send_cmd1("G0 X-79.70 Y337.40\n")
        self._send_cmd1("G0 X-79.86 Y336.93\n")
        self._send_cmd1("G0 Z5\n")
        self._send_cmd1("G0 X-79.70 Y337.40\n")
        self._send_cmd1("G0 Z0\n")
        self._send_cmd1("G0 X-79.55 Y337.72\n")
        self._send_cmd1("G0 X-79.23 Y338.19\n")
        self._send_cmd1("G0 X-78.92 Y338.35\n")
        self._send_cmd1("G0 X-78.60 Y338.35\n")
        self._send_cmd1("G0 X-78.44 Y338.19\n")
        self._send_cmd1("G0 X-78.44 Y338.03\n")
        self._send_cmd1("G0 X-78.60 Y337.40\n")
        self._send_cmd1("G0 X-78.76 Y336.93\n")
        self._send_cmd1("G0 Z5\n")
        self._send_cmd1("G0 X-78.60 Y337.40\n")
        self._send_cmd1("G0 Z0\n")
        self._send_cmd1("G0 X-78.44 Y337.72\n")
        self._send_cmd1("G0 X-78.13 Y338.19\n")
        self._send_cmd1("G0 X-77.81 Y338.35\n")
        self._send_cmd1("G0 X-77.50 Y338.35\n")
        self._send_cmd1("G0 X-77.34 Y338.19\n")
        self._send_cmd1("G0 X-77.34 Y337.87\n")
        self._send_cmd1("G0 X-77.50 Y337.40\n")
        self._send_cmd1("G0 X-77.50 Y337.09\n")
        self._send_cmd1("G0 X-77.34 Y336.93\n")
        self._send_cmd1("G0 X-77.18 Y336.93\n")
        self._send_cmd1("G0 X-76.87 Y337.09\n")
        self._send_cmd1("G0 X-76.71 Y337.24\n")
        self._send_cmd1("G0 X-76.40 Y337.72\n")
        self._send_cmd1("G0 Z5\n")
        self._send_cmd1("G0 X-77.08 Y337.72\n")
        self._send_cmd1("G0 Z0\n")
        self._send_cmd1("G0 X-76.76 Y338.35\n")
        self._send_cmd1("G0 X-77.08 Y337.40\n")
        self._send_cmd1("G0 X-77.08 Y337.09\n")
        self._send_cmd1("G0 X-76.92 Y336.93\n")
        self._send_cmd1("G0 X-76.60 Y336.93\n")
        self._send_cmd1("G0 X-76.29 Y337.09\n")
        self._send_cmd1("G0 X-75.97 Y337.40\n")
        self._send_cmd1("G0 X-75.66 Y337.87\n")
        self._send_cmd1("G0 Z5\n")
        self._send_cmd1("G0 X-75.50 Y338.35\n")
        self._send_cmd1("G0 Z0\n")
        self._send_cmd1("G0 X-76.44 Y335.51\n")
        self._send_cmd1("G0 X-76.60 Y335.20\n")
        self._send_cmd1("G0 X-76.92 Y335.04\n")
        self._send_cmd1("G0 X-77.08 Y335.20\n")
        self._send_cmd1("G0 X-77.08 Y335.51\n")
        self._send_cmd1("G0 X-76.92 Y335.98\n")
        self._send_cmd1("G0 X-76.44 Y336.46\n")
        self._send_cmd1("G0 X-75.97 Y336.77\n")
        self._send_cmd1("G0 X-75.66 Y336.93\n")
        self._send_cmd1("G0 X-75.18 Y337.21\n")
        self._send_cmd1("G0 X-74.71 Y337.72\n")
        self._send_cmd1("G0 Z5\n")
        self._send_cmd1("G0 X-70.34 Y338.35\n")
        self._send_cmd1("G0 Z0\n")
        self._send_cmd1("G0 X-70.65 Y338.35\n")
        self._send_cmd1("G0 X-70.96 Y338.19\n")
        self._send_cmd1("G0 X-71.12 Y338.03\n")
        self._send_cmd1("G0 X-71.28 Y337.72\n")
        self._send_cmd1("G0 X-71.28 Y337.40\n")
        self._send_cmd1("G0 X-71.12 Y337.09\n")
        self._send_cmd1("G0 X-70.81 Y336.93\n")
        self._send_cmd1("G0 X-70.49 Y336.93\n")
        self._send_cmd1("G0 X-70.18 Y337.09\n")
        self._send_cmd1("G0 X-70.02 Y337.24\n")
        self._send_cmd1("G0 X-69.86 Y337.56\n")
        self._send_cmd1("G0 X-69.86 Y337.87\n")
        self._send_cmd1("G0 X-70.02 Y338.19\n")
        self._send_cmd1("G0 X-70.34 Y338.35\n")
        self._send_cmd1("G0 X-70.49 Y338.19\n")
        self._send_cmd1("G0 X-70.49 Y337.87\n")
        self._send_cmd1("G0 X-70.34 Y337.56\n")
        self._send_cmd1("G0 X-70.02 Y337.40\n")
        self._send_cmd1("G0 X-69.55 Y337.40\n")
        self._send_cmd1("G0 X-69.23 Y337.56\n")
        self._send_cmd1("G0 X-69.08 Y337.72\n")
        self._send_cmd1("G0 Z5\n")
        self._send_cmd1("G0 X-69.23 Y337.72\n")
        self._send_cmd1("G0 Z0\n")
        self._send_cmd1("G0 X-68.92 Y338.19\n")
        self._send_cmd1("G0 X-68.76 Y338.50\n")
        self._send_cmd1("G0 X-68.92 Y337.87\n")
        self._send_cmd1("G0 X-69.86 Y335.04\n")
        self._send_cmd1("G0 Z5\n")
        self._send_cmd1("G0 X-68.92 Y337.87\n")
        self._send_cmd1("G0 Z0\n")
        self._send_cmd1("G0 X-68.76 Y338.19\n")
        self._send_cmd1("G0 X-68.45 Y338.35\n")
        self._send_cmd1("G0 X-68.13 Y338.35\n")
        self._send_cmd1("G0 X-67.82 Y338.19\n")
        self._send_cmd1("G0 X-67.66 Y337.87\n")
        self._send_cmd1("G0 X-67.66 Y337.56\n")
        self._send_cmd1("G0 X-67.82 Y337.24\n")
        self._send_cmd1("G0 X-67.97 Y337.09\n")
        self._send_cmd1("G0 X-68.29 Y336.93\n")
        self._send_cmd1("G0 Z5\n")
        self._send_cmd1("G0 X-68.92 Y337.09\n")
        self._send_cmd1("G0 Z0\n")
        self._send_cmd1("G0 X-68.60 Y336.93\n")
        self._send_cmd1("G0 X-68.13 Y336.93\n")
        self._send_cmd1("G0 X-67.66 Y337.09\n")
        self._send_cmd1("G0 X-67.34 Y337.24\n")
        self._send_cmd1("G0 X-66.87 Y337.72\n")
        self._send_cmd1("G0 Z5\n")
        self._send_cmd1("G0 X-66.61 Y339.14\n")
        self._send_cmd1("G0 Z0\n")
        self._send_cmd1("G0 X-66.61 Y338.98\n")
        self._send_cmd1("G0 X-66.45 Y338.98\n")
        self._send_cmd1("G0 X-66.45 Y339.14\n")
        self._send_cmd1("G0 X-66.61 Y339.14\n")
        self._send_cmd1("G0 Z5\n")
        self._send_cmd1("G0 X-67.08 Y337.72\n")
        self._send_cmd1("G0 Z0\n")
        self._send_cmd1("G0 X-66.77 Y338.35\n")
        self._send_cmd1("G0 X-67.08 Y337.40\n")
        self._send_cmd1("G0 X-67.08 Y337.09\n")
        self._send_cmd1("G0 X-66.92 Y336.93\n")
        self._send_cmd1("G0 X-66.77 Y336.93\n")
        self._send_cmd1("G0 X-66.45 Y337.09\n")
        self._send_cmd1("G0 X-66.29 Y337.24\n")
        self._send_cmd1("G0 X-65.98 Y337.72\n")
        self._send_cmd1("G0 Z5\n")
        self._send_cmd1("G0 X-65.81 Y337.72\n")
        self._send_cmd1("G0 Z0\n")
        self._send_cmd1("G0 X-65.50 Y338.19\n")
        self._send_cmd1("G0 X-65.18 Y338.35\n")
        self._send_cmd1("G0 X-65.02 Y338.19\n")
        self._send_cmd1("G0 X-65.02 Y338.03\n")
        self._send_cmd1("G0 X-65.18 Y337.40\n")
        self._send_cmd1("G0 X-65.34 Y336.93\n")
        self._send_cmd1("G0 Z5\n")
        self._send_cmd1("G0 X-65.18 Y337.40\n")
        self._send_cmd1("G0 Z0\n")
        self._send_cmd1("G0 X-65.02 Y337.72\n")
        self._send_cmd1("G0 X-64.71 Y338.19\n")
        self._send_cmd1("G0 X-64.39 Y338.35\n")
        self._send_cmd1("G0 X-64.08 Y338.35\n")
        self._send_cmd1("G0 X-63.92 Y338.19\n")
        self._send_cmd1("G0 X-63.92 Y337.87\n")
        self._send_cmd1("G0 X-64.08 Y337.40\n")
        self._send_cmd1("G0 X-64.08 Y337.09\n")
        self._send_cmd1("G0 X-63.92 Y336.93\n")
        self._send_cmd1("G0 X-63.76 Y336.93\n")
        self._send_cmd1("G0 X-63.45 Y337.09\n")
        self._send_cmd1("G0 X-63.29 Y337.24\n")
        self._send_cmd1("G0 X-62.98 Y337.72\n")
        self._send_cmd1("G0 Z5\n")
        self._send_cmd1("G0 X-62.86 Y339.14\n")
        self._send_cmd1("G0 Z0\n")
        self._send_cmd1("G0 X-62.86 Y338.98\n")
        self._send_cmd1("G0 X-62.70 Y338.98\n")
        self._send_cmd1("G0 X-62.70 Y339.14\n")
        self._send_cmd1("G0 X-62.86 Y339.14\n")
        self._send_cmd1("G0 Z5\n")
        self._send_cmd1("G0 X-63.33 Y337.72\n")
        self._send_cmd1("G0 Z0\n")
        self._send_cmd1("G0 X-63.01 Y338.35\n")
        self._send_cmd1("G0 X-63.33 Y337.40\n")
        self._send_cmd1("G0 X-63.33 Y337.09\n")
        self._send_cmd1("G0 X-63.17 Y336.93\n")
        self._send_cmd1("G0 X-63.01 Y336.93\n")
        self._send_cmd1("G0 X-62.70 Y337.09\n")
        self._send_cmd1("G0 X-62.54 Y337.24\n")
        self._send_cmd1("G0 X-62.23 Y337.72\n")
        self._send_cmd1("G0 Z5\n")
        self._send_cmd1("G0 X-61.12 Y338.35\n")
        self._send_cmd1("G0 Z0\n")
        self._send_cmd1("G0 X-61.43 Y338.35\n")
        self._send_cmd1("G0 X-61.74 Y338.19\n")
        self._send_cmd1("G0 X-61.90 Y338.03\n")
        self._send_cmd1("G0 X-62.06 Y337.72\n")
        self._send_cmd1("G0 X-62.06 Y337.40\n")
        self._send_cmd1("G0 X-61.90 Y337.09\n")
        self._send_cmd1("G0 X-61.59 Y336.93\n")
        self._send_cmd1("G0 X-61.27 Y336.93\n")
        self._send_cmd1("G0 X-60.96 Y337.09\n")
        self._send_cmd1("G0 X-60.80 Y337.24\n")
        self._send_cmd1("G0 X-60.64 Y337.56\n")
        self._send_cmd1("G0 X-60.64 Y337.87\n")
        self._send_cmd1("G0 X-60.80 Y338.19\n")
        self._send_cmd1("G0 X-61.12 Y338.35\n")
        self._send_cmd1("G0 X-61.27 Y338.19\n")
        self._send_cmd1("G0 X-61.27 Y337.87\n")
        self._send_cmd1("G0 X-61.12 Y337.56\n")
        self._send_cmd1("G0 X-60.80 Y337.40\n")
        self._send_cmd1("G0 X-60.33 Y337.40\n")
        self._send_cmd1("G0 X-60.01 Y337.56\n")
        self._send_cmd1("G0 X-59.86 Y337.72\n")
        self._send_cmd1("G0 Z5\n")
        self._send_cmd1("G0 X-60.01 Y337.72\n")
        self._send_cmd1("G0 Z0\n")
        self._send_cmd1("G0 X-59.70 Y338.19\n")
        self._send_cmd1("G0 X-59.38 Y338.35\n")
        self._send_cmd1("G0 X-59.23 Y338.19\n")
        self._send_cmd1("G0 X-59.23 Y338.03\n")
        self._send_cmd1("G0 X-59.38 Y337.40\n")
        self._send_cmd1("G0 X-59.54 Y336.93\n")
        self._send_cmd1("G0 Z5\n")
        self._send_cmd1("G0 X-59.38 Y337.40\n")
        self._send_cmd1("G0 Z0\n")
        self._send_cmd1("G0 X-59.23 Y337.72\n")
        self._send_cmd1("G0 X-58.91 Y338.19\n")
        self._send_cmd1("G0 X-58.60 Y338.35\n")
        self._send_cmd1("G0 X-58.28 Y338.35\n")
        self._send_cmd1("G0 X-58.12 Y338.19\n")
        self._send_cmd1("G0 X-58.12 Y337.87\n")
        self._send_cmd1("G0 X-58.28 Y337.40\n")
        self._send_cmd1("G0 X-58.28 Y337.09\n")
        self._send_cmd1("G0 X-58.12 Y336.93\n")
        self._send_cmd1("G0 X-57.97 Y336.93\n")
        self._send_cmd1("G0 X-57.65 Y337.09\n")
        self._send_cmd1("G0 X-57.49 Y337.24\n")
        self._send_cmd1("G0 X-57.18 Y337.72\n")
        self._send_cmd1("G0 Z5\n")
        self._send_cmd1("G0 X-54.76 Y338.35\n")
        self._send_cmd1("G0 Z0\n")
        self._send_cmd1("G0 X-55.07 Y338.35\n")
        self._send_cmd1("G0 X-55.39 Y338.19\n")
        self._send_cmd1("G0 X-55.55 Y338.03\n")
        self._send_cmd1("G0 X-55.71 Y337.72\n")
        self._send_cmd1("G0 X-55.71 Y337.40\n")
        self._send_cmd1("G0 X-55.55 Y337.09\n")
        self._send_cmd1("G0 X-55.23 Y336.93\n")
        self._send_cmd1("G0 X-54.92 Y336.93\n")
        self._send_cmd1("G0 X-54.60 Y337.09\n")
        self._send_cmd1("G0 X-54.44 Y337.24\n")
        self._send_cmd1("G0 X-54.29 Y337.56\n")
        self._send_cmd1("G0 X-54.29 Y337.87\n")
        self._send_cmd1("G0 X-54.44 Y338.19\n")
        self._send_cmd1("G0 X-54.76 Y338.35\n")
        self._send_cmd1("G0 X-54.92 Y338.19\n")
        self._send_cmd1("G0 X-54.92 Y337.87\n")
        self._send_cmd1("G0 X-54.76 Y337.56\n")
        self._send_cmd1("G0 X-54.44 Y337.40\n")
        self._send_cmd1("G0 X-53.97 Y337.40\n")
        self._send_cmd1("G0 X-53.66 Y337.56\n")
        self._send_cmd1("G0 X-53.50 Y337.72\n")
        self._send_cmd1("G0 Z5\n")
        self._send_cmd1("G0 X-53.66 Y337.72\n")
        self._send_cmd1("G0 Z0\n")
        self._send_cmd1("G0 X-53.03 Y338.50\n")
        self._send_cmd1("G0 X-52.72 Y338.98\n")
        self._send_cmd1("G0 X-52.56 Y339.29\n")
        self._send_cmd1("G0 X-52.40 Y339.76\n")
        self._send_cmd1("G0 X-52.40 Y340.08\n")
        self._send_cmd1("G0 X-52.56 Y340.24\n")
        self._send_cmd1("G0 X-52.88 Y340.08\n")
        self._send_cmd1("G0 X-53.03 Y339.76\n")
        self._send_cmd1("G0 X-53.35 Y338.50\n")
        self._send_cmd1("G0 X-53.82 Y337.09\n")
        self._send_cmd1("G0 X-54.29 Y335.98\n")
        self._send_cmd1("G0 X-54.45 Y335.51\n")
        self._send_cmd1("G0 X-54.45 Y335.20\n")
        self._send_cmd1("G0 X-54.29 Y335.04\n")
        self._send_cmd1("G0 X-53.98 Y335.20\n")
        self._send_cmd1("G0 X-53.82 Y335.67\n")
        self._send_cmd1("G0 X-53.66 Y337.09\n")
        self._send_cmd1("G0 X-53.51 Y336.93\n")
        self._send_cmd1("G0 X-53.19 Y336.93\n")
        self._send_cmd1("G0 X-52.88 Y337.09\n")
        self._send_cmd1("G0 X-52.72 Y337.24\n")
        self._send_cmd1("G0 X-52.40 Y337.72\n")
        self._send_cmd1("G0 Z5\n")
        self._send_cmd1("G0 X-50.46 Y337.72\n")
        self._send_cmd1("G0 Z0\n")
        self._send_cmd1("G0 X-50.14 Y338.19\n")
        self._send_cmd1("G0 X-49.83 Y338.82\n")
        self._send_cmd1("G0 Z5\n")
        self._send_cmd1("G0 X-49.36 Y340.24\n")
        self._send_cmd1("G0 Z0\n")
        self._send_cmd1("G0 X-50.30 Y337.40\n")
        self._send_cmd1("G0 X-50.30 Y337.09\n")
        self._send_cmd1("G0 X-50.14 Y336.93\n")
        self._send_cmd1("G0 X-49.83 Y336.93\n")
        self._send_cmd1("G0 X-49.52 Y337.09\n")
        self._send_cmd1("G0 X-49.36 Y337.24\n")
        self._send_cmd1("G0 X-49.04 Y337.72\n")
        self._send_cmd1("G0 Z5\n")
        self._send_cmd1("G0 X-50.30 Y338.98\n")
        self._send_cmd1("G0 Z0\n")
        self._send_cmd1("G0 X-49.20 Y338.98\n")
        self._send_cmd1("G0 Z5\n")
        self._send_cmd1("G0 X-48.96 Y337.72\n")
        self._send_cmd1("G0 Z0\n")
        self._send_cmd1("G0 X-48.65 Y338.19\n")
        self._send_cmd1("G0 X-48.18 Y338.98\n")
        self._send_cmd1("G0 X-48.02 Y339.29\n")
        self._send_cmd1("G0 X-47.86 Y339.76\n")
        self._send_cmd1("G0 X-47.86 Y340.08\n")
        self._send_cmd1("G0 X-48.02 Y340.24\n")
        self._send_cmd1("G0 X-48.33 Y340.08\n")
        self._send_cmd1("G0 X-48.49 Y339.76\n")
        self._send_cmd1("G0 X-48.65 Y339.14\n")
        self._send_cmd1("G0 X-48.81 Y338.19\n")
        self._send_cmd1("G0 X-48.96 Y336.93\n")
        self._send_cmd1("G0 X-48.81 Y337.40\n")
        self._send_cmd1("G0 X-48.65 Y337.72\n")
        self._send_cmd1("G0 X-48.33 Y338.19\n")
        self._send_cmd1("G0 X-48.02 Y338.35\n")
        self._send_cmd1("G0 X-47.70 Y338.35\n")
        self._send_cmd1("G0 X-47.55 Y338.19\n")
        self._send_cmd1("G0 X-47.55 Y337.87\n")
        self._send_cmd1("G0 X-47.70 Y337.40\n")
        self._send_cmd1("G0 X-47.70 Y337.09\n")
        self._send_cmd1("G0 X-47.55 Y336.93\n")
        self._send_cmd1("G0 X-47.39 Y336.93\n")
        self._send_cmd1("G0 X-47.07 Y337.09\n")
        self._send_cmd1("G0 X-46.92 Y337.24\n")
        self._send_cmd1("G0 X-46.60 Y337.72\n")
        self._send_cmd1("G0 Z5\n")
        self._send_cmd1("G0 X-46.65 Y337.24\n")
        self._send_cmd1("G0 Z0\n")
        self._send_cmd1("G0 X-46.34 Y337.40\n")
        self._send_cmd1("G0 X-46.18 Y337.56\n")
        self._send_cmd1("G0 X-46.02 Y337.87\n")
        self._send_cmd1("G0 X-46.02 Y338.19\n")
        self._send_cmd1("G0 X-46.18 Y338.35\n")
        self._send_cmd1("G0 X-46.34 Y338.35\n")
        self._send_cmd1("G0 X-46.65 Y338.19\n")
        self._send_cmd1("G0 X-46.81 Y337.87\n")
        self._send_cmd1("G0 X-46.81 Y337.40\n")
        self._send_cmd1("G0 X-46.65 Y337.09\n")
        self._send_cmd1("G0 X-46.34 Y336.93\n")
        self._send_cmd1("G0 X-46.02 Y336.93\n")
        self._send_cmd1("G0 X-45.71 Y337.09\n")
        self._send_cmd1("G0 X-45.55 Y337.24\n")
        self._send_cmd1("G0 X-45.24 Y337.72\n")
        self._send_cmd1("G0 Z5\n")
        self._send_cmd1("G0 X-43.39 Y337.72\n")
        self._send_cmd1("G0 Z0\n")
        self._send_cmd1("G0 X-42.75 Y338.50\n")
        self._send_cmd1("G0 X-42.44 Y338.98\n")
        self._send_cmd1("G0 X-42.28 Y339.29\n")
        self._send_cmd1("G0 X-42.12 Y339.76\n")
        self._send_cmd1("G0 X-42.12 Y340.08\n")
        self._send_cmd1("G0 X-42.28 Y340.24\n")
        self._send_cmd1("G0 X-42.60 Y340.08\n")
        self._send_cmd1("G0 X-42.75 Y339.76\n")

        self._send_cmd1("G0 Z80\n")
        self._send_cmd1("G0 X0 Y190\n")
        
    def disconnect1(self):
        self.ser1.disconnect()    

    def read_Gcode1(self):
        #This is a personal test.
        #path = "resource/Dexarm/gcode/hourse.gcode"
        #self.ser1.write(path.encode())
        self.ser1.writeFile('test1.gcode')
        #self._send_cmd1("path\r")    

    def set_workorigin1(self):
        """
        Set the current position as the new work origin.
        """
        self._send_cmd1("G92 X0 Y0 Z0 E0\r")

    def set_acceleration1(self, acceleration, travel_acceleration, retract_acceleration=60):
        """
        Set the preferred starting acceleration for moves of different types.

        Args:
            acceleration (int): printing acceleration. Used for moves that employ the current tool.
            travel_acceleration (int): used for moves that include no extrusion.
            retract_acceleration (int): used for extruder retraction moves.
        """
        cmd = "M204"+"P" + str(acceleration) + "T"+str(travel_acceleration) + "R" + str(retract_acceleration) + "\r\n"
        self._send_cmd1(cmd)

    def set_module_type1(self, module_type):
        """
        Set the type of end effector.

        Args:
            module_type (int):
                0 for Pen holder module
                1 for Laser engraving module
                2 for Pneumatic module
                3 for 3D printing module
        """
        self._send_cmd1("M888 P" + str(module_type) + "\r")

    def get_module_type1(self):
        """
        Get the type of end effector.

        Returns:
            string that indicates the type of the module
        """
        self.ser1.reset()
        self.ser1.write('M888\r'.encode())
        while True:
            serial_str = self.ser1.readString().decode("utf-8")
            #serial_str = self.ser1.readLine()
            if len(serial_str) > 0:
                if serial_str.find("PEN") > -1:
                    module_type = 'PEN'
                if serial_str.find("LASER") > -1:
                    module_type = 'LASER'
                if serial_str.find("PUMP") > -1:
                    module_type = 'PUMP'
                if serial_str.find("3D") > -1:
                    module_type = '3D'
            if len(serial_str) > 0:
                if serial_str.find("ok") > -1:
                    return module_type

    def move_to1(self, x=None, y=None, z=None, e=None, feedrate=2000, mode="G1", wait=True):
        """
        Move to a cartesian position. This will add a linear move to the queue to be performed after all previous moves are completed.

        Args:
            mode (string, G0 or G1): G1 by default. use G0 for fast mode
            x, y, z (int): The position, in millimeters by default. Units may be set to inches by G20. Note that the center of y axis is 300mm.
            feedrate (int): set the feedrate for all subsequent moves
        """
        print('move_to1', x, y, z, e, feedrate, mode, wait)
        cmd = mode + "F" + str(feedrate)
        if x is not None:
            cmd = cmd + "X"+str(round(x))
        if y is not None:
            cmd = cmd + "Y" + str(round(y))
        if z is not None:
            cmd = cmd + "Z" + str(round(z))
        if e is not None:
            cmd = cmd + "E" + str(round(e))
        cmd = cmd + "\r\n"
        self._send_cmd1(cmd, wait=wait)

    def fast_move_to1(self, x=None, y=None, z=None, feedrate=2000, wait=True):
        """
        Fast move to a cartesian position, i.e., in mode G0

        Args:
            x, y, z (int): the position, in millimeters by default. Units may be set to inches by G20. Note that the center of y axis is 300mm.
            feedrate (int): sets the feedrate for all subsequent moves
        """
        self.move_to1(self, x=x, y=y, z=z, feedrate=feedrate, mode="G0", wait=wait)

    def get_current_position1(self):
        """
        Get the current position
        
        Returns:
            position x,y,z, extrusion e, and dexarm theta a,b,c
        """
        self.ser1.reset()
        self.ser1.write('M114\r'.encode())
        x, y, z, e, a, b, c = None, None, None, None, None, None, None
        while True:
            serial_str = self.ser1.readString().decode("utf-8")
            #serial_str = self.ser1.readLine()
            if len(serial_str) > 0:
                if serial_str.find("X:") > -1:
                    temp = re.findall(r"[-+]?\d*\.\d+|\d+", serial_str)
                    x = float(temp[0])
                    y = float(temp[1])
                    z = float(temp[2])
                    e = float(temp[3])
            if len(serial_str) > 0:
                if serial_str.find("DEXARM Theta") > -1:
                    temp = re.findall(r"[-+]?\d*\.\d+|\d+", serial_str)
                    a = float(temp[0])
                    b = float(temp[1])
                    c = float(temp[2])
            if len(serial_str) > 0:
                if serial_str.find("ok") > -1:
                    return x, y, z, e, a, b, c

    def delay_ms1(self, value):
        """
        Pauses the command queue and waits for a period of time in ms

        Args:
            value (int): time in ms
        """
        self._send_cmd1("G4 P" + str(value) + '\r')

    def delay_s1(self, value):
        """
        Pauses the command queue and waits for a period of time in s

        Args:
            value (int): time in s
        """
        self._send_cmd1("G4 S" + str(value) + '\r')

    def rotate_wrist1(self, value):
        #This is a personal test.
        """
        Setting the rotation of wrist in way or the other

        Args:
            value (int): degrees of rotation
        """
        self._send_cmd1("M1114" + str(value) + '\r')    

    def soft_gripper_pick1(self):
        """
        Close the soft gripper
        """
        self._send_cmd1("M1001\r")

    def soft_gripper_place1(self):
        """
        Wide-open the soft gripper
        """
        self._send_cmd1("M1000\r")

    def soft_gripper_nature1(self):
        """
        Release the soft gripper to nature state
        """
        self._send_cmd1("M1002\r")

    def soft_gripper_stop1(self):
        """
        Stop the soft gripper
        """
        self._send_cmd1("M1003\r")

    def air_picker_pick1(self):
        """
        Pickup an object
        """
        self._send_cmd1("M1000\r")

    def air_picker_place1(self):
        """
        Release an object
        """
        self._send_cmd1("M1001\r")

    def air_picker_nature1(self):
        """
        Release to nature state
        """
        self._send_cmd1("M1002\r")

    def air_picker_stop1(self):
        """
        Stop the picker
        """
        self._send_cmd1("M1003\r")

    def laser_on1(self, value=0):
        """
        Turn on the laser

        Args:
            value (int): set the power, range form 1 to 255
        """
        self._send_cmd1("M3 S" + str(value) + '\r')

    def laser_off1(self):
        """
        Turn off the laser
        """
        self._send_cmd1("M5\r")

    """Conveyor Belt"""
    def conveyor_belt_forward1(self, speed=0):
        """
        Move the belt forward
        """
        self._send_cmd1("M2012 F" + str(speed) + 'D0\r')

    def conveyor_belt_backward1(self, speed=0):
        """
        Move the belt backward
        """
        self._send_cmd1("M2012 F" + str(speed) + 'D1\r')

    def conveyor_belt_stop1(self, speed=0):
        """
        Stop the belt
        """
        self._send_cmd1("M2013\r")

    """Sliding Rail"""
    def sliding_rail_init1(self):
        """
        Sliding rail init.
        """
        self._send_cmd1("M2005\r")

    def close1(self):
        """
        Release the serial port.
        """
        self.ser1.close()

print('Dexarm class loaded')


python.execfile('example.py')
