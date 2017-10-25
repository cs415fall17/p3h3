import math
import numpy as np

def fft(a):
	# does fast fourier transform
	if len(a) == 1:
		return a
	else:
		a_even = [a[i] for i in range(len(a)) if i % 2 == 0]
		a_odd = [a[i] for i in range(len(a)) if i % 2 == 1]
		#a = a[0::1]
		#a = a[1::1]
		a_even = fft(a_even)
		a_odd = fft(a_odd)

		r = [0] * len(a)
		n_max = len(a) // 2
		# principle root of unity (w^1)
		e_exponent = (-2 * math.pi) / len(a)
		w = complex(math.cos(e_exponent), math.sin(e_exponent))

		for i in range(n_max):
			r[i] = 				a_even[i] + (w ** i) * a_odd[i]
			r[i + n_max] = 		a_even[i] - (w ** i) * a_odd[i]
		return r

def fftInverse(a):

	a = fft(a)

	inverted = a[0] + [a[i] for i in range(len(a) - 1, 0)]
	length_a = len(a)
	return [element // length_a for element in inverted]

def pad(a):
	# have to double the size with 0's?
	power_of_2 = 1
	while len(a) > power_of_2:
		power_of_2  = power_of_2 * 2

	while len(a) < power_of_2:
		a.append(0)

	return a

def multFFT(a, b):

	a = pad(a)
	b = pad(b)

	a = fft(a)
	b = fft(b)

	c = [a[i] * b[i] for i in len(a)]

	c = fftInverse(c)
	return c

def cooefficients(a, b):

	c = []
	for k in range(len(a)):
		sum_ = 0
		for j in range(k):
			sum_ = a[j] * b[k - j]
		c[k] = sum_
	return c

def outputToFile(file_name, file_string):

	file = open(file_name, 'w')
	file.write(file_string)
	file.close
# wrong
def printComplex(A):
	# A is a complex number
	a = A.real
	b = A.imag
	if abs(A.real) < 0.999:
		a = 0
	if abs(A.imag) < 0.999:
		b = 0
	#print(A)
	return complex(a, b)


#print(fft([1, 0]))

#print()
print([printComplex(i) for i in fft([-1, 1, -2, 0])])
print([printComplex(i) for i in fft([0, 2, 1, 1])])
print()
print(fft([-1, 0, 1, 2, -2, 1, 0, 1]))
print(np.fft.fft([-1, 0, 1, 2, -2, 1, 0, 1]))

print()
# doesn't work here
# aprroximation issues
print(fft([-1, 0, 1, 2, -2,0, 8, 5, 4, 1, 0, 1]))
print(np.fft.fft([-1, 0, 1, 2, -2,0, 8, 5, 4, 1, 0, 1]))
outputToFile("test.txt", "this is a test")
#e_exponent = (-2 * math.pi)/4
#print(complex(math.cos(e_exponent), math.sin(e_exponent )))
#print(complex(1/math.sqrt(2)), -1/math.sqrt(2))