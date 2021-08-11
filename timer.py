#import module

import time

#define countdown

def countdown(t):
	while t :
		min, secs = = divmod(t, 60)
		timer = '{:02d}:{02d}'.form
		print(timer, end="\r")
		time.sleep(1)
		t -= 1

	print('FIYAAAA')

#input time in sec

t = input("Enter the time in secs:")

#functions
countdown(int(t))

