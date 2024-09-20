import time

def WaitTimer(t):
	while t:
		time.sleep(1)
		print(f"Starting in : {t}", end ="\r")
		t -= 1
	else:
		print("                                ",end ="\r")