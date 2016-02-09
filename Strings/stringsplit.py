#!/usr/bin/python3

def main():
	# Split works using whitespace
	s = "going down Anfield road!"
	n = s.split()
	print(n)
	for w in n:
		print(w)
	# Joining strings
	# Joing with colon between
	print(':'.join(n))
	# Joining with spacing
	print(' '.join(n))

if __name__ == "__main__":
	main()