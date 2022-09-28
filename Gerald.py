import praw
from getpass import getpass

# Obtaining and setting up credentials
c = open("client.id", "r")
id = str(c.read()).strip()
c.close()

s = open("secret.txt", "r")
secret = str(s.read()).strip()
s.close()

u = open("user.txt", "r")
user = str(u.read()).strip()
u.close()

reddit = praw.Reddit()
verbose = False


def investigateSubreddit():
	print()

def investigateUser():
	print()

def search():
	print()

if (len(input()) == 2):
	try:
		n = open("username.txt")
		name = str(n.read()).strip()
		n.close()
		p = open("password.txt")
		pwd = str(p.read()).strip()
		p.close()
		reddit = praw.Reddit(
			user_agent=user,
			client_id=id,
			client_secret=secret,
			username=name,
			password=pwd
		)
	except:
		reddit = praw.Reddit(
			user_agent=user,
			client_id=id,
			client_secret=secret
		)
else:
	cli = input().split(" ")
	if ( len(cli) == 3 and cli[2].toLowerCase() == "-s"):
		print("Username: ")
		uname = input()
		print("Password: ")
		pword = getpass()
		reddit.username=uname
		reddit.password=pword
	elif ( len(cli) == 4 and cli[2].toLowerCase() == "-u"):
		reddit.username=cli[3]
		print("Password: ")
		reddit.password=getpass()
	elif (len(cli) == 3 and cli[2].toLowerCase() == "-v"):
		print("Username: ")
		reddit.username=input()
		print("Password: ")
		reddit.password=getpass()
		verbose=True

while(True):
	print("Select a function: ")
	if (verbose):
		print("Input your single choice as a digit")
		print("1. Investigate Subreddit")
		print("2. Investigate User")
		print("3. Search")
	if (input() == '1'):
		investigateSubreddit()
	elif(input() == '2'):
		investigateUser()
	elif(input() == '3'):
		search()
	else:
		break

