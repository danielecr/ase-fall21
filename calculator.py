#calculator.py

def sum(m,n):
	res = m;
	if n < 0:
		for x in range( - n ):
			res -= 1
	else:
		for x in range(0, n):
			res += 1
	return res;

def subtract(m,n):
	res = m;
	if n >= 0:
		for x in range(n):
			res -= 1
	else:
		for x in range(0, -n):
			res += 1
	return res;


def divide(m, n):
	if n == 0:
		raise ZeroDivisionError
	if abs(m) < abs(n):
		return 0
	reverse = (m < 0 and  n > 0) or (m > 0 and n < 0)
	m1 = abs(m)
	n1 = abs(n)
	remain = m1
	quot = 0;
	while remain >0:
		remain = remain -n1
		quot = quot + 1
	if remain < 0:
		quot-=1
	if reverse:
		return - quot 
	else:
		return quot

def multiply(m, n):
	reverse = (m < 0 and  n > 0) or (m > 0 and n < 0)
	m1 = abs(m)
	n1 = abs(n)
	result = 0
	for i in range(0,n1):
		result += m1
	return -result if reverse else result


if __name__ == "__main__":
	b = multiply(2,4)
	print(b)

	s = sum(3,4)
	print(s);

	d = divide(7,3)
	print("division", d)

	#d = divide(3, 0)
	#print("division", d)

	d = divide(-3, 1)
	print("division", d)

	d = divide(3, -2)
	print("division", d)
