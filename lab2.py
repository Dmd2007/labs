"""
lab2.py
Dylan Durand
2/14/2018

"""

def is_even(n):
	"""
    Checks if number is even
    n: integer
  	Returns: True if number is even, False otherwise

  	>>> is_even(2)
  	True
  	>>> is_even(5)
  	False
	"""

	if n % 2 == 0:
		return True
	else: 
		return False

if __name__ == '__main__':
	import doctest
	doctest.testmod()