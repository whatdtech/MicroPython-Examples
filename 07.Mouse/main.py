# main.py -- put your code here!
import pyb

switch = pyb.Switch()
accel = pyb.Accel()

while True:
	pyb.hid((switch(), accel.x(), -accel.y(), accel.z()))
	pyb.delay(20)
