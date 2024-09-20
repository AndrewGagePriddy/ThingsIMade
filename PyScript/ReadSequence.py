import Fibonacci
import time
import vgamepad as vg
import keyboard
import os
import ControllerKeysScript
import ClockStuff

os.system('cls')


txtFile = "FibonacciSequence.txt"



def StartScreen():
	
	print(f"Press ~ to begin reading: {txtFile}")
	
	keyboard.wait('~')
	AutoReadTxt()
	
	
def AutoReadTxt():
	c = .2
	place = 0
	f = open(txtFile,"r")	
	a = f.read()
	
	ClockStuff.WaitTimer(5)
	print("Hold = to begin controller setup")
	print("Hold , to reset")
	print("Hold ESC to end")
	print("Hold . to change speed")
	
	for x in a:
		time.sleep(c)
		ControllerKeysScript.GetKeyPress(int(a[place]))
		place = place + 1
		
		if keyboard.is_pressed('.'):
			c = float(input("Change speed to: "))
			ClockStuff.WaitTimer(3)
			
		if keyboard.is_pressed(','):
			print("Resetting...")
			place = 0
			
		if keyboard.is_pressed('='): ControllerKeysScript.SetupController()
		
		if keyboard.is_pressed('esc'): break
		
	else:
		print("writing new sequence")
		print(place)
		if place == 0: place = 10
		
		#create more text if the code runs out
		Fibonacci.Fib(place)
		#
		AutoReadTxt()
	f.close()	

StartScreen()


