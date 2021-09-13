###################################################
# Basic script for coordinating 2 dexarms with MRL

# for virtual testing
runtime.setVirtual(False)

# variables
dexarmPort1 = 'COM3'
dexarmPort2 = 'COM4'

# joystick map
joy_test1 = "Num 1"
joy_go_home = "Num 2"
joy_move_to = "Num 3" # "Num 3"
joy_disconnect = "Num 5"
joy_set_work_origin = "Num 8"
joy_exec_file = "Num 9"
joy_down_dexarm2 = "Down"
joy_up_dexarm2 = "Up"

# start 2 dexarms
dexarm1 = Dexarm('serial1', dexarmPort1)
dexarm2 = Dexarm('serial2', dexarmPort2)

# start the services
python = Runtime.start("python","Python")
joy = Runtime.start("joy","Joystick")
swing = Runtime.start("swing","SwingGui")

#this set which kind of controller you want to poll data from
#it is the number you can see in the Joystick GUI when you open the list of devices
joy.setController(0)

#tell joystick service to send data to python as a message only when new data is aviable
joy.addInputListener(python)

#this is the method in python which receive the data from joystick service
#it is triggered only when new data arrive, it's not a loop !
def onJoystickInput(data):
 #this print the name of the key/button you pressed (it's a String)
 #this print the value of the key/button (it's a Float)
 print (data)
 if (data.id == joy_move_to):
     if (data.value == 1):
        print(joy_move_to, "was pressed its value is", data.value)
        dexarm1.move_to1(50, 300, 0)
        #dexarm1.read_Gcode1()
        print('moved dexarm1 to 50, 300, 0')
        #print('moved dexarm1 to test1.gcode')
 elif (data.id == joy_exec_file):
     if (data.value == 1):
         print("executing script example.py", data.value)
         execfile(RuningFolder+'/Dexarm/scripts/example.py')
 elif (data.id == joy_test1):
     if (data.value == 1):
         print("reading test1.gcode", data.value)
         dexarm2.move_to1(0, 220, 50)
         dexarm1.set_module_type1(0)
         dexarm1.read_Gcode1()
 elif (data.id == joy_go_home):
     if (data.value == 1):
         print("Go home", data.value)
         dexarm1.go_home1()
         dexarm2.go_home1()
 elif (data.id == joy_disconnect):
     if (data.value == 1):
         print("Disconnect", data.value)
         dexarm1.disconnect1()
         dexarm2.disconnect1()
 elif (data.id == joy_set_work_origin):
     if (data.value == 1):
         print(joy_set_work_origin, "Work origin is set", data.value)    
         dexarm1.set_workorigin1()
 elif (data.id == joy_down_dexarm2):
    if (data.value == 1):
        print("Moving down dexarm2", data.value)
        dexarm2.set_relativeDown1()
 elif (data.id == joy_up_dexarm2):
    if (data.value == 1):
        print("Moving up dexarm2", data.value)
        dexarm2.set_relativeUp1()

'''
 elif (data.id == "Down"):
    if (data.value == 1):
        print("Moving down dexarm1", data.value)
        dexarm1.set_relativeDown1()
 elif (data.id == "Up"):
    if (data.value == 1):
        print("Moving up dexarm1", data.value)
        dexarm1.set_relativeUp1()        
'''
print('example script loaded')
