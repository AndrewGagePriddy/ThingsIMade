import FibonacciGenerator
import time
import vgamepad as vg
import keyboard
import os
import ControllerKeysScript
import ClockStuff

os.system('cls')


txtFile = r"TextFile\ReadThis.txt"

def FirstLoop():
	print("Hold = to begin controller setup")
	print("Hold , to reset")
	print("Hold ESC to end")
	print("Hold . to change speed")
	AutoReadTxt()

def StartScreen():
	
	print(f"Press ~ to begin reading: ReadThis.txt")
	keyboard.wait('~')
	
	FirstLoop()
	
	
	
	
def AutoReadTxt():
	c = .2
	place = 0
	f = open(txtFile,"r")	
	a = f.read()
	ClockStuff.WaitTimer(3)
	
	
	
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
		
		if place < 10: place = 10
		print(f"Extending sequence to: {place}")
		
		#create more text if the code runs out
		FibonacciGenerator.Fib(place)
		#
		
		AutoReadTxt()
	f.close()	

StartScreen()


