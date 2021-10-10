#calculator.py

def sum(m,n):
	res = m;
	if n < 0:
		for x in range(abs(n)):
			res -= 1
	else:
		for x in range(0, n):
			res += 1
	return res;

def divide(m, n):
	if n == 0:
		return 0
	if abs(m) < abs(n):
		return 0
	reverse = False
	if (m < 0 and  n > 0) or (m > 0 and n < 0):
		reverse = True
	m1 = abs(m)
	n1 = abs(n)
	remain = m1
	quot = 0;
	while remain >0:
		remain = remain -n1
		quot = quot + 1
	if reverse:
		return 1 - quot
	else:
		return quot -1;

def multiply(m, n):
	return m * n

def subtract(m, n):
	return m - n

s = sum(3,4)
print(s);

d = divide(7,3)
print("division", d)

d = divide(3, 0)
print("division", d)

d = divide(-3, 1)
print("division", d)

d = divide(3, -2)
print("division", d)
