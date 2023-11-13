import os, sys, time
from dotenv import load_dotenv
from ringcentral import SDK

load_dotenv()

class Person:
  def __init__(self, name, phoneNumber):
    self.name = name
    self.phoneNumber = phoneNumber

#get phone numbers from guest list - text file 
def getPhoneNumbers():
    h = open('numbers.txt', 'r')

    content = h.readlines()

    for line in content:
        p = Person(createRecipient())
        sendMessage(p)
        

#seperate string into recipent name and phone number 
def createRecipient(String line):
    #split
     i = line.split()
     name = i[0]
     phoneNumber = i[1]

     #create 
     recipent = Person(name,phoneNumber)

     return recipent

def sendMessage(Person p):
    platform.post('/restapi/v1.0/account/~/extension/~/sms',
{
    'from' : { 'phoneNumber': sendNumber },
    'to'   : [ {'phoneNumber': p.phoneNumber} ],
    'text' : 'Hi! You are invited to , please RSVP'
})

def main():
    getPhoneNumbers()

 main()   
