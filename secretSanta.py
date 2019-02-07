import random
from fbchat import Client
from fbchat.models import *
from getpass import getpass 

def secretSanta(names):

	couples = []
	willGive = []
	willBeGiven = []

	while len(willBeGiven) != len(names):
		tempWillGive = [name for name in names if name not in willGive] 
		name1 = random.choice(tempWillGive)
		
		tempWillBeGiven = [name for name in names if (name not in willBeGiven and name != name1)] 
		name2 = random.choice(tempWillBeGiven)

		couple = (name1,name2)
		willGive.append(name1)
		willBeGiven.append(name2)
		couples.append(couple)

	return couples

def getParam():

	nb = int(input("Please enter the number of secret santas: "))

	names = []
	for i in range(nb):
		response = input("Please enter the name of your friends : ")
		names.append(response)

	return names

def output(couples):

	for couple in couples:
		string = couple[0] + " is the secret Santa of " + couple[1]
		print(string)


def sendMessages(names,couples):

	username = str(input("Username: ")) 
	client = Client(username, getpass()) 
	
	for couple in couples:
		name1 = couple[0]
		name2 = couple[1]
		friends = client.searchForUsers(name1)
		user = friends[0] 
		print("User's ID: {}".format(user.uid))
		print("User's name: {}".format(user.name))

		string = couple[0] + " is the secret Santa of " + couple[1]
		spamString = """
───────────████──███────────────
──────────█████─████────────────
────────███───███───████──███───
────────███───███───██████████──
────────███─────███───████──██──
─────────████───████───███──██──
──────────███─────██────██──██──
──────██████████────██──██──██──
─────████████████───██──██──██──
────███────────███──██──██──██──
────███─████───███──██──██──██──
───████─█████───██──██──██──██──
───██████───██──────██──────██──
─████████───██──────██─────███──
─██────██───██─────────────███──
─██─────███─██─────────────███──
─████───██████─────────────███──
───██───█████──────────────███──
────███──███───────────────███──
────███────────────────────███──
────███───────────────────███───
─────████────────────────███────
──────███────────────────███────
────────███─────────────███─────
────────████────────────██──────
──────────███───────────██──────
──────────████████████████──────
──────────████████████████──────
────────────────────────────────
"""
		sent = client.send(Message(text=string), thread_id=user.uid, thread_type=ThreadType.USER)
		sent = client.send(Message(text=spamString), thread_id=user.uid, thread_type=ThreadType.USER)

		if sent: 
			print("Message sent successfully!") 

if __name__ == '__main__':
	
	names = getParam()
	if names:
		couples = secretSanta(names)

	send = str(input("Do you want to send the results to your friends on facebook ? (y/n)")) 
	send = send.strip()

	if send == "y":
		sendMessages(names,couples)





