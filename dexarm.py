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
        self.name = name
        self.stopped = False
        self.ser1 = Runtime.start(name,"Serial")
        self.ser1.connect(port, 115200, 8, 1, 0)
        self.is_open = self.ser1.isConnected()
        if self.is_open:
            print('pydexarm: %s connected' % self.ser1.name)
        else:
            print('failed to connect to serial port')

    def stop(self):
        print('dexarm', self.name, 'stopping')
        self.stopped = True


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

    #path = "test1.gcode"
    def send_gcode1(self, wait=True):
        ####This is a personal test.
        self.ser1.writeFile('myOpinion.gcode')
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

    #def removeComment(string):
        #if (string.find(';')==-1):
            #return string
        #else:
            #return string[:string.index(';')]

    def strip_gcode1(self):
        g = open('myOpinion.gcode','r')
        print("opened gcode")
        for line in g:
            #l = removeComment(line)
            #l = l.strip() # Strip all EOL characters for streaming
            #print("striping gcode")
            if  (line.isspace()==False and len(line)>0) :
                self._send_cmd1(line+'\n') # Send g-code block
                print 'Sending: ' + line

    def process_letter(self, letter):
        print('opening letter ' + letter)
        f = open(letter,'r')
        for line in f and not self.stopped:
            if  (line.isspace()==False and len(line)>0) :
                self._send_cmd1(line+'\n')
                print ('Dexarm1 gcode line: ' + line)

    def pickAndPlace1(self):
        h = open('pickAndPlace1.gcode','r')
        print("opened gcode")
        for line in h:
            if  (line.isspace()==False and len(line)>0) :
                self._send_cmd1(line+'\n') # Send g-code block
                print 'Dexarm2 gcode line: ' + line

    def pickAndPlace2(self):
        j = open('pickAndPlace2.gcode','r')
        print("opened gcode")
        for line in j:
            if  (line.isspace()==False and len(line)>0) :
                self._send_cmd1(line+'\n') # Send g-code block
                print 'Dexarm2 gcode line: ' + line

    def pickPlace1(self):
        k = open('pickPlace1.gcode','r')
        print("opened gcode")
        for line in k:
            if  (line.isspace()==False and len(line)>0) :
                self._send_cmd1(line+'\n') # Send g-code block
                print 'Dexarm2 gcode line: ' + line 

    def pickPlace2(self):
        m = open('pickPlace2.gcode','r')
        print("opened gcode")
        for line in m:
            if  (line.isspace()==False and len(line)>0) :
                self._send_cmd1(line+'\n') # Send g-code block
                print 'Dexarm2 gcode line: ' + line            

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
        self._send_cmd1("G0 X0 Y0 Z-3\n")
        self._send_cmd1("G90\r")

    def set_relativeUp1(self):
        #This is a personal test.
        self._send_cmd1("G91\r")
        self._send_cmd1("G0 X0 Y0 Z3\n")
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
    
    def disconnect1(self):
        #This is a personal test.
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
        self._send_cmd1("G92 X0 Y300 Z0\r")

    def move_to_workorigin1(self):
        """
        Move to the current work position.
        """
        self._send_cmd1("G0 X0 Y300 Z0\r")    

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

    #def fast_move_to1(self, x=None, y=None, z=None, feedrate=2000, wait=True):
        """
        Fast move to a cartesian position, i.e., in mode G0

        Args:
            x, y, z (int): the position, in millimeters by default. Units may be set to inches by G20. Note that the center of y axis is 300mm.
            feedrate (int): sets the feedrate for all subsequent moves
        """
        #self.move_to1(self, x=x, y=y, z=z, feedrate=feedrate, mode="G0", wait=wait)

    def fast_move_to1(self, x, y, z, feedrate=6000, wait=True):
        cmd = "G0"+"F" + str(feedrate) + "X"+str(x) + "Y" + str(y) + "Z" + str(z) + "\r\n"
        self._send_cmd1(cmd, wait=wait)    

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

    def air_picker_rotate1(self, radius=0):
        """
        Setting the rotation of wrist in way or the other

        Args:
            value (int): degrees of rotation
        """
        self._send_cmd1("M2100"'\r')
        self._send_cmd1("M2101 P" + str(radius) + '\r')    

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

    def disconnect1(self):
        """
        Release the serial port.
        """
        self.ser1.clear()    

def action2():
    letters = ['letter1.gcode','letter2.gcode','letter3.gcode']
    for letter in letters:
        # We move dexarm1 away
        dexarm1.fast_move_to1(140, 160, 80)
        print "moved dexarm1"
        # We start dexarm2 to set the paper
        ##dexarm2.pickAndPlace1()  ##gcode
        
        dexarm2.delay_s1(2)
        #dexarm2.set_module_type2(6)
        dexarm2.fast_move_to1(220, 320, 100)
        dexarm2.fast_move_to1(220, 320, 0)
        dexarm2.air_picker_pick1()
        dexarm2.fast_move_to1(220, 320, 100)
        dexarm2.delay_s1(1)
        dexarm2.air_picker_rotate1(-35)
        
        dexarm2.fast_move_to1(0, 320, 100)
        dexarm2.fast_move_to1(0, 320, 0)
        dexarm2.air_picker_place1()
        dexarm2.air_picker_natur1()
        dexarm2.delay_s1(2)

        dexarm2.fast_move_to1(0, 320, 100)
        dexarm2.delay_s1(1)
        dexarm2.air_picker_rotate1(35)

        dexarm2.fast_move_to1(140, 160, 100)
        print "dexarm2 picked and placed paper"

        dexarm1.delay_s1(7)
        # We start dexarm1 to write on paper
        dexarm1.process_letter(letter)  ##gcode

        # gcode move dexarm1 away
        #dexarm1.move_to1(140, 180, 50)

        # We start dexarm2 to remove the written paper
        #sleep(5) #needs to wait until the end of previous gcode
        dexarm2.pickAndPlace2() ##gcode
        #dexarm2.delay_s1(5)
        #dexarm2.fast_move_to1(0, 320, 100)
        #dexarm2.fast_move_to1(0, 320, 0)
        #dexarm2.air_picker_pick1()
        #dexarm2.fast_move_to1(0, 320, 100)

        #dexarm2.delay_s1(1)
        #dexarm2.air_picker_rotate1(-35)

        #dexarm2.fast_move_to1(-225, 315, 100)
        #dexarm2.fast_move_to1(-225, 315, 0)
        #dexarm2.air_picker_place1()
        #dexarm2.air_picker_nature1()
        #dexarm2.delay_s1(2)
        
        #dexarm2.fast_move_to1(-225, 315, 100)

        #dexarm2.delay_s1(1)
        #dexarm2.air_picker_rotate1(35)

        #dexarm2.fast_move_to1(140, 160, 100)
        print ("dexarm2 removed paper")

def action1():
    letters = ['letter1.gcode','letter2.gcode','letter3.gcode','letter4.gcode','letter5.gcode','letter6.gcode','letter7.gcode']
    for letter in letters:
        # We move dexarm1 away
        dexarm2.delay_s1(1)
        dexarm1.fast_move_to1(100, 218, 36)
        print ("dexarm1 moved to rotate paper")

        # We start dexarm2 to set the paper
        dexarm2.pickPlace1()  ##gcode
        print ("dexarm2 picked and placed paper")

        # We start dexarm1 to write on paper
        dexarm1.delay_s1(5)
        #dexarm1.fast_move_to1(160, 150, 100)
        dexarm1.process_letter(letter)  ##gcode

        dexarm2.delay_s1(2)
        # We start dexarm2 to remove the written paper
        dexarm2.pickPlace2() ##gcode
        print ("dexarm2 removed paper")


print('Dexarm class loaded')


python.execFile('joystick.py')