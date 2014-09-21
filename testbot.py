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
PostTitle = 'Test Post 3'
PostText = 'Test post among many others, this one has a link to the code that posted it'
PostURL = 'www.github.com/LordofDorknes/redditTestPostBot'
r.submit('test',PostTitle, url=PostURL)

"""submit(subreddit, title, text=None,
url=None, captcha=None, save=None,
send_replies=None, resubmit=None)"""
