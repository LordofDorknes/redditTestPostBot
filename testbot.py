import time # unnecessary import
import praw #import reddit api
f = open('password.txt', 'r') # read password from file
password = f.read()
#password variable for login set from file

user_agent = ("Some Testing Bot v 0.0.1 by /u/LordofDorknes"
              "github.com/LordofDorknes/redditTestPostBot")
# define unique useragent

r = praw.Reddit(user_agent=user_agent)
r.login('TestingBotAccount1', password) #log in
PostTitle = 'Test Post 1'
PostText = 'Test post among many others'
r.submit('test',PostTitle,text=PostText)

