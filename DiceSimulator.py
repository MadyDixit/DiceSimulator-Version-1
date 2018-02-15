import random
import time

def  cast():
	input("Press any key for cast the dice!")
	r = list(range(1, 7))
	print("Result :" + str(random.choice(r)))

while True:
	time.sleep(1)
	cast()