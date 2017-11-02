#p5
	# w = 3

#p3
def hgcd(a, b):
	a = abs(a)
	b = abs(b)
	print("(",a, ",", b, ")")
	# base case
	# other persons
	if b == 0:
		return a
	if bothAreEven(a, b):

		return 2 * hgcd( a // 2, b // 2 )

	elif (not isEven(a)) and isEven(b):
		return hgcd( a, b // 2 )

	# extra part to prevent infinite call stack when a and b are odd and (a - b) // 2 == a
	elif bothAreOdd(a, b) and abs((a - b) // 2) == a:
		return hgcd(b, a % b)

	elif bothAreOdd(a, b):
		# |1 - 3| // 2 == 1
		return hgcd( abs((a - b) // 2), b )
	# extra part to prevent infinite call stack when a is even and b is odd
	else:
	
		return hgcd(b, a % b)

def hgcdv(a, b):
	a = abs(a)
	b = abs(b)
	print(a, ',', b)
	# base case
	if b == 0:
		return a
	elif bothAreEven(a, b):

		return 2 * hgcd( a // 2, b // 2 )

	elif (not isEven(a)) and isEven(b):
		return hgcd( a, b // 2 )

	elif bothAreOdd(a, b):
		# |1 - 3| // 2 == 1
		return hgcd( (a - b) // 2, b )

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
	print("(",a, ",", b, ")")

	if b == 0:
		return a
	return gcd(b, a % b)

def hgcdCheck(a, b):
	a = abs(a)
	b = abs(b)
	# base case
	if b == 0:
		return 1
	if bothAreEven(a, b):

		return (2 * hgcdCheck( a // 2, b // 2 ))//2 + 1

	elif (not isEven(a)) and isEven(b):
		return hgcdCheck( a, b // 2 ) + 1
	elif bothAreOdd(a, b) and abs((a - b) // 2) == a:
		return hgcdCheck(b, a % b) + 1
	elif bothAreOdd(a, b):
		# |1 - 3| // 2 == 1
		return hgcdCheck( abs((a - b) // 2), b ) + 1
	# extra part to prevent infinite call stack when a is even and b is odd
	else:
		return hgcdCheck(b, a % b) + 1
def gcdCheck(a, b):

	if b == 0:
		return 1
	return gcdCheck(b, a % b) + 1
#hgcd(25, 24)

#print()
#gcd(25, 24)

#print("h")

#hgcd(21, 25)
#print()
#gcd(21, 25)

print("hg is faster")
print(hgcd(34, 53))
print(gcd(34, 53))


print("h is significantly slower")
print(hgcd(32, 48))
print(gcd(32, 48))



print("g is faster")
print(hgcd(18, 45))
print(gcd(18, 45))

#print(hgcd(123, 87))

vector = [0, 1, 1, 1, 5, 2]
print(vector)
x = [[(3 ** (i * j) % 7) for i in range(6)] for j in range(6)]
print("x")
[print(a) for a in x]

transformed_vector = [sum([vector[i] * x[j][i] for i in range(6)]) % 7 for j in range(6)]
[print(a) for a in transformed_vector]

print([[x[j][i] for i in range(len(x[j]))] for j in range(len(x))])
quit()
y = [[(3 ** (i * j) % 7) for i in range(6)] for j in range(6)]
[print([ round(i)for i in a]) for a in y]

original_vector = [sum([transformed_vector[i] * y[j][i] for i in range(6)]) % 7 for j in range(6)]

original_vector = [original_vector[0]] + [original_vector[i] for i in range(len(original_vector) - 1, 0, -1)]
original_vector = [a for a in original_vector]
[print(round(a)) for a in original_vector]

exit()

for i in range(100):
	for j in range(100):
		
		#print(i, j)
		if hgcdCheck(i, j) < gcdCheck(i, j):
			print("hg is faster")
			print(i, j)
			#print(hgcd(i, j))
			#print()
			#print(gcd(i, j))
			print()
			#print("---------")
			#print(hgcd(i, j))

			#print()
			#print(gcd(i, j))
			#print("---------")
			#print()
		
		elif hgcdCheck(i, j) > gcdCheck(i, j):
			print("g is faster")
			print(i, j)
			#print(hgcd(i, j))
			print()
			#print(gcd(i, j))
		
		elif hgcdCheck(i, j) >= 2 * gcdCheck(i, j):
			print("h is significantly slower")
			#print(i, j)
			#print(hgcd(i, j))
			#print()
			#print(gcd(i, j))
			#h_is_significantly_slower = True
			print()
		
print(hgcd(123, 87))

print(hgcd(13, 21))

[print([j ** i % 7 for i in range(6)]) for j in range(6)]
print(sum([1, 5, 4, 6, 2, 3]) % 7)

'''
13 8
19 12
21 8
21 13
23 14
29 8
29 18
29 21
31 12
31 18
31 19
31 20
34 13
34 21
35 22
37 8
37 14
37 23
37 29
39 24
41 26
43 12
43 28
43 31
45 8
45 26
45 28
45 37
47 13
47 18
47 29
47 30
47 34
49 18
49 30
49 31
50 19
50 21
50 29
50 31
51 14
51 20
51 28
51 31
51 37
51 40
53 8
53 34
53 45
55 12
55 21
55 34
55 36
55 43
57 22
57 35
57 36
57 44
58 36
59 38
60 13
60 23
60 37
60 47
61 8
61 38
61 53
63 24
63 39
65 14
65 18
65 40
65 42
65 47
65 51
66 29
66 37
67 12
67 18
67 26
67 41
67 44
67 49
67 55
69 8
69 19
69 42
69 50
69 61
71 20
71 21
71 26
71 28
71 43
71 44
71 45
71 46
71 50
71 51
71 56
73 13
73 28
73 42
73 45
73 46
73 60
74 31
74 43
75 44
75 46
76 21
76 29
76 47
76 55
77 8
77 30
77 47
77 50
77 69
79 12
79 14
79 22
79 28
79 29
79 30
79 48
79 49
79 50
79 51
79 52
79 57
79 65
79 67
80 31
80 49
81 31
81 34
81 47
81 50
81 52
82 31
82 37
82 45
82 51
82 52
83 18
83 23
83 54
83 65
85 8
85 18
85 54
85 67
85 77
86 13
86 73
87 24
87 34
87 53
87 54
87 63
87 68
88 19
88 37
88 51
88 69
89 34
89 55
89 58
91 12
91 20
91 36
91 40
91 51
91 55
91 56
91 60
91 71
91 72
91 79
92 21
92 35
92 57
92 71
93 8
93 14
93 26
93 36
93 52
93 54
93 57
93 60
93 67
93 79
93 85
94 36
94 58
95 29
95 60
95 62
95 66
97 21
97 26
97 37
97 38
97 59
97 60
97 62
97 71
97 76
98 43
98 45
98 53
98 55
98 60
99 13
99 28
99 38
99 61
99 71
99 86
'''