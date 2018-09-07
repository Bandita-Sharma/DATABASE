#Que1-->Write a python script to create a databse of students named Students.
import pymongo
client=pymongo.MongoClient()
database=client['Studentdb']
print("database created")
collection=database['studenttbl']
print("table created")
print()

#Que2-->Take students name and marks(between 0-100) as input from user 10 times using loops.
print('Enter Detail Of Student')
for i in range (10):
    fn=input('enter the name:')
    mrk=int(input('enter the marks:'))

#Que3-->Add these values in two columns named "Name" and "Marks" with the appropriate data type.
for i in range(10):
    collection.insert_one({'Name':fn,'Mark':mrk})
print('VALUES INSERTED IN TABLE')

#Que4-->Print the names of all the students who scored more than 80 marks.
print('MARKS GREATER THAN 80')
data=collection.find({'Mark':{"$gt" : 80}})
for document in data:
    print(document)

