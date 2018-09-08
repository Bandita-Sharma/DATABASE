#Que1-->Write a python script to create a databse of students named Students.
import pymongo
client=pymongo.MongoClient()
'''CREATES DATABASE'''
database=client['Studentdb']  
print("database created")
'''CREATES TABLE'''
collection=database['studenttbl']
print("table created")
print()

#Que2-->Take students name and marks(between 0-100) as input from user 10 times using loops.
print('Enter Detail Of Student')
record=[]
for i in range (10):
    record.append({"name":input(),"Marks":int(input())})
print()

#Que3-->Add these values in two columns named "Name" and "Marks" with the appropriate data type.
'''insert rows in table'''
data=collection.insert_many(record)   
print('VALUES INSERTED IN TABLE')
for data in collection.find():
        print(data)
print()

#Que4-->Print the names of all the students who scored more than 80 marks.
print('MARKS GREATER THAN 80:')
for document in collection.find():
    if document["Marks"]>80:
        print(document["name"])
