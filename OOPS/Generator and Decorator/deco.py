import time

def fun(func):
	def fun2(*args,**kwargs):
		st=time.time()
		print("starting time ",st)
		result=func(*args,**kwargs)
		et=time.time()
		print("ending time",et)
		return result
	return fun2

@fun
def fibo(n):
	a,b=0,1
	for i in range(n):
		yield a
		a,b=b,a+b

n=int(input("enter value"))
fibonacci=fibo(n)

print("series")
for i in fibonacci:
	print(i)
