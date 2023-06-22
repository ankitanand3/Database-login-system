#<Ankit> <Anand>
#MCS 260 Spring 2022 Project 2
#I hereby attest that I have adhered to the rules for projects as well as UIC’s Academic Integrity standards while completing this project.

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