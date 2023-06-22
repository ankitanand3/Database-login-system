#<Ankit> <Anand>
#MCS 260 Spring 2022 Project 2
#I hereby attest that I have adhered to the rules for projects as well as UIC’s Academic Integrity standards while completing this project.

import random #importing random function

password = [] #creating an empty list to store 1024 random created passwords
n = 0 #Counting number of password to be genrated
#PasswordGenerator:
"""This will generate random password for email"""
while n<1024: #Using while loop to generate exact 1024 random passwords
  upper_char = "AEIOU" #Uppercase characters to be randomly used in passwords.
  
  lower_char = "aeiou" #Lowercase characters to be randomly used in passwords.
  
  Charecters = upper_char + lower_char #Joining lowercas and Uppercase characters to create password
  len1 = [4,5,6,7,8] #List of numbers from which random length of password will be created
  rand_upper = random.choice(upper_char) #Choosing random upper letter charecter
  rand_lower = random.choice(lower_char) #Choosing random lower letter charecter
  rand_len = random.choice(len1) #Choosing random length of password
  pass1 = rand_upper + rand_lower #Joining upper and lower case characters for password
  for x in range(rand_len-2): #looping through random length
    
    pass1 = pass1 + random.choice(Charecters)
    pass_lst = list(pass1.split()) #Convering it into list
    random.shuffle(pass_lst) #Random shuffling the password list
    pa = "" #Creating empty pa string
  for x in pass_lst: #Looping through the password list
    pa = pa + x #Adding eacgh element to the empty password string
    adj = "" #Creating empty string to remove adjacent


  for a in pa: #looping through the string
  
    if adj == "" or a != adj[len(adj)-1]: #Checking for the repeated values
   
      adj = adj + a #Adding all values in empty string adj

  
  n = n + 1 #Counting n everytime to generate 1024 passwords

  
  password.append(adj) #Appending values everytime in the empty list rand_list
  continue #To continue the loop till it gives us desired number of outcomes

UIN_file = open("UIN.txt", "r") #Opening UIN.txt file to read

list_of_lists_UIN = [] #Creating empty list to store UIN values
for line in UIN_file: #Looping through each line of the file
  stripped_line = line.strip() #Using strip function
  line_list = stripped_line.split() #Using split function
  list_of_lists_UIN.append(line_list) #Appending all values in empty list created list_of_lists_UIN after spliting

UIN_file.close() #Closing file




UIN_list = [] #Creating empty list
for element in list_of_lists_UIN: #Looping through each element in the list list_of_lists_UIN
  
  if type(element) is list: #Checking element type if its list
    for item in element: 
      UIN_list.append(item) #Appending item to the empty list created UIN_list
      
  else:
    UIN_list.append(element)

UIN_list = list(dict.fromkeys(UIN_list)) #Removing duplicates from UIN_list

rev = [] #Creating empty list to store reversed value
for i in UIN_list: #Looping through each element in the list UIN_lists
  a = i[::-1] #Reversing all the UIN values in the list
  rev.append(a) #Appending item to the empty list created rev





s = [] #Creating empty list to store value added 0
for j in rev: #Looping through each element in the list rev
  
  while len(j) < 7: #Checking length of the element
    j += "0" #Adding 0 so that the total length should be 7
  s.append(j) #Appending it to empty list s


UIN = [] #Empty list to store all UIN
for k in s: #Looping through each element in the list s
  a2 = k[::-1] #Reversing all the UIN values in the list
  UIN.append(a2) #Appending it to empty list UIN



NetID_file = open("NetID.txt", "r") #Opening NetID.txt file to read

NetID_lists = [] #Creating empty list
for line in NetID_file: #Looping through each element in the file NetID.txt
  stripped_line = line.strip()
  line_list = stripped_line.split()
  NetID_lists.append(line_list) #Appending it to empty list NetID_lists

NetID_file.close() #Closing file

flat_list2 = [] #Creating empty list
for element in NetID_lists: #Looping through each element in the list NetID_lists
  
  if type(element) is list: #Checking element type if its list
    for item in element: 
      flat_list2.append(item) #Appending item to the empty list created flat_list2
      
  else:
    flat_list2.append(element)

flat_list2 = list(dict.fromkeys(flat_list2)) #Removing duplicates

email = [] #Creating empty list to store emails
for j in flat_list2: #Looping through each element in the list flat_list2
  j += "@uic.edu" #Adding @uic.edu in every username 
  email.append(j) #Appending item to the empty list created email


AllUsers = { UIN[i]:(email[i],password[i]) for i in range(len(UIN)) } #Creating a dictionary of name AllUsers to store Key UIN and Values Email and Password 


file = open("users.txt","w") #Writing a new file named users.txt to store dictionary values in it

for key, value in AllUsers.items(): 

 file.write('%s:%s\n' % (key, value)) #Writing key and values in text file

file.close() #Closing file

inp_email = input('Enter email: ') #Taking input email
inp_pass = input('Enter password: ') #Taking input password
list_of_users = [] #Creating empty list
c = open('users.txt') #Opening file users.txt

txt = c.read() #reading file

list_of_users.append(inp_email) 

if inp_email and inp_pass in txt: #Checking if input email and password are in the list
  print("You have successfully logged in!")
elif inp_email in txt and inp_pass not in txt: #Checking if only input email is in the list
  print("That password does not match the email provided.")
else: #Checking if input email and password both are not in the list
  print("That email is not in our system.")