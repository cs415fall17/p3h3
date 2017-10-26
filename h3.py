def hgcd(a, b):
	a = abs(a)
	b = abs(b)
	print('(', a, ',', b, ')')
	# base case
	if b == 0:
		return a
	elif bothAreEven(a, b):

		x = 2 * hgcd( a // 2, b // 2 )
		return x

	elif (not isEven(a)) and isEven(b):
		x = hgcd( a, b // 2 )
		return x
	elif bothAreOdd(a, b) and (a - b) // 2 == a:
		x = hgcd(b, a % b)
		return x
	elif bothAreOdd(a, b):
		# |1 - 3| // 2 == 1
		x = hgcd( (a - b) // 2, b )
		return x
	# extra part to prevent infinite call stack when a is even and b is odd
	else:
		x = hgcd(b, a % b)
		return x

def isEven(a):
	if a % 2 == 0:
		return True
	else:
		return False

def bothAreEven(a, b):
	if isEven(a) and isEven(b):

		return True
	else:
		return False 

def bothAreOdd(a, b):
	if (not isEven(a)) and (not isEven(b)):
		return True
	else:
		return False

def gcd(a, b):
	#print('(', a, ',', b, ')')

	if b == 0:
		return a
	return gcd(b, a % b)

#hgcd(25, 24)

#print()
#gcd(25, 24)

#print("h")

#hgcd(21, 25)
#print()
#gcd(21, 25)
print(hgcd(5, 3))
print(gcd(5, 3))
'''
for i in range(100):
	for j in range(i):
		print(i, j)
		print(hgcd(i, j))
		print(gcd(i, j))
		print()
'''