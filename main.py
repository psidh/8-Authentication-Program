import csv
import itertools
import random
import sys
import threading
import time

data_dict = {}
security_list=[]

print("This websites is for army  ")
print("You can only register with Gmail accounts on this website")
#_______________________________________________________________________________________________
#_______________________________________________________________________________________________
def register():
	email_ = input("Enter your email id: ").lower()
	password = input("create your password: ")
	password2 = input("confirm your password: ")
	sec_num = int(input("Enter your security number (CONFIDENTIAL): "))
	integer = random.randint(1000000, 9999999)

	print(integer)
	int_input = int(input("Enter the Satellite Verification code: \n"))
	if int_input == integer:
		if "@gmail.com" in email_:
			if password == password2:

				security_list.append(sec_num)
				data_dict[email_] = password
				# print(security_list)

				print("           AUTHENTICATION VERIFIED✅ | ACCESS GRANTED")
				with open("data.txt", "a") as data:
					data.write(f"{email_} is associated with security number: {sec_num} | Password is {password}\n")
			else:


				print("INVALID INPUT !")
				register()
		else:



			print("Login through GMAIL Accounts only ! or Turn off caps lock")
			register()
	else:


		print("           INCORRECT CODE | ACCESS DENIED")


#_______________________________________________________________________________________________
#_______________________________________________________________________________________________
def login():
	integer = random.randint(100000,999999)
	email_ = input("Enter your email id: ").lower()
	password = input("create your password: ")
	sec_num = int(input("Enter your security number (CONFIDENTIAL): \n"))
	print(integer)
	int_input = int(input("Enter the Satellite Verification code: "))
	if int_input == integer:
		if sec_num in security_list and email_ in data_dict and password == data_dict[email_]:




			print("            AUTHENTICATION VERIFIED✅ | ACCESS GRANTED")


		else:


			print("           UNAUTHORISED LOGIN ❗️| ACCESS DENIED")
			login()
	else:





		print("           UNAUTHORISED LOGIN⚓︎ | ACCESS DENIED")
		print("           PROGRAM TERMINATED ®")
#_______________________________________________________________________________________________
#_______________________________________________________________________________________________

# INPUT CHOICES

def choice():
	print("Register | Login | Reset Credentials")
	prompt  = input("Enter your command >>> \n").lower()

	if prompt == "register":
		register()

	#___________________________________________________________________________________________

	elif prompt == "login":
		login()

	#___________________________________________________________________________________________
	else:
		pass

choice()

curr = time.time()
curr2 = time.ctime(curr)

done = False


