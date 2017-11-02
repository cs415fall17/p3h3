import math
import numpy as np
# use time
import timeit

def fft(a):
	# does fast fourier transform
	if len(a) == 1:
		return a
	else:
		a_even = [a[i] for i in range(len(a)) if i % 2 == 0]
		a_odd = [a[i] for i in range(len(a)) if i % 2 == 1]
		'''
		if len(a) >= 4:
			print(a_even)
			print(a_odd)
		'''
		a_even = fft(a_even)
		a_odd = fft(a_odd)

		r = [0] * len(a)
		n_max = len(a) // 2
		# principle root of unity (w^1)
		# e^(2(pi) )
		e_exponent = (2 * math.pi) / len(a)
		w = complex(math.cos(e_exponent), math.sin(e_exponent))
		# [1, 2, 1] -> 121
		#print([w ** i for i in range(n_max )])
		# [0, n_max - 1] = [0, (len(a) // 2) - 1]
		for i in range(n_max):
			#print(w ** i)
			#print(i)
			r[i] = 				a_even[i] + (w ** i) * a_odd[i]
			r[i + n_max] = 		a_even[i] - (w ** i) * a_odd[i]
		print()
		return r

def fftInverse(a):
	#print("a", a)
	a = fft(a)
	#print("fft(a)", a)
	length_a = len(a)
	# [len(a) - 1, 1]
	inverted = [a[0]] + [a[i] for i in range(len(a) - 1, 0, -1)]
	#print("inverted", inverted)
	#final_answer = [complex(element.real // length_a, element.imag // length_a)  for element in inverted]
	return [complex(element.real // length_a, element.imag // length_a) for element in inverted]

def pad(a):
	power_of_2 = 1
	length_a = len(a)
	while length_a > power_of_2:
		power_of_2  = power_of_2 * 2
	#print(power_of_2)
	#print(a)
	#print(a + a + [0 for i in range((power_of_2) - length_a)])
	#quit()

	# add 0's to a so len(a) is a power of 2
	a = a + [0 for i in range((power_of_2) - length_a)]
	# have to double the size with 0's after the padding has been added
	print(a)
	a = a + [0 for i in range(len(a))]
	print(a)
	#quit()
	return a

def multFFT(a, b):

	a = pad(a)
	b = pad(b)
	#print(a)
	#print(b)
	#quit()
	a = fft(a)
	b = fft(b)
	#print("fft(a)", a)
	#print("fft(b)", b)
	c = [a[i] * b[i] for i in range(len(a))]
	#print("c", c)
	#d = cooefficients(a, b)
	#print("d", d)
	c = fftInverse(c)
	return c

def multSlow(a, b):
	a = pad(a)
	b = pad(b)
	return [ sum([a[j] * b[k - j] for j in range(k + 1)]) * 1.0 for k in range(len(a))]

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

#print([printComplex(i) for i in fft([-1, 1, -2, 0])])
#print([printComplex(i) for i in fft([0, 2, 1, 1])])
#print()
#print(fft([-1, 0, 1, 2, -2, 1, 0, 1]))
#print(np.fft.fft([-1, 0, 1, 2, -2, 1, 0, 1]))

#print()
# from http://pythoncentral.io/time-a-python-function/

def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

def check():
	return fft(pad([-1, 0, 1, 2, -2,0, 8, 5, 4, 1, 0, 1]))
def multFFTNumpy(A, B):

  a = np.fft.fft(A)
  b = np.fft.fft(B)

  C = [a[i] * b[i] for i in range(len(A))]
  m = np.fft.ifft(C)
  return m

#print(fft(pad([-1, 0, 1, 2, -2,0, 8, 5, 4, 1, 0, 1])))
#print(np.fft.fft(pad([-1, 0, 1, 2, -2,0, 8, 5, 4, 1, 0, 1])))
#n = wrapper(fft, pad([-1, 0, 1, 2, -2,0, 8, 5, 4, 1, 0, 1]))
#print(timeit.timeit(n, number = 1))
#outputToFile("test.txt", str(timeit.timeit(n, number = 1)))
a = [1, 2, 1]
#print("decimal version if [1, 2, 1] was interpreted as a partial result from a binary multiplication")
#print(sum([a[i] * (2 ** i) for i in range(len(a))]))

#print()
#x = multFFT([1,1, 2, 3, 4, 5, 6, 7], [7, 6, 5, 4, 3, 2, 1, 1])
#x = [a.real for a in x]
#print("final_answer", x)
#y = multFFTNumpy([1,1, 2, 3, 4, 5, 6, 7, 0, 0, 0, 0, 0, 0, 0, 0], [7, 6, 5, 4, 3, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0])
#y = [round(a.real) for a in y]
#print("numpy version")
#print("final_answer", y)
#n = multSlow([1,1, 2, 3, 4, 5, 6, 7], [7, 6, 5, 4, 3, 2, 1, 1])
#print("final_answer", n)
print(fftInverse([1, -1, 2, 0, -1, 1, 0, 1]))
quit()
my_code =[round(a.real) for a in fft([-1, 0, 1, 2, -2,0, 8, 5, 4, 1, 0, 1, 0, 0, 0, 0])]
x = [round(a.real) for a in np.fft.fft([-1, 0, 1, 2, -2,0, 8, 5, 4, 1, 0, 1, 0, 0, 0, 0])]
print(np.fft.fft([-1, 0, 1, 2, -2,0, 8, 5, 4, 1, 0, 1, 0, 0, 0, 0]))
print(fft([-1, 0, 1, 2, -2,0, 8, 5, 4, 1, 0, 1, 0, 0, 0, 0]))

for i in range(len(my_code)):
	if my_code[i] != x[i]:
		print(my_code[i], x[i])
		print("fail")
print(my_code)
print(x)
outputToFile("test.txt", "this is a test")

'''
e_exponent = (-2 * math.pi)/8
print(complex(math.cos(e_exponent), math.sin(e_exponent )))
print(complex(1/math.sqrt(2)), -1/math.sqrt(2))
'''