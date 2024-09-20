import time
import vgamepad as vg
import ClockStuff

gamepad = vg.VX360Gamepad()

buttonA = vg.XUSB_BUTTON.XUSB_GAMEPAD_A
buttonB = vg.XUSB_BUTTON.XUSB_GAMEPAD_B
buttonX = vg.XUSB_BUTTON.XUSB_GAMEPAD_X
buttonY = vg.XUSB_BUTTON.XUSB_GAMEPAD_Y
buttonSelect = vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK
buttonStart = vg.XUSB_BUTTON.XUSB_GAMEPAD_START
buttonLB = vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER
buttonRB = vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER
buttonL3 = vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB
buttonR3 = vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB
buttonGuide = vg.XUSB_BUTTON.XUSB_GAMEPAD_GUIDE

buttonDUP = vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP
buttonDLeft = vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT
buttonDRight = vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT
buttonDDown = vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN



def GetKeyPress(key):
	
	if key == 0:
		PressKey(buttonDUP)
		print("Up")
	elif key == 1:
		PressKey(buttonDDown)
		print("Down")
	elif key == 2:
		PressKey(buttonDLeft)
		print("Left")
	elif key == 3: 
		PressKey(buttonDRight)
		print("Right")
	elif key == 4: 
		PressKey(buttonA)
		print("A")
	elif key == 5: 
		PressKey(buttonB)
		print("B")
	elif key == 6: 
		#PressKey(buttonLB)
		print("LB")
	elif key == 7: 
		#PressKey(buttonRB)
		print("RB")
	elif key == 8: 
		PressKey(buttonSelect)
		print("Select")
	elif key == 9: 
		PressKey(buttonStart)
		print("Start")		


def PressKey(press):
		gamepad.press_button(press)
		gamepad.update()
		time.sleep(0.2)
		gamepad.release_button(press)
		gamepad.update()


def SetupController():
	print("Starting controller config in 5")
	ClockStuff.WaitTimer(5)
	count = 0
	
	for x in range(11):
		
		GetKeyPress(count)
		count = count + 1
		gamepad.reset()
		time.sleep(1)
		