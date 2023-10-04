
from callLimit import callLimit

@callLimit(3)
def f(value, x):
    print ("f()")

@callLimit(1)
def g():
    print ("g()")

for i in range(3):
	f(value=1, x='hi')
	# g()