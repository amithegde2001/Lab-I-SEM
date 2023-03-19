d=dict()
class Employee:
	def input(self):
		self.name=input("enter employee name :\n ")
		self.address=input("enter the address: \n")
		self.pan=input("enter pan details : \n ")
		self.basic=int(input("enter basic salary : \n"))
		self.tds=int(input("enter tds : \n "))
		self.deduct=int(input("enter deduction \n "))
		self.hra=1.25*self.basic
		self.da=0.25*self.basic
		self.gross=self.basic+self.hra+self.da
		self.net=self.gross-self.deduct
		self.update()
	
	def update(self):
		d.update({self.name: {
			"name":self.name,
			"address":self.address,
			"pan":self.pan,
			"basic":self.basic,
			"tds":self.tds,
			"deduct":self.deduct,
			"hra":self.hra,
			"da":self.da,
			"gross":self.gross,
			"net":self.net,
		}})
	
	def search(self,name):
		flag=0
		for key in d:
			if key == name:
				print("employee found")
				for i in d[key]:
					print(i,d[key][i])
					flag=1
		if flag==0:
			print("no record found")
	
	def printemp(self):
		for key in d:
			print(key,d[key])


class employeee(Employee):
	em=Employee()
	while(True):
		ch=int(input("\n 1.to add employee \n 2.print all employees \n 3.find employee by name \n 4.exit \n"))
		if ch==1:
			em.input()
		elif ch==2:
			em.printemp()
		elif ch==3:
			name=input("enter employee name :")
			em.search(name)
		elif ch==4:
			break
	print("thank you for using employee management system ")

