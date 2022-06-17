print("Hello World")
counties = ["Arapahoe", "Denver", "Jefferson"]
print(counties)
#counties = list()
print(counties)
print(counties[0])
print(counties[-1])
print(counties[-2])
print(len(counties))
print(counties[0:1])
print(counties[0:2])
print(counties[:1])
print(counties[:2])
print(counties[0:])
print(counties[1:])
print(counties.append("El Paso"))
print(counties)
print(counties.insert(2, "El Paso"))
print(counties)
print(counties.remove("El Paso"))
print(counties)
print(counties.pop(3))
print(counties)
counties[2] = "El Paso"
print(counties)
counties_tuple = ("Arapahoe", "Denver", "Jefferson")
print(counties_tuple)
print(len(counties_tuple))
print(counties_tuple[1])
counties_dict = {}
print(counties)
counties_dict["Arapahoe"] = 422829
print(counties_dict)
counties_dict["Denver"]= 463353
counties_dict["Jefferson"] = 432438
print(counties_dict)
print(len(counties_dict))
print(counties_dict.items())
print(counties_dict.keys())
print(counties_dict.values())
print(counties_dict.get("Denver"))
print(counties_dict["Arapahoe"])
voting_data =[]
print(voting_data.append({"county":"Arapahoe", "registered_voters": 422829}))
print(voting_data.append({"county":"Denver", "registered_voters": 463353}))
print(voting_data.append({"county":"Jefferson", "registered_voters": 432438}))
print(voting_data)
#Decision statement

#How many votes did you get?
my_votes = int(input("How many votes did you get in the election"))
#Total votes in the election
total_votes= int(input("What is the total votes in the election"))
#Calculate the percentage of votes you received 
percentage_votes = (my_votes/total_votes)*100
print("I received " + str(percentage_votes)+ "% of the total votes.")

# If statement
#If condition:
#statement 1
#statement 2

counties = ["Arapahoe", "Denver", "Jefferson"]
print(counties)
if counties[1] == 'Denver':
    print(counties[1])

#if-else Statement
# if condition:
#statement1 
#statement2
#Else:
#statemnet 1
#statement 2

temperature = int(input("What is the temperature outside?"))
print(temperature)

if temperature >80:
    print("turn on the AC")
else: 
    print("Open the windows")


# What is the score?

score = int(input("WHat is your test score? "))

if  (score >= 90):
    print("Your grade is a A")
if (score >= 80) :
    print("Your grade is a B")
if (score >= 70) :
    print("Your grade is a C")
if (score >= 60) :
    print("Your grade is a D")
else:
    print("Your grade is an F")


score = int(input("WHat is your test score?"))
if (score >= 90):
    print('Your grade is a A.')
elif (score >= 80):
    print('Your grade is a B.')
elif (score >=70):
    print('Your grade is a C.')
elif (score >=60):
    print('Your grade is a D.')
else:
    print('Your grade is an F')
print("hello World")


import datetime
now= datetime.datetime.now()
print("The time right now is", now)

# the Csv module
import csv
dir(csv)

dir(int)
dir(float)
dir(bool)
dir(list)
dir(tuple)
dir(dict)
dir(datetime)









