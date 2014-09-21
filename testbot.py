import time # unnecessary import
import praw #import reddit api
import webbrowser
f = open('password.txt', 'r') # read password from file
password = f.read()
#password variable for login set from file
user_agent = ("Some Testing Bot v 0.0.1 by /u/LordofDorknes"
              "github.com/LordofDorknes/redditTestPostBot")
# define unique useragent
r = praw.Reddit(user_agent=user_agent)
r.login('TestingBotAccount1', password) #log in
PostTitle = 'Test Post 5'
PostText = 'trying to find out if captcha id is directly related to captcha url'
PostURL = 'www.github.com/LordofDorknes/redditTestPostBot'
Subreddit= 'test'
#returnedcaptcha={'iden' : 'the captcha id', 'captcha': 'the captcha response text'}
r.submit(Subreddit,PostTitle, url=PostURL)
"""
try:
   r.submit(Subreddit,PostTitle, url=PostURL, captcha=None raise_captcha_exception=True)
except praw.errors.InvalidCaptcha as E:
    captchaurl = 'http://www.reddit.com/captcha/{0}.png'.format(E.response['captcha']) #'http://www.reddit.com/captcha/'%id.pngE.response['captcha']
    webbrowser.open_new_tab(captchaurl)
    print('raw id:' + E.response['captcha'])
    print('url:' + captchaurl)
    captchareturn = {'iden' : E.response['captcha'], 'captcha': input('Captcha:')}
   """
    #kill me


"""submit(subreddit, title, text=None,
url=None, captcha=None, save=None,
send_replies=None, resubmit=None)"""

