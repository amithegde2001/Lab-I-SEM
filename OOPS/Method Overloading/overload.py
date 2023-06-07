def addition(name=None,age=None):
	if name is not None and age is None:
		print("hii",name)
	
	elif name is not None and age is not None:
		print(f"hii {name} and your age is {age}")

	else:
		print("hii")


addition()
addition("amit")
addition("amit",21)
