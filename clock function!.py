import time

def clock(mode=None, h=time.localtime(time.time())[3], m=time.localtime(time.time())[4]):
	if (mode != 'm' and mode) or (h not in range(24)) or (m not in range(60)): return "Invalid entry"
	
	for i in range((h%12)*5): print(" ", end="") #i want println back >:(
	print("v", end="")
	
	if mode == 'm': print(h)
	elif h == 0: print(h+12)
	else: print(h%12)
	
	for i in range(11): print("+" + "-" * 4, end="")
	print("+" + "-" * 4)
	
	for i in range(m): print(" ", end="")
	print("^", end="")
	print(m)
	
	print("It is ", end="")
	if mode == 'm': print(h, end="")
	elif h == 0: print(h+12, end="")
	else: print(h%12, end="")
	print(":", end="") #ughhghgh
	if (m < 10): print("0", end="")
	print(m, end="")
	if mode == 'm':	print()
	elif h >= 12: print("pm")
	else: print("am")