while(True):
	print("1.String Operations \n 2.Tuple Operations")
	ch=int(input("enter your choice"))
	if(ch==1):
		str1=input("enter first string ")
		str2=input("enter second string ")
		print("1.isupper \n 2.islower \n 3.toLowercase \n 4.toUppercase \n 5.length \n 6.splitting \n 7.reverse \n 8. slicing \n 9.concatination \n 10.printing multiple times ")
		while(True):
			ch2=int(input("enter the operation"))
			if(ch2==1):
				print(f"IS {str1} is in uppercase ? ",str1.isupper())
			elif(ch2==2):
				print(f"Is {str2} is in lowercase ? ",str2.islower())
			elif(ch2==3):
				print(f" {str1} in lowercase = ",str1.lower())
			elif(ch2==4):
				print(f"{str2} in uppercase = ",str2.upper())
			elif(ch2==5):
				print(f"length of {str1} = ",len(str1))
			elif(ch2==6):
				print(f" splitting of {str2} = ",str2.split())
			elif(ch2==7):
				print(f"reverse of {str1} = ", str1[::-1])
			elif(ch2==8):
				print(f"slicing of {str2} = ",str2[2:6])
			elif(ch2==9):
				print(f"concatinaiton = ",str1+str2)
			elif(ch2==10):
				print(f"{str2}  multliple times = ",5*str2)
			else:
				break
	if(ch==2):
		tup1=(1,2,3,4,5)
		tup2=(7,8,9,10,4)
		print("1.length \n 2.slicing \n 3.maximum item \n 4.minimum item \n 5. Index of particular value  tuple \n 6.concatination \n 7.repeatation \n 8.reversign \n 9.sorting tuple elements \n 10.sums up ")
		while(True):
			ch3=int(input("enter the operation "))
			if(ch3==1):
				print(f"Length of the tuple {tup1} = ",len(tup1))
			elif(ch3==2):
				print(f"slicing of tuple {tup2} = ",tup2[2:4])
			elif(ch3==3):
				print(f"maximum value of {tup1} = ",max(tup1))
			elif(ch3==4):
				print(f"minimum value of {tup2} = ",min(tup2))
			elif(ch3==5):
				print(f"index of 3 in {tup1} = ",tup1.index(3))
			elif(ch3==6):
				print(f"concationaiton of {tup1} and {tup2} = ",tup1+tup2)
			elif(ch3==7):
				print(f"repeatation of {tup1} = ",4 * tup1)
			elif(ch3==8):
				print(f"reverse of {tup2} = ",tup2[::-1])
			elif(ch3==9):
				print(f"sorting of {tup1} = " ,sorted(tup1))
			elif(ch3==10):
				print(f"total sum of {tup2} = ",sum(tup2))
			else:
				break
				


	else:
		print("invalid choice ")
		exit()

