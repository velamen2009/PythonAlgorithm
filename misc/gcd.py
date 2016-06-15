"""
Greatest common divisor
"""

def gcd1(x, y):
	return x if y == 0 else gcd1(y, x%y)

def gcd2(x, y):
	while x > 0:
		if x < y:
			x, y = y, x
		x = x - y
	return y

def gcd3(x, y):
	while 0 != y:
		x, y = y, x%y
	return x

if __name__ == '__main__':
	import sys
	print(gcd1(int(sys.argv[1]), int(sys.argv[2])))
	print(gcd2(int(sys.argv[1]), int(sys.argv[2])))
	print(gcd3(int(sys.argv[1]), int(sys.argv[2])))
