"""
Greatest common multiple
"""

def gcm1(x, y):
	m = x * y
	while x > 0:
		if x < y:
			x, y = y, x
		x = x - y
	return m/y

def gcm2(x, y):
	m = x * y
	while 0 != y:
		x, y = y, x%y
	return m/x

if __name__ == '__main__':
	import sys
	print(gcm1(int(sys.argv[1]), int(sys.argv[2]))) 
	print(gcm2(int(sys.argv[1]), int(sys.argv[2]))) 
