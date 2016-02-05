#!/usr/bin/python3

def main():
	"""Simple fibonacci series"""
	a, b = 0, 1
	while b < 56:
		print(b)
		a, b = b, a + b
	print()

if __name__ == "__main__":
	main()