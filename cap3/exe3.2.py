def do_twice(f,num):
	f(num)
	f(num)

def print_spam(bruce):
	print(bruce)

def do_four(f,bruce):
	do_twice(f,bruce)
	do_twice(f,bruce)

do_four(print_spam,'spam')