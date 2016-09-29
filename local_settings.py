'''
fill in the name of the account you're tweeting from here.
'''

#configuration
MY_CONSUMER_KEY = '6x6V3R6mhoLaoQDeHVsOnrqor'
MY_CONSUMER_SECRET = '5dedaxfX19Bhiiw2GtLQsKpj29KA6ibiOTF8SpXvrVnNgVZ7eN'
MY_ACCESS_TOKEN_KEY = '779341059755220992-vfTq6o2T1day6EjjLdkwAl2ZrX4Dqo1'
MY_ACCESS_TOKEN_SECRET = 'VH1wqyEM6dOd2ULVbKeMLn52OfOGGFdnij6DWsZnGWMtj'

SOURCE_ACCOUNTS = ["martylyricfm"] #A list of comma-separated, quote-enclosed Twitter handles of account that you'll generate tweets based on. It should look like ["account1", "account2"]. If you want just one account, no comma needed.
ODDS = 7 #How often do you want this to run? 1/8 times?
ORDER = 2 #how closely do you want this to hew to sensical? 1 is low and 3 is high.
DEBUG = False #Set this to False to start Tweeting live
STATIC_TEST = False #Set this to True if you want to test Markov generation from a static file instead of the API.
TEST_SOURCE = ".txt" #The name of a text file of a string-ified list for testing. To avoid unnecessarily hitting Twitter API.
TWEET_ACCOUNT = "smartywhelan" #The name of the account you're tweeting to.
