
'''
This program computes the Fast Fourier Transform algorithm.  It is then timed against doing normal polynomial multiplication.
The Fast Fourier Transform algorithm:

1) Take a polynomial.
2) Split it into the even terms and odd terms(not even and odd powers).
3) Keep doing this untill there is only 1 term left.
4) Then take the value and multiply it by a root of unity.
5) Return the value up the call stack.
6) Multiply all values returned by roots of unity for each function call.
done


'''


import math
import numpy as np
import time

def fft(a):
	# does fast fourier transform
	if len(a) == 1:
		return a
	else:
		a_even = [a[i] for i in range(len(a)) if i % 2 == 0]
		a_odd = [a[i] for i in range(len(a)) if i % 2 == 1]

		a_even = fft(a_even)
		a_odd = fft(a_odd)

		r = [0] * len(a)
		n_max = len(a) // 2
		# principle root of unity (w^1)
		# e^(2(pi)/|a| )
		e_exponent = (2 * math.pi) / len(a)
		w = complex(math.cos(e_exponent), math.sin(e_exponent))


		# [0, n_max - 1] = [0, (len(a) // 2) - 1]
		for i in range(n_max):

			r[i] = 				a_even[i] + (w ** i) * a_odd[i]
			r[i + n_max] = 		a_even[i] - (w ** i) * a_odd[i]


		return r

def fftInverse(a):

	# computes the fft inverse
	a = fft(a)

	length_a = len(a)

	inverted = [a[0]] + [a[i] for i in range(len(a) - 1, 0, -1)]


	return [complex(element.real // length_a, element.imag // length_a) for element in inverted]

def pad(a):
	# adds 0's to the end of a
	power_of_2 = 1
	length_a = len(a)
	while length_a > power_of_2:
		power_of_2  *= 2


	# add 0's to a so len(a) is a power of 2
	a = a + [0 for i in range((power_of_2) - length_a)]
	# have to double the size with 0's after the padding has been added

	a = a + [0 for i in range(len(a))]

	return a

def multFFT(a, b):

	# does polynomial multiplication using fft
	a = pad(a)
	b = pad(b)

	a = fft(a)
	b = fft(b)

	c = [a[i] * b[i] for i in range(len(a))]


	c = fftInverse(c)
	return c

def multSlow(a, b):
	# does regular polynomial multiplication
	a = pad(a)
	b = pad(b)
	return [ sum([a[j] * b[k - j] for j in range(k + 1)]) for k in range(len(a))]

def outputToFile(file_name, file_string):

	# outputs to file_name
	file = open(file_name, 'w')
	file.write(file_string)
	file.close

def multFFTNumpy(A, B):

	# the numpy version of polynomial multiplication using fft
	a = np.fft.fft(A)
	b = np.fft.fft(B)

	C = [a[i] * b[i] for i in range(len(A))]
	m = np.fft.ifft(C)
	return m


def demo():

	# this demo shows the difference in the time it takes for regular polynomial multiplication contrasted to the
	# polynomial multiplication using fft
	start_0 = time.time()
	answer_0 = multFFT(
	[1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1],

	[1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1])
	end_0 = time.time()
	total_time_0 = end_0 - start_0
	print(total_time_0)

	start_1 = time.time()
	answer_1 = multSlow([1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1],

	[1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1])
	end_1 = time.time()
	total_time_1 = end_1 - start_1
	print(total_time_1)


	if total_time_0 < total_time_1:
		print('The fft algorithm is faster than regular multiplication')
		print()
		outputToFile("test.txt", str(total_time_0) + '\n' + str(total_time_1))

	else:
		print('Your values are too small to see the efficency of fft.')
		print()
demo()
